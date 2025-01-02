import uvicorn
from fastapi import APIRouter, FastAPI

from app.src.core.config import get_settings

settings = get_settings()

api_router = APIRouter(prefix=settings.API_V1_STR)


app = FastAPI(
    debug=settings.DEBUG,
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
)

app.include_router(api_router)


@app.get("/")
def health():
    return {"message": "Ok"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)
