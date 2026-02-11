from fastapi import FastAPI, Depends
from app.api.v1.routers.auth import router as auth_router
from app.api.v1.routers.admin import router as admin_router
from fastapi.middleware.cors import CORSMiddleware
from app.utils.helper_functions import admin_check

app = FastAPI(
    title="Civic issue backend",
    version="1.0.0",
    description="Backend API for civic issue reporting system"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(admin_router, prefix="/api/v1/admin", tags=["Admin"])


@app.get("/")
def health_check():
    return {"status": "Backend is running"}