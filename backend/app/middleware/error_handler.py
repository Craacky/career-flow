from fastapi import FastAPI
from starlette.responses import JSONResponse


def setup_error_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def global_exception_handler(request, exc):
        return JSONResponse(status_code=500,
                            content={"detail": str(exc)})
