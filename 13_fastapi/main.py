from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class HelloResp(BaseModel):
    msg: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    code: str
    tax: float | None = None


app = FastAPI()


item_list = []


class Counter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1


counter = Counter()


@app.get("/")
async def root():
    counter.increment()
    return {"message": "Hello World"}


@app.get("/hello/{name}", response_model=HelloResp)
async def hello_name(name: str):
    counter.increment()
    return HelloResp(msg=f"Hello {name}")


@app.get("/counter")
async def get_counter():
    counter.increment()
    return {"counter": counter.counter}


@app.post("/items/")
async def create_item(item: Item):
    item_list.append(item)
    return item


@app.get("/items/")
async def get_items():
    return item_list


@app.get("/items/{name}")
async def get_items(name: str):
    for item in item_list:
        if item.name == name:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
