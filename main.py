import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apis.route import api_router
from core.config import settings
from db.session import engine
from db.base import Base
from middleware.middleware import RateLimitingMiddleware
from fastapi.testclient import TestClient


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.add_middleware(RateLimitingMiddleware)

# client = TestClient(app)


# def test_rate_limiting_middleware():
#     time.sleep(1)
#     response = client.get("/")
#     # Assert the response status code is 200
#     assert response.status_code == 200

#     time.sleep(1)
#     response = client.get("/")
#     # Assert the response status code is 200
#     assert response.status_code == 200

#     time.sleep(1)
#     response = client.get("/")
#     # Assert the response status code is 200
#     assert response.status_code == 200

#     time.sleep(1)
#     response = client.get("/")
#     # Assert the response status code is 200
#     assert response.status_code == 429


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
