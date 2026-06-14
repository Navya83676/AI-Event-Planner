from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from routes.event_routes import router

from utils.pdf_generator import generate_pdf

from database import engine

from models.event_model import Base

# =========================
# DATABASE
# =========================

Base.metadata.create_all(
    bind=engine
)

# =========================
# FASTAPI APP
# =========================

app = FastAPI(

    title=
        "AI Event Planner API",

    version=
        "1.0.0",

    description=
        "Multi-Agent AI Event Planning System"
)

# =========================
# CORS
# =========================

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "https://ai-event-planner-1.onrender.com",
        "http://localhost:5173"
    ],

    allow_credentials=False,

    allow_methods=["*"],

    allow_headers=["*"],
)

# =========================
# ROUTES
# =========================

app.include_router(
    router
)

# =========================
# ROOT ROUTE
# =========================

@app.get("/")
async def root():

    return {

        "message":
            "AI Event Planner Backend Running",

        "status":
            "healthy"
    }

@app.get("/health")
def health():

    return {
        "status": "ok"
    }
