from typing import Union
from fastapi import FastAPI
from db_example import registros # Se importa la variable "registros" del archivo db_example

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print(registros) # la variable registros la usamos acá como queremos

    # TO DO:
        # "registros" es una lista de tuples y hay que convertirlo a JSON

    return {"item_id": item_id, "q": q}