from fastapi import APIRouter, Depends, HTTPException, Body
from pos_api.app import app
from pos_api.models.county import County
from mongoengine.errors import DoesNotExist
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/api/county",
    tags=["county"],
    dependencies=[Depends(app.users.current_user(active=True))],
)


class CountyPayload(BaseModel):
    name: Optional[str]
    teryt: Optional[str]
    user: Optional[str]


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
    name = " ".join(part.capitalize() for part in name.split(" "))
    counties = County.objects(name=name)
    if not len(counties):
        raise HTTPException(404, "County not found!")
    return [county.teryt for county in counties]


@router.patch("/users/add")
def add_user_to_county(payload: CountyPayload = Body(...)):
    county=County.objects(teryt=payload.teryt).get()
    if payload.user not in county.users:
        county.users.append(payload.user)
    county.save()

@router.get("/users/list")
def get_counties_users():
    counties = County.objects()
    return [
         {
            "county": county.name, 
            "users": county.users
         } for county in counties if len(county.users)
    ]
