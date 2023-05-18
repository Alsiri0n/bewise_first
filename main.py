import uvicorn

from app.web.app import setup_app

# store = None
#
#
# @lru_cache()
# def get_settings():
#     return Settings()
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     global store
#     store = setup_store(app)
#     yield
#     # Clean up the ML models and release the resources
#     store = None
#
#
# # app = FastAPI(lifespan=lifespan)
#
#
# async def request(url) -> list[Question | None]:
#     accessor = APIAccessor()
#     question = await accessor.get_data(url)
#     return question
#
#
# async def save_to_db(question: list[Question]) -> None:
#     pass
#
#
# async def get_data_from_external_api(qnt: int):
#     url = r"https://jservice.io/api/random?count=" + str(qnt)
#     data = await request(url)
#     if data:
#         print(data)
#         await save_to_db(data)


# @app.post("/request")
# async def qnt_questions(
#     background_tasks: BackgroundTasks,
#     settings: Annotated[Settings.Config, Depends(get_settings)],
#     ur: UserRequest = UserRequest,
# ) -> dict:
#     background_tasks.add_task(get_data_from_external_api, ur.questions_num)
#     print(settings)
#     return {"message": f"{ur.questions_num}"}


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(setup_app(), host="0.0.0.0", port=8000)
