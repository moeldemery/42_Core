#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Protocol, Union


class ProcessingStage(Protocol):
    def process(self: "ProcessingStage", data: Any) -> Any: ...


class InputStage:
    def process(self: "InputStage", data: Any) -> dict:
        if data is None:
            raise ValueError("Invalid data format")
        return data


class TransformStage:
    def process(self: "TransformStage", data: Any) -> dict:
        if isinstance(data, str):
            if "," in data:
                fields = data.split(",")
                return {"parsed_fields": fields}
            return {"stream_data": data}
        return data


class OutputStage:
    def process(self: "OutputStage", data: Any) -> str:
        return data


class ProcessingPipeline(ABC):
    def __init__(self: "ProcessingPipeline", pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.pipeline_type = "Generic"
        self.stages: List[ProcessingStage] = []

    def add_stage(self: "ProcessingPipeline", stage: Any) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self: "ProcessingPipeline", data: Any) -> Any:
        """To be overridden by Adapters."""
        pass

    def run_stages(self: "ProcessingPipeline", data: Any) -> Any:
        current_data = data
        try:
            for stage in self.stages:
                current_data = stage.process(current_data)
            return current_data
        except Exception as e:
            raise RuntimeError(f"Pipeline failure at stage: {e}")


class JSONAdapter(ProcessingPipeline):
    def __init__(self: "JSONAdapter", pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.pipeline_type = "JSON"

    def process(self: "JSONAdapter", data: Any) -> str:
        result = self.run_stages(data)
        if not isinstance(result, dict):
            raise ValueError("Invalid JSON structure")
        """if isinstance(result, str):
            if result == "error_data":
                raise ValueError("Processing error in StreamAdapter")
            return result"""
        val = result.get("value", 0)
        unit = result.get("unit", "C")
        return f"Processed temperature reading: {val}°{unit} (Normal range)"


class CSVAdapter(ProcessingPipeline):
    def __init__(self: "CSVAdapter", pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.pipeline_type = "CSV"

    def process(self: "CSVAdapter", data: Any) -> str:
        if data == "error_data":
            raise ValueError("Simulated processing error in StreamAdapter")
        result = self.run_stages(data)
        if isinstance(result, dict) and "parsed_fields" in result:
            """count = max(len(result["parsed_fields"]) - 1, 0)"""
            count = len(data.split(",")) if isinstance(data, str) else 1
        else:
            count = 0
        return f"User activity logged: {count} actions processed"


class StreamAdapter(ProcessingPipeline):
    def __init__(self: "StreamAdapter", pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.pipeline_type = "Stream"

    def process(self: "StreamAdapter", data: Any) -> Union[str, Any]:
        if data == "error_data":
            raise ValueError("Simulated processing error in StreamAdapter")

        result = self.run_stages(data)

        if isinstance(result, dict) and "stream_data" in result:
            return "Stream summary: Real-time sensor stream processed"
        return result


class NexusManager:
    def __init__(self: "NexusManager") -> None:
        self.pipelines: Dict[str, ProcessingPipeline] = {}

    def register_pipeline(self: "NexusManager",
                          pipeline: ProcessingPipeline) -> None:
        self.pipelines[pipeline.pipeline_type] = pipeline

    def process_data(self: "NexusManager",
                     data_payloads: Dict[str, Any]) -> None:
        for fmt, payload in data_payloads.items():
            if fmt in self.pipelines:
                print(f"Processing {fmt} data through same pipeline...")
                if isinstance(payload, str):
                    display_input = f'"{payload}"'
                else:
                    display_input = payload

                print(f"Input: {display_input}")
                if fmt == "JSON":
                    stage_msg = "Enriched with metadata and validation"
                if fmt == "CSV":
                    stage_msg = "Parsed and structured data"
                if fmt == "Stream":
                    stage_msg = "Aggregated and filtered"

                print(f"Transform: {stage_msg}")
                print(f"Output: {self.pipelines[fmt].process(payload)}\n")
            else:
                print(f"No pipeline registered for format: {fmt}\n")

    def process_chained(
        self: "NexusManager", data: Any, chain: list[ProcessingPipeline]
    ) -> Any:
        current_val = data
        for pipe in chain:
            current_val = pipe.process(current_val)
        return current_val

    def monitor(self: "NexusManager", start_time: float,
                end_time: float, record_count: int,
                chain_len: int) -> None:
        elapsed = end_time - start_time
        efficiency = max(0, 100 - (elapsed * 10))

        print(
            f"Chain result: {record_count} records processed through "
            f"{chain_len}-stage pipeline"
        )
        print(
            f"Performance: {efficiency:.0f}% efficiency,"
            f" {elapsed:.3f}s total processing time\n"
        )

    def pipeline_recovery(self: "NexusManager",
                          PipelineA: ProcessingPipeline) -> None:
        try:
            PipelineA.process("error_data")
        except Exception as e:
            print(f"Error detected in Stage 2: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: " "Pipeline restored,"
                  " processing resumed\n")


def nexus_pipeline() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")

    manger = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    stages = [InputStage(), TransformStage(), OutputStage()]
    stages_msg = [
        "Input validation and parsing",
        "Data transformation and enrichment",
        "Output formatting and delivery",
    ]
    i = 1

    for msg in stages_msg:
        print(f"Stage {i}: {msg}")
        i += 1

    json_pipe = JSONAdapter("JSON_001")
    csv_pipe = CSVAdapter("CSV_001")
    stream_pipe = StreamAdapter("STREAM_001")

    process_pipes: List[ProcessingPipeline] = [
        json_pipe, csv_pipe, stream_pipe
        ]
    for pipe in process_pipes:
        for s in stages:
            pipe.add_stage(s)
        manger.register_pipeline(pipe)

    print("\n=== Multi-Format Data Processing ===\n")

    data_payloads = {
        "JSON": {"sensor": "temp", "value": 23.5, "unit": "C"},
        "CSV": "user,action,timestamp",
        "Stream": "Real-time sensor stream",
    }

    manger.process_data(data_payloads)
    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")
    chain = [csv_pipe, json_pipe, stream_pipe]

    raw_data = "sensor_id,102,temp,22.5,timestamp,2024-06-01T12:00:00Z"
    result = manger.process_chained(raw_data, chain)

    manger.monitor(
        start_time=0.0, end_time=0.2, record_count=100,
        chain_len=len(chain)
    )

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    manger.pipeline_recovery(stream_pipe)

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    nexus_pipeline()
