from fastapi import APIRouter
from services.placeService import create_place

router = APIRouter(prefix="/places", tags=["Places"])

@router.post("/create")
def create_place_route(id_espacio: str):
    return create_place(id_espacio)
