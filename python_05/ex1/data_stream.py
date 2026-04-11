#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Tuple, typing

## code from ex0
class DataProcessor(ABC):
    def __init__(self) -> None:
        self.new_data: list[str] = []

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
            else:
                self.new_data.append(str(data))
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
            else:
                self.new_data.append(data)
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
                    self.new_data.append(str(x))
            else:
                self.new_data.append(str(data))
        else:
            raise ValueError("Invalid data")

## code from ex1
class DataStream():
    def register_processor(self, proc: DataProcessor) -> None:
        pass
    def process_stream(self, stream: list[typing.Any]) -> None:
        pass
    def print_processors_stats(self) -> None:
        pass


def function() -> None:
    pass


if __name__ == "__main__":
    function()
