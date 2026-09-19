from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Question that the AI should answer"
    )


class QuestionResponse(BaseModel):
    question_id: str
    question: str
    status: str