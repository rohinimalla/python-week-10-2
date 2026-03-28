import pandas as pd
data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, 92, 78, 90],
    "Age": [20, 21, 19, 22]
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
print("\nSorted by Marks (Ascending):")
print(df.sort_values(by="Marks"))
print("\nSorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))
print("\nFirst 2 rows:")
print(df[:2])
print("\nUsing loc (label-based slicing):")
print(df.loc[0:2, ["Name", "Marks"]])
print("\nUsing iloc (index-based slicing):")
print(df.iloc[0:2, 0:2])

