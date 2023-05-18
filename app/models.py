from pydantic import BaseModel, validator


class UserRequest(BaseModel):
    questions_num: int

    @validator("questions_num")
    def questions_num_as_positive_num(cls, questions_num):
        if questions_num < 1:
            raise ValueError("Must greater than 0")
        elif not isinstance(questions_num, int):
            raise ValueError("Must be positive integer")
        return questions_num
