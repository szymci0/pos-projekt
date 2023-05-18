from fastapi import APIRouter, Depends
from pos_api.app import app
from pos_api.models.position import Position

router = APIRouter(
    prefix="/api/position",
    tags=["position"],
    dependencies=[Depends(app.users.current_user(active=True))],
)

@router.get("/")
def list_positions():
    return list(Position.objects())

