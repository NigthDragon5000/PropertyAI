
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://admin:Aa123456@cluster0.n5xi3un.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Selecciona la base de datos y la colección
db = client["sample_mflix"]
movies = db["movies"]

# Extrae el primer registro
first_movie = movies.find_one()
print(first_movie)


# Nueva base de datos y colección

db = client["usuarios_db"]      # Crea o selecciona la base de datos
users = db["usuarios"]          # Crea o selecciona la colección (tabla)


usuario = {
    "correo": "jjcc5000@gmail.com",
    "password": "Aa123456"  # luego veremos cómo encriptarla 😉
}

users.insert_one(usuario)
print("Usuario guardado correctamente.")