import inspect
import importlib
import pandas as pd


def get_default_values(func):
    signature = inspect.signature(func)
    parameters = signature.parameters
    default_values = {}

    for param_name, param in parameters.items():
        if param.default != inspect.Parameter.empty:
            default_values[param_name] = param.default

    output = {
        "feature": func.__name__,
        "dependency": default_values.keys(),
    }

    return pd.DataFrame(output)


def find_named_arguments(module_name):
    module = importlib.import_module(module_name)

    results = []

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and hasattr(obj, "__wrapped__"):
            wrapped_func = obj.__wrapped__  # Get the original undecorated function
            defaults_df = get_default_values(wrapped_func)
            results.append(defaults_df)

    return pd.concat(results)
