from morphine import Dependency


class Factory[T](Dependency):
    def __call__(self) -> T:
        return self._dependency_class(*self._constructor_args, **self._constructor_kwargs)
