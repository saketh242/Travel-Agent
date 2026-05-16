from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

import backend.config  # noqa: F401 — load env before planner

ROOT_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = ROOT_DIR / "frontend"

app = FastAPI(title="Travel Planner", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if FRONTEND_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


class PlanRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=2000)


class PlanResponse(BaseModel):
    plan: str


@app.get("/")
async def index():
    index_file = FRONTEND_DIR / "index.html"
    if not index_file.is_file():
        raise HTTPException(status_code=404, detail="Frontend not found")
    return FileResponse(index_file)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/api/plan", response_model=PlanResponse)
async def create_plan(body: PlanRequest):
    query = body.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        from backend.ai_logic import travel_planner

        plan = travel_planner(query)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Failed to generate travel plan. Check server logs.",
        ) from exc

    return PlanResponse(plan=plan)
