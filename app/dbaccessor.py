from .models import Question, QuestionModel
from sqlalchemy import select, desc
from sqlalchemy.engine import Result
from .database import db


# Helper for work with DB and keeping query for db
class DBAccessor:
    async def add_question(self, q: list[Question]) -> None:
        async with db.session() as session:
            async with session.begin():
                session.add_all(q)
        await session.commit()

    async def get_questions(self, qnt: int) -> list[Question]:
        async with db.session() as session:
            query = select(QuestionModel).order_by(desc(QuestionModel.id)).limit(qnt)
            result: Result = await session.execute(query)
        q_model = result.scalars().all()
        if q_model:
            return [question.to_dc() for question in q_model]

    async def exist_question_by_id(self, id_: int) -> bool:
        result = False
        async with db.session() as session:
            query = select(QuestionModel.id).where(QuestionModel.q_id == id_)
            query_result: Result = await session.execute(query)
        q_result = query_result.scalar()
        if q_result:
            result = True
        return result
