from database.database import APIClient

db = APIClient()

class StudentService:

    @staticmethod
    def get_users():
        return db.get("student_table/")

    @staticmethod
    def get_users_cod(cod:str):

        try:
            return db.get(f"student_table/{cod}")
        except:
            return None
        
    @staticmethod
    def create_users(cod:str, name:str, can_reserv:str):

        if(StudentService.get_users_cod(cod) == None):

            payload = {"cod_student" : cod,
                       "name_student": name,
                       "can_reserv":can_reserv}

            return db.post("student_table/", payload)

        return f"El usuario de codigo {cod} ya existe"

    @staticmethod
    def delete_users(cod: str):
        user = StudentService.get_users_cod(cod)
        if user is None:
            return {"error": f"Usuario con código {cod} no encontrado"}

        db.delete(f"student_table/{cod}")

        return {"success": f"Usuario {cod} eliminado correctamente"}

    @staticmethod
    def update_users(cod: str, name: str, can_reserv: str):

        user = StudentService.get_users_cod(cod)
        if user is None:

            return {"error":f"Usuario con código {cod} no encontrado"}
        
        payload = {"cod_student" : cod,
                    "name_student": name,
                    "can_reserv":can_reserv}
        db.put(f"student_table/{cod}", payload)