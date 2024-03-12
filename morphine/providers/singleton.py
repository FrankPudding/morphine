from typing import Optional

from morphine.provider import Provider


class Singleton[T](Provider):
    """Provides the same instance on each call."""
    _instance: Optional[T] = None

    def __call__(self) -> T:
        if self._instance is not None:
            return self._instance
        evaluated_kwargs = {}
        for key, value in self._constructor_kwargs.items():
            if isinstance(value, Provider):
                evaluated_kwargs[key] = value()
                continue
            evaluated_kwargs[key] = value
        self._instance = self._instance_type(
            *tuple(
                arg() if isinstance(arg, Provider) else arg
                for arg in self._constructor_args
            ),
            **{
                key: value() if isinstance(value, Provider) else value
                for key, value in self._constructor_kwargs.items()
            },
        )
        return self._instance

    def reset(self) -> None:
        self._instance = None
