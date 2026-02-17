#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self: object, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self: object, data: Any) -> bool:
        pass

    def format_output(self: object, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self: "NumericProcessor", data: Any) -> bool:
        if type(data) is not list:
            return False
        try:
            len(data)
            sum(data)
            for item in data:
                item + 2
            return True
        except Exception:
            return False

    def process(self: "NumericProcessor", data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid numeric data"
        count = len(data)
        total = sum(data)
        avg = total / count if count > 0 else 0.0
        return f"Processed {count} numeric values, sum={total}, avg={avg:.1f}"

    def format_output(self: "NumericProcessor", result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self: "TextProcessor", data: Any) -> bool:
        try:
            if len(data) < 0:
                return False
            data.split()
            data.lower()
            return True
        except Exception:
            return False

    def process(self: "TextProcessor", data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid text data"
        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"

    def format_output(self: "TextProcessor", result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self: "LogProcessor", data: Any) -> bool:
        try:
            parts = data.split(":", 1)
            if len(parts) != 2:
                return False
            parts[0].strip()
            parts[1].strip()
            return True
        except Exception:
            return False

    def process(self: "LogProcessor", data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid log format"
        parts = data.split(":", 1)

        level = parts[0].strip()
        message = parts[1].strip()
        tag = "[ALERT]" if level in ["ERROR", "CRITICAL"] else "[INFO]"
        return f"{tag} {level} level detected: {message}"

    def format_output(self: "LogProcessor", result: str) -> str:
        return super().format_output(result)


def run_processor(proc: DataProcessor, data: Any, name: str,
                  val_msg: str) -> None:
    print(f"Initializing {name}...")
    print(f"Processing data: {data}")
    if proc.validate(data):
        print(f"Validation: {val_msg}")
        result = proc.process(data)
    else:
        print("Validation failed.")
        result = proc.process(data)
    print(proc.format_output(result))
    print()


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_data: list[int] = [1, 2, 3, 4, 5]
    run_processor(
        NumericProcessor(), num_data, "Numeric Processor",
        "Numeric data verified"
    )

    text_data: str = "Hello Nexus World"
    run_processor(TextProcessor(), text_data, "Text Processor",
                  "Text data verified")

    log_data: str = "ERROR: Connection timeout"
    run_processor(LogProcessor(), log_data, "Log Processor",
                  "Log entry verified")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    data = [
        ([1, 2, 3], NumericProcessor()),
        ("Code Nexus", TextProcessor()),
        ("INFO: System ready", LogProcessor()),
    ]
    i: int = 1
    for input_data, obj in data:
        print(f"Result {i}: {obj.process(input_data)}")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
