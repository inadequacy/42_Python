#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.new_data: List[str] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self.new_data:
            raise Exception("No data available")
        value = self.new_data.pop(0)
        return 0, value

# corrected gotta do other two
class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, List):
            return all(isinstance(x, (int, float)) for x in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, List):
                for x in data:
                    self.new_data.append(str(x))
            else:
                self.new_data.append(str(data))
        else:
            raise Exception("Invalid data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, List):
            return all(isinstance(x, str) for x in data)
        else:
            return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, List):
                for x in data:
                    self.new_data.append(x)
            else:
                self.new_data.append(data)
        else:
            raise Exception("Invalid data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (dict, List[dict])):
            return True
        else:
            return False

    def ingest(self, data: Any) -> None:
        if isinstance(data, ({str: str}, List[str: str])):
            self.new_data = str(data)
        else:
            raise Exception("Invalid data")


def function() -> None:
    print("=== Code Nexus - Data Processor ===")

    # Numeric
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # type: ignore (intentional)
    except Exception as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for i in range(3):
        idx, val = np.output()
        print(f"Numeric value {i}: {val}")

    # Text
    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")

    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    idx, val = tp.output()
    print(f"Text value {idx}: {val}")

    # Log
    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")

    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]

    print(f"Processing data: {logs}")
    lp.ingest(logs)

    print("Extracting 2 values...")
    for i in range(2):
        idx, val = lp.output()
        print(f"Log entry {i}: {val}")


if __name__ == "__main__":
    function()
