from fastapi import APIRouter, Depends
from pos_api.app import app
from pos_api.models.county import County

router = APIRouter(
    prefix="/api/county",
    tags=["county"],
    dependencies=[Depends(app.users.current_user(active=True))],
)

@router.get("/")
def list_counties():
    return [{
        "name": county.name,
        "TERYT": county.teryt,
    } for county in County.objects.all()]


@router.get("/{teryt}")
def get_county_name(teryt: str):
    return County.objects(teryt=teryt).get().name
