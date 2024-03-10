from typing import Optional

from morphine import Provider


class Singleton[T](Provider):
    """Provides the same instance on each call."""
    _instance: Optional[T] = None

    def __call__(self) -> T:
        if self._instance is not None:
            return self._instance
        self._instance = self._instance_type(self._constructor_args, self._constructor_kwargs)
        return self._instance

    def reset(self) -> None:
        self._instance = None
