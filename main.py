from datasets import load_dataset
import pandas as pd

ds = load_dataset("sharjeelyunus/github-issues-dataset", split="train")
df = ds.to_pandas()[["title","body","labels","severity"]]

df["description"] = df["body"].fillna("")
df["label_type"] = df["labels"].apply(lambda x: x[0] if x else "bug")
df = df[["title","description","label_type","severity"]]
print(df.head())
