from fastapi import APIRouter
from .models import UserRequest

api = APIRouter()


@api.post("/request")
async def qnt_questions(ur: UserRequest = UserRequest) -> dict:
    return {"message": f"{ur.questions_num}"}