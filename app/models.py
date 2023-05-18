from pydantic import BaseModel, validator
from datetime import datetime
from dataclasses import dataclass
from sqlalchemy import BigInteger, Column, Text, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


# Validation model for user request
class UserRequest(BaseModel):
    questions_num: int

    @validator("questions_num")
    def questions_num_as_positive_num(cls, questions_num):
        if questions_num < 1:
            raise ValueError("Must greater than 0")
        elif not isinstance(questions_num, int):
            raise ValueError("Must be positive integer")
        return questions_num


# Validation API response
class APICategory(BaseModel):
    id: int
    title: str
    created_at: str
    updated_at: str
    clues_count: int


# Validation API response
class APIResponse(BaseModel):
    id: int
    answer: str
    question: str
    value: int
    airdate: datetime
    created_at: datetime
    updated_at: datetime
    category_id: int
    game_id: int
    invalid_count: int | None
    category: APICategory

    def to_question(self) -> "QuestionModel":
        return QuestionModel(q_id=self.id, q_text=self.question,
                             a_text=self.answer, q_date=self.created_at.replace(tzinfo=None))


# Dataclass for API question
@dataclass
class Question:
    q_id: int
    q_text: str
    a_text: str
    q_date: datetime


# ORM Model for SQL
class QuestionModel(Base):
    __tablename__ = "questions"
    id = Column(BigInteger, primary_key=True, nullable=False)
    q_id = Column(BigInteger, nullable=False, unique=True)
    q_text = Column(Text, nullable=False)
    a_text = Column(Text, nullable=False)
    q_date = Column(DateTime, nullable=False)


    # Convert ORM result to dataclass
    def to_dc(self) -> Question:
        return Question(
            q_id=self.q_id,
            q_text=self.q_text,
            a_text=self.a_text,
            q_date=self.q_date,
        )
