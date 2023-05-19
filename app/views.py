from fastapi import APIRouter

from .apiaccessor import APIAccessor
from .dbaccessor import DBAccessor
from .models import UserRequest, APIResponse

api = APIRouter()


# Request to external API
async def request(url) -> list[APIResponse | None]:
    accessor = APIAccessor()
    question = await accessor.get_data(url)
    if question:
        return question


# Saving question to DB
async def save_to_db(question: list[APIResponse], db_accessor: DBAccessor) -> None:
    q = [q.to_question() for q in question]
    await db_accessor.add_question(q)


# Get and validate data from external API
async def get_data_from_external_api(qnt: int, db_accessor: DBAccessor):
    url = r"https://jservice.io/api/random?count=" + str(qnt)
    api_response = await request(url)
    clear_questions, i = [], 0
    # Check unique value at db
    while len(clear_questions) != qnt:
        exists: bool = await db_accessor.exist_question_by_id(api_response[i].id)
        if not exists:
            clear_questions.append(api_response[i])
            i += 1
        else:
            url = r"https://jservice.io/api/random?count=1"
            api_response = await request(url)

    if clear_questions:
        await save_to_db(clear_questions, db_accessor)


# User request to internal API
@api.post("/request")
async def qnt_questions(ur: UserRequest = UserRequest) -> list:
    db_accessor = DBAccessor()
    await get_data_from_external_api(ur.questions_num, db_accessor)
    questions = await db_accessor.get_questions(ur.questions_num)
    return [q for q in questions]
