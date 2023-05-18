from fastapi import APIRouter, Depends
from pydantic import BaseModel
from pos_api.app import app
from pos_api.models.position import Position

router = APIRouter(
    prefix="/api/position",
    tags=["position"],
    dependencies=[Depends(app.users.current_user(active=True))],
)

@router.get("/")
def list_positions():
    return [{
        "email": pos.email,
        "x": pos.x,
        "y": pos.y
    } for pos in Position.objects.all()] 


