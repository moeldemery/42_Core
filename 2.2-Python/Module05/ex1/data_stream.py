#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self: object, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self: object, data_batch: List[Any]) -> str:
        pass

    def filter_data(self: object, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return [item for item in data_batch]

    def get_stats(self: "DataStream") -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id,
            "processed": self.processed_count
        }


class SensorStream(DataStream):

    def __init__(self: "SensorStream", stream_id: str) -> None:
        super().__init__(stream_id)
        self.sensor_type = "Environmental Data"
        self.name_category = "Sensor"

    def process_batch(self: "SensorStream", data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)
            temps = [float(s.split(":")[1])
                     for s in data_batch if "temp" in str(s)]
            avg = sum(temps) / len(temps) if temps else 0.0
            return (f"Sensor analysis: {len(data_batch)} readings processed," +
                   f" avg temp: {avg:.1f}°C")
        except Exception as e:
            return f"Sensor Error: {e}"

    def filter_data(self: "SensorStream", data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high_priority":
            return [d for d in data_batch if "error" in str(d).lower()
                    or "critical" in str(d).lower()]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self: "TransactionStream", stream_id: str) -> None:
        super().__init__(stream_id)
        self.sensor_type = "Financial Data"
        self.name_category = "Transaction"

    def process_batch(self: "TransactionStream", data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)
            net_flow = 0
            for op in data_batch:
                if ":" in str(op):
                    action, val = str(op).split(":")
                    net_flow += int(val) if action == "buy" else -int(val)
            if net_flow > 0:
                return (f"Transaction stream processed {len(data_batch)} " +
                    f"operations, net flow: +{net_flow} units")
            return (f"Transaction stream processed {len(data_batch)} " +
                f"operations, net flow: {net_flow} units")
        except Exception as e:
            return f"Transaction Error: {e}"

    def filter_data(self: "TransactionStream", data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high_priority":
            return [d for d in data_batch if int(str(d).split(":")[1]) >= 500]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self: "EventStream", stream_id: str) -> None:
        super().__init__(stream_id)
        self.sensor_type = "Event Data"
        self.name_category = "Event"

    def process_batch(self: "EventStream", data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        error_cnt = 0
        for event in data_batch:
            if "error" in str(event).lower():
                error_cnt += 1
        return (f"Event analysis: {len(data_batch)} events," +
            f" {error_cnt} error(s) detected")


class StreamProcessor:
    def __init__(self: "StreamProcessor") -> None:
        self.streams: List[DataStream] = []

    def add_stream(self: "StreamProcessor", stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self: "StreamProcessor", mixed_data: List[Any],
                    criteria: Optional[str] = None) -> None:
        for i in range(len(self.streams)):
            stream = self.streams[i]
            batch = mixed_data[i]

            if isinstance(stream, SensorStream):
                prefix = "- Sensor data"
                unit = "readings"
            elif isinstance(stream, TransactionStream):
                prefix = "- Transaction data"
                unit = "operations"
            else:
                prefix = "- Event data"
                unit = "events"

            stream.process_batch(batch)
            print(f"{prefix}: {len(batch)} {unit} processed")

    def filter_all(self: "StreamProcessor", batches: List[List[Any]],
                   criteria: str) -> List[List[Any]]:
        return [self.streams[i].filter_data(batches[i], criteria)
                for i in range(len(self.streams))]


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    s_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    t_batch = ["buy:100", "sell:150", "buy:75"]
    e_batch = ["login", "error", "logout"]

    sensor = SensorStream("SENSOR_001")
    print(f"Initializing {sensor.name_category} Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.sensor_type}")
    print(f"Processing sensor batch: {s_batch}")
    """print(f"Processing sensor batch: [{', '.join(s_batch)}]")"""
    analysis_s = sensor.process_batch(s_batch)
    print(analysis_s, "\n")

    transaction = TransactionStream("TRANS_001")
    print(f"Initializing {transaction.name_category} Stream...")
    print(f"Stream ID: {transaction.stream_id},"
          f"Type: {transaction.sensor_type}")
    print(f"Processing transaction batch: {t_batch}")
    """print(f"Processing sensor batch: [{', '.join(t_batch)}]")"""
    analysis_t = transaction.process_batch(t_batch)
    print(analysis_t, "\n")

    event = EventStream("EVENT_001")
    print(f"Initializing {event.name_category} Stream...")
    print(f"Stream ID: {event.stream_id}, Type: {event.sensor_type}")
    print(f"Processing transaction batch: {e_batch}")
    """print(f"Processing sensor batch: [{', '.join(e_batch)}]")"""
    analysis_e = event.process_batch(e_batch)
    print(analysis_e, "\n")

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))

    mixed_batches = [
        ["temp:20", "temp:24"],
        ["buy:10", "sell:50", "buy:20", "sell:100"],
        ["login", "error", "logout"]
    ]

    processor.process_all(mixed_batches)

    print("\nStream filtering active: High-priority data only")

    filter_data = [
        ["temp:45:critical", "temp:50:critical", "temp:20"],
        ["sell:500", "buy:125"],
        ["login", "error"]
    ]
    filtered_results = processor.filter_all(filter_data, "high_priority")

    print(f"Filtered results: {len(filtered_results[0])} critical sensor "
          f"alerts, {len(filtered_results[1])} large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
