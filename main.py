from typing import Union
from fastapi import FastAPI
import json
from db_example import registros # Se importa la variable "registros" del archivo db_example

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print(registros) # la variable registros la usamos acá como queremos

    result = []
    for index, fila in enumerate(registros):
        result.append({'id': fila[0], 'name': fila[1], 'age': fila[2]})
    
    mi_json = json.loads(json.dumps(result))
        
    print(type(mi_json))

    return mi_json