from functools import wraps


def feature(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        df = args[0]
        name = func.__name__
        if name in df.columns:
            return df[name]

        return func(df, **kwargs)

    return wrapper
