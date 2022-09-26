import fastapi
import uvicorn

print("Hello fastapi")

api = fastapi.FastAPI()
#Use Alt-Enter for context help
#api = FastAPI()

@api.get("/")
def index():
    return {"msg": "Hello from FastAPI",
            "another msg": ["Hello", "World"]}

uvicorn.run(api)