from fastapi import status, FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import redis

# --- Config ---
API_KEY = "demo123"  # Use env vars in production
API_KEY_NAME = "X-API-Key"
r = redis.Redis(host="redis", port=6379, decode_responses=True)

# --- Models ---
model_registry = {"gpt2": "text-generation", "summarizer": "summarization"}

app = FastAPI()


class InferenceRequest(BaseModel):
    model_id: str
    input_text: str


# Simulate Security
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API Key"
        )
    return api_key


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/deploy")
def deploy_model(model_id: str, api_key: str = Depends(validate_api_key)):
    print("Hello ", api_key)
    if model_id not in model_registry:
        raise HTTPException(status_code=404, detail="Model not supported")
    r.set(f"model:{model_id}", "loaded")  # Simulate deployment
    return {"status": f"Model {model_id} deployed"}


@app.post("/predict")
def predict(request: InferenceRequest):
    if not r.exists(f"model:{request.model_id}"):
        raise HTTPException(status_code=404, detail="Model not deployed")
    # Simulate inference (replace with actual Hugging Face call)
    return {"output": f"Result for '{request.input_text}' using {request.model_id}"}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
