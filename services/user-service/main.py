from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter(
    "user_service_requests_total",
    "Total number of requests"
)

@app.get("/health")
def health():
    return {"status": "UP"}

@app.get("/users")
def get_users():
    REQUEST_COUNT.inc()
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )

@app.get("/")
def root():
    return "Project 1 is Completed!!!"
