
# import pandas as pd

# data = {
#     "Class": ["A", "B", "A", "B", "C", "C"],
#     "Score": [85, 90, 88, 72, 95, 80],
#     "Age": [15, 16, 15, 17, 16, 15],
# }

# df = pd.DataFrame(data)
#
grouped = df.groupby("column_name")

for name, group in grouped:
    print(name)
    print(group)
    
grouped.mean()
grouped.sum()

df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column").agg({"numeric_column":["mean", "max", "min"]})

pivot = df.pivot_table(
    values="numeric_column",
    index="category_column",
    aggfunc="mean"
)

def range_func(x):
    return x.max() - x.min()

df.groupby("category_column")["numeric_column"].agg(range_func)

df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column")["numeric_column"].max()
df.groupby("category_column")["numeric_column"].min()

df.groupby("category_column").agg(
    {"numeric_column": ["mean", "max", "min"]}
)









