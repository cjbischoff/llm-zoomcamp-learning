import os

import dlt
import requests
from dotenv import load_dotenv

load_dotenv()

LOGFIRE_QUERY_URL = "https://logfire-us.pydantic.dev/v1/query"


def fetch_records():
    token = os.environ["LOGFIRE_READ_TOKEN"]
    r = requests.get(
        LOGFIRE_QUERY_URL,
        headers={"Authorization": f"Bearer {token}"},
        params={"sql": "SELECT * FROM records ORDER BY start_timestamp DESC LIMIT 1000"},
    )
    r.raise_for_status()
    data = r.json()

    columns = {c["name"]: c["values"] for c in data["columns"]}
    names = list(columns.keys())
    rows = [dict(zip(names, values)) for values in zip(*columns.values())]
    return rows


if __name__ == "__main__":
    rows = fetch_records()
    print(f"Fetched {len(rows)} spans")

    pipeline = dlt.pipeline(
        pipeline_name="logfire_traces",
        destination="duckdb",
        dataset_name="agent_traces",
    )
    load_info = pipeline.run(rows, table_name="records")
    print(load_info)
