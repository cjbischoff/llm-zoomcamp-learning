import duckdb

con = duckdb.connect("logfire_traces.duckdb")

tables = con.execute(
    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'agent_traces'"
).fetchall()
print(f"Q2: {len(tables)} tables in agent_traces")

rows = con.execute("""
    SELECT attributes__gen_ai_usage_input_tokens
    FROM agent_traces.records
    WHERE span_name = 'chat gpt-5.4-mini'
""").fetchall()
total_input_tokens = sum(r[0] or 0 for r in rows)
print(f"Q3: total input tokens across {len(rows)} LLM calls = {total_input_tokens}")
