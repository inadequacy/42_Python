#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Tuple, Protocol


# code from ex0
class DataProcessor(ABC):
    def __init__(self) -> None:
        self.new_data: list[str] = []
        self.active: bool = False
        self.total_processed = 0
        self.current_index = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self, nb: int) -> list[Tuple[int, str]]:
        result = []
        count = min(nb, len(self.new_data))

        for _ in range(count):
            value = self.new_data.pop(0)
            self.current_index += 1
            result.append((self.current_index, value))
        return result

    def stats(self) -> str:
        return f"total {self.total_processed} items processed, " \
               f"remaining {len(self.new_data)} on processor"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for x in data:
                    self.new_data.append(str(x))
                    self.total_processed += 1
            else:
                self.new_data.append(str(data))
                self.total_processed += 1
        else:
            raise ValueError("Invalid data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for x in data:
                    self.new_data.append(x)
                    self.total_processed += 1
            else:
                self.new_data.append(data)
                self.total_processed += 1
        else:
            raise ValueError("Invalid data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return True
        elif isinstance(data, list):
            return all(isinstance(x, dict) for x in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for x in data:
                    self.new_data.append(
                        f"{str(x.get('log_level'))}:"
                        f"{str(x.get('log_message'))}")
                    self.total_processed += 1
            else:
                self.new_data.append(str(data))
                self.total_processed += 1
        else:
            raise ValueError("Invalid data")


# code from ex2
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExport(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        content = [value for _, value in data]
        print("CSV output:")
        print(",".join(content))
        with open("file.csv", "a") as file:
            file.write(",".join(content))


class JSONExport(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        content = []
        print("JSON output:")
        for index, value in data:
            content.append(f'"item_{index}": "{value}"')
        print("{" + ", ".join(content) + "}")
        with open("file.json", "a") as file:
            file.write("{" + ", ".join(content) + "}")


# code from ex1
class DataStream:
    def __init__(self):
        self.active_processor = []

    def register_processor(self, proc: DataProcessor) -> None:
        proc.active = True
        self.active_processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for x in stream:
            handled = False
            for proc in self.active_processor:
                if proc.validate(x):
                    proc.ingest(x)
                    handled = True
                    break
            if not handled:
                print("DataStream error - "
                      f"Can't process element in stream: {x}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.active_processor:
            print("No processors and no data")
            return

        for proc in self.active_processor:
            name = proc.__class__.__name__
            print(f"{name}: {proc.stats()}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.active_processor:
            data = processor.output(nb)
            if data:
                plugin.process_output(data)


def function() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message":
             "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExport())
    ds.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE", "log_message":
             "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExport())
    ds.print_processors_stats()


if __name__ == "__main__":
    function()
