from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    codigo:str
    nombre:str
    can_reserv:str