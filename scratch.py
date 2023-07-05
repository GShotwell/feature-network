from dependencies import get_default_values, find_named_arguments
from features import age_in_years, age
from pandas import DataFrame

df = DataFrame(
    {
        "name": ["Tom", "Dick", "Harry"],
        "age": [500, 1000, 3000],
        "city": ["New York", "Paris", "London"],
    }
)

print(find_named_arguments("features"))
df = find_named_arguments("features")
print(df.shape)
