from typing import Type, Any, Tuple, Dict


class Dependency[T]:
    _dependency_class: Type[T]
    _constructor_args: Tuple[Any, ...]
    _constructor_kwargs: Dict[str, Any]

    def __init__(self, dependency_class: Type[T], *args, **kwargs):
        self._dependency_class = dependency_class
        self._constructor_args = args
        self._constructor_kwargs = kwargs

    def override_dependencies(self, *args, **kwargs):
        self._constructor_args = args
        self._constructor_kwargs = kwargs
