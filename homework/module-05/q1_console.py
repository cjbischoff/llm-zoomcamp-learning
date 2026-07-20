from dotenv import load_dotenv

load_dotenv()

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)

from traced_rag import RAGTraced
from starter import index, client

rag = RAGTraced(index=index, llm_client=client)

query = "How does the agentic loop keep calling the model until it stops?"
answer = rag.rag(query)
print("ANSWER:", answer)
