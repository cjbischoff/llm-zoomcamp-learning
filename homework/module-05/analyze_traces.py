import pandas as pd
import sqlite3

conn = sqlite3.connect("traces.db")
df = pd.read_sql("SELECT * FROM spans", conn)
conn.close()

print("Q4: span names present:", sorted(df["name"].unique()))

df["duration_ns"] = df["end_time"] - df["start_time"]

print("\nQ5: total duration by span name (excluding rag):")
totals = df[df["name"] != "rag"].groupby("name")["duration_ns"].sum() / 1e6
print(totals, "ms")

print("\nQ6: input_tokens per llm span:")
tokens = df[df["name"] == "llm"]["input_tokens"].dropna()
print(tokens.tolist())
print(f"min={tokens.min()} max={tokens.max()} spread={(tokens.max() - tokens.min()) / tokens.min():.1%}")
