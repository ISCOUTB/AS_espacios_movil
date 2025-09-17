from fastapi import APIRouter, HTTPException
from services.studentService import StudentService
from schemas.usuarioSchema import UsuarioSchema

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/obtener_usuarios")
def get_user():
    return StudentService.get_users()

@router.post("/create_user")
def create_user(cod:str, name:str, can_reserv:str):
    return StudentService.create_users(cod, name, can_reserv)

@router.delete("/delete_user/{cod}")
def delete_user(cod: str):
    result = StudentService.delete_users(cod)

    if "error" in result:
        # Devuelve error 404 si el usuario no existe
        raise HTTPException(status_code=404, detail=result["error"])

    return {"message": result["success"]}

@router.put("/update_user")
def update_user(cod: str, name: str, can_reserv: str):
    return StudentService.update_users(cod, name, can_reserv)