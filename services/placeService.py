from database.database import get_connection

def create_place(id_place: str):
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO espacio (id_place, disponible)
        VALUES (%s, TRUE)
    """, (id_place,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"success": True, "id_place": id_place}
