from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


class Hello(BaseModel):
    message: str


router = APIRouter()


@router.get("")
async def get_test():
    try:
        pass
    except:
        raise HTTPException(405, 'No Content')
    return {"message": "pong!"}


@router.post("")
async def post_test(hello: Hello):
    try:
        if hello.message == "Ahoy!":
            pass
        else:
            raise
    except:
        raise HTTPException(400, 'Please say Ahoy!')
    return {"message": "Yo-ho!"}