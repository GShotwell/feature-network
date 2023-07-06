import inspect
import importlib
import pandas as pd
import igraph as ig


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


def get_dependencies(module_name):
    module = importlib.import_module(module_name)

    results = []

    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and hasattr(obj, "__wrapped__"):
            wrapped_func = obj.__wrapped__  # Get the original undecorated function
            defaults_df = get_default_values(wrapped_func)
            results.append(defaults_df)

    return pd.concat(results)


def get_dep_graph(module):
    edges = get_dependencies(module)
    return ig.Graph.TupleList(edges.itertuples(index=False), directed=True)


def plot_dependencies(module):
    g = get_dep_graph(module)
    ig.plot(g)


def parse_deps(feature, module, mode):
    g = get_dep_graph(module)
    paths = g.get_all_shortest_paths(feature, mode=mode)
    features = g.vs[i]["name"] for i in path[1:]
    return list(features)


def upstream_features(feature, module):
    return parse_deps(feature, module, mode="out")


def downstream_features(feature, module):
    return parse_deps(feature, module, "in")
