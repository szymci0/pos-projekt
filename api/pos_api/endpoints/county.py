from fastapi import APIRouter, Depends, HTTPException
from pos_api.app import app
from pos_api.models.county import County
from mongoengine.errors import DoesNotExist

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


@router.get("/name/{name}")
def get_county_teryt(name: str):
    counties = County.objects(name=name)
    if not len(counties):
        raise HTTPException(404, "County not found!")
    return [county.teryt for county in counties]
    
