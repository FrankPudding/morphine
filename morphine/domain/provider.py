from typing import Any, Dict, Protocol, Self, Tuple, Type, runtime_checkable


@runtime_checkable
class Provider[T](Protocol):
    _instance_type: Type[T]
    _constructor_args: Tuple[Any, ...]
    _constructor_kwargs: Dict[str, Any]

    def __init__(self, instance_type: Type[T], *args, **kwargs):
        self._instance_type = instance_type
        self._constructor_args = args
        self._constructor_kwargs = kwargs

    def __call__(self, *args, **kwargs): ...

    def override(self, dependency: Self):
        self._instance_type = dependency._instance_type
        self._constructor_args = dependency._constructor_args
        self._constructor_kwargs = dependency._constructor_kwargs

    def override_dependencies(self, *args, **kwargs):
        self._constructor_args = args
        self._constructor_kwargs = kwargs
