from fastapi import APIRouter, BackgroundTasks

from .models import UserRequest, APIResponse
from .config import Settings
from .apiaccessor import APIAccessor

api = APIRouter()


async def request(url) -> list[APIResponse | None]:
    accessor = APIAccessor()
    question = await accessor.get_data(url)
    if question:
        return question


async def save_to_db(question: list[APIResponse]) -> None:
    for q in question:
        print(q)


async def get_data_from_external_api(qnt: int) -> None:
    url = r"https://jservice.io/api/random?count=" + str(qnt)
    data = await request(url)
    if data:
        await save_to_db(data)


@api.post("/request")
async def qnt_questions(
    background_tasks: BackgroundTasks, ur: UserRequest = UserRequest
) -> dict:
    # background_tasks.add_task(get_data_from_external_api, ur.questions_num)
    await get_data_from_external_api(ur.questions_num)
    return {"message": f"{ur.questions_num}"}
