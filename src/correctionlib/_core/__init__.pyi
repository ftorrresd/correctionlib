from typing import Dict, Iterator, List, Type, TypeVar, Union

import numpy

class Variable:
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def type(self) -> str: ...

class CompoundCorrection:
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def inputs(self) -> List[Variable]: ...
    @property
    def output(self) -> Variable: ...
    def evaluate(self, *args: Union[str, int, float]) -> float: ...
    def evalv(self, *args: Union[numpy.ndarray, str, int, float]) -> numpy.ndarray: ...

class Correction:
    @property
    def name(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def version(self) -> int: ...
    @property
    def inputs(self) -> List[Variable]: ...
    @property
    def output(self) -> Variable: ...
    def evaluate(self, *args: Union[str, int, float]) -> float: ...
    def evalv(self, *args: Union[numpy.ndarray, str, int, float]) -> numpy.ndarray: ...

T = TypeVar("T", bound="CorrectionSet")

class CorrectionSet:
    @classmethod
    def from_file(cls: Type[T], filename: str) -> T: ...
    @classmethod
    def from_string(cls: Type[T], data: str) -> T: ...
    @property
    def schema_version(self) -> int: ...
    def __getitem__(self, key: str) -> Correction: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    @property
    def compound(self) -> Dict[str, CompoundCorrection]: ...
