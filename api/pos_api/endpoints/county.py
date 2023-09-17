from fastapi import (
    APIRouter, 
    Depends, 
    HTTPException, 
    Body, 
    UploadFile,
    File,
)
from pos_api.app import app
from pos_api.models.county import County
import io
import pandas as pd
from starlette.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from pos_pkg.data import DATA_SOURCE

router = APIRouter(
    prefix="/api/county",
    tags=["county"],
    dependencies=[Depends(app.users.current_user(active=True))],
)

users_filename =  "users_template.xlsx"


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


@router.get("/users/template")
def get_users_template():
    return FileResponse(
        DATA_SOURCE / users_filename,
        media_type="application/octet-stream",
        filename=users_filename,
    )


@router.post("/users/upload")
async def upload_users_file(file: UploadFile = File(...)):
    if file.content_type != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        raise HTTPException(status_code=400, detail="Only xlsx file available")
    xlsx = io.BytesIO(await file.read())
    df = pd.read_excel(xlsx)
    for row in df.iterrows():
        county = County.objects(name=row[1]["County"]).get()
        county.users = county.users + row[1]["Users"].split(',')
        county.save()
    