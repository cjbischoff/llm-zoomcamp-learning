import time

from rag_helper import RAGBase


def llm_structured(client, instructions, user_prompt, schema, model="gpt-5.4-mini"):
    messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": user_prompt},
    ]

    response = client.responses.parse(
        model=model,
        input=messages,
        text_format=schema,
    )

    return response.output_parsed, response.usage


def llm_structured_retry(client, instructions, user_prompt, schema, model="gpt-5.4-mini", retries=5, delay=5):
    for attempt in range(retries):
        try:
            return llm_structured(client, instructions, user_prompt, schema, model=model)
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(delay * (attempt + 1))


PRICES = {
    "gpt-5.4-mini": {"input": 0.75 / 1_000_000, "output": 4.50 / 1_000_000},
}


def calc_price(usage, model="gpt-5.4-mini"):
    price = PRICES[model]

    input_cost = usage.input_tokens * price["input"]
    output_cost = usage.output_tokens * price["output"]

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": input_cost + output_cost,
    }


def calc_total_price(usages, model="gpt-5.4-mini"):
    total = 0.0

    for usage in usages:
        total += calc_price(usage, model=model)["total_cost"]

    return total


class RAGWithUsage(RAGBase):
    """RAGBase with the tuned search boosts, tracking token usage per call."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usages = []

    def search(self, query, num_results=5):
        boost_dict = {"question": 1.0, "answer": 2.0, "section": 0.1}
        filter_dict = {"course": self.course}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict=filter_dict,
        )

    def llm(self, prompt, retries=5, delay=5):
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt},
        ]

        for attempt in range(retries):
            try:
                response = self.llm_client.responses.create(
                    model=self.model,
                    input=input_messages,
                )
                self.usages.append(response.usage)
                return response.output_text
            except Exception:
                if attempt == retries - 1:
                    raise
                time.sleep(delay * (attempt + 1))

    def total_cost(self):
        return calc_total_price(self.usages, model=self.model)

    def reset_usage(self):
        self.usages = []


def map_progress(pool, items, function):
    from tqdm.auto import tqdm

    futures = [pool.submit(function, item) for item in items]

    results = []
    for future in tqdm(futures):
        results.append(future.result())

    return results
