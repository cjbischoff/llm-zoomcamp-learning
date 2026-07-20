from opentelemetry import trace

from rag_helper import RAGBase

tracer = trace.get_tracer("llm-zoomcamp")


def calculate_cost(model, usage):
    cost = 0
    if "gpt-5.4-mini" in model:
        cost = (usage.input_tokens * 0.15 + usage.output_tokens * 0.60) / 1_000_000
    return cost


class RAGTraced(RAGBase):

    def rag(self, query):
        with tracer.start_as_current_span("rag"):
            return super().rag(query)

    def search(self, query, num_results=5):
        with tracer.start_as_current_span("search"):
            return super().search(query, num_results)

    def llm(self, prompt):
        with tracer.start_as_current_span("llm") as span:
            response = super().llm(prompt)
            usage = response.usage
            cost = calculate_cost(self.model, usage)
            span.set_attribute("input_tokens", usage.input_tokens)
            span.set_attribute("output_tokens", usage.output_tokens)
            span.set_attribute("cost", cost)
            return response
