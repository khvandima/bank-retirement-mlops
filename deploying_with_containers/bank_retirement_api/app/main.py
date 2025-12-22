from typing import Any
from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from loguru import logger
from app.api import api_router
from app.config import settings, setup_app_logging


setup_app_logging(config=settings)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1_STR}/openapi.json',
)

root_router = APIRouter()


@root_router.get("/")
def index(request: Request) -> Any:
    body = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Bank Retirement API</title>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                    background: #f5f7fa;
                    margin: 0;
                    padding: 0;
                }

                .container {
                    max-width: 800px;
                    margin: 80px auto;
                    background: #ffffff;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
                }

                h1 {
                    margin-top: 0;
                    color: #1f2933;
                    test-align: center;
                }

                p {
                    color: #4a5568;
                    line-height: 1.6;
                }

                .links {
                    margin-top: 30px;
                    display: flex;
                    justify-content: center;
                    gap: 16px;
                }

                a.button {
                    display: inline-block;
                    margin-right: 15px;
                    padding: 12px 20px;
                    background: #2563eb;
                    color: white;
                    text-decoration: none;
                    border-radius: 6px;
                    font-weight: 500;
                }

                .button.health {
                    background-color: #22c55e;
                    color: white;
                }
                
                .button.health:hover {
                    background-color: #16a34a;
                }

                a.button:hover {
                    opacity: 0.9;
                }

                footer {
                    margin-top: 40px;
                    font-size: 0.9em;
                    color: #9ca3af;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🏦 Bank Retirement Prediction API</h1>

                <p>
                    This API provides predictions for bank retirement outcomes using
                    a trained machine learning model.
                </p>

                <p>
                    It is designed as a production-ready service with validation,
                    testing and reproducible inference.
                </p>

                <div class="links">
                    <a href="/docs" class="button">Open API Docs</a>
                    <a href="/api/v1/health" class="button health">Health Check</a>
                </div>

                <footer>
                    <p>Powered by FastAPI • Deployed on Railway</p>
                </footer>
            </div>
        </body>
        </html>
        """

    return HTMLResponse(content=body)


app.include_router(api_router, prefix=settings.API_V1_STR)

app.include_router(root_router)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

if __name__ == '__main__':
    logger.warning('Running in development mode. Do not run like this in production.')

    import uvicorn
    uvicorn.run(app, host='localhost', port=8001, log_level='debug')
