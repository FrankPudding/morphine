from morphine import Dependency


class Factory[T](Dependency):
    def __call__(self) -> T:
        evaluated_kwargs = {}
        for key, value in self._constructor_kwargs.items():
            if isinstance(value, Dependency):
                evaluated_kwargs[key] = value()
                continue
            evaluated_kwargs[key] = value
        return self._dependency_class(
            *tuple(
                arg() if isinstance(arg, Dependency) else arg
                for arg in self._constructor_args
            ),
            **{
                key: value() if isinstance(value, Dependency) else value
                for key, value in self._constructor_kwargs.items()
            },
        )
