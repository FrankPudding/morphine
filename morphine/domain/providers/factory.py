from morphine import Provider


class Factory[T](Provider):
    """
    Provides a new instance with each call
    """
    def __call__(self) -> T:
        evaluated_kwargs = {}
        for key, value in self._constructor_kwargs.items():
            if isinstance(value, Provider):
                evaluated_kwargs[key] = value()
                continue
            evaluated_kwargs[key] = value
        return self._instance_type(
            *tuple(
                arg() if isinstance(arg, Provider) else arg
                for arg in self._constructor_args
            ),
            **{
                key: value() if isinstance(value, Provider) else value
                for key, value in self._constructor_kwargs.items()
            },
        )
