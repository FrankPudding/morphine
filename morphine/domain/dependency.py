from typing import Any, Dict, Protocol, Self, Tuple, Type, runtime_checkable


@runtime_checkable
class Dependency[T](Protocol):
    _dependency_class: Type[T]
    _constructor_args: Tuple[Any, ...]
    _constructor_kwargs: Dict[str, Any]

    def __init__(self, dependency_class: Type[T], *args, **kwargs):
        self._dependency_class = dependency_class
        self._constructor_args = args
        self._constructor_kwargs = kwargs

    def __call__(self, *args, **kwargs): ...

    def override(self, dependency: Self):
        self._dependency_class = dependency._dependency_class
        self._constructor_args = dependency._constructor_args
        self._constructor_kwargs = dependency._constructor_kwargs

    def override_dependencies(self, *args, **kwargs):
        self._constructor_args = args
        self._constructor_kwargs = kwargs
