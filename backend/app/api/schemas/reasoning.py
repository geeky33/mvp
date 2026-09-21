from pydantic import BaseModel, Field


class InferenceRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Question to analyze",
    )

    num_consistency_samples: int = Field(
        default=5,
        ge=1,
        description="Number of samples used for consistency estimation",
    )


class ReasoningStepResponse(BaseModel):
    step_number: int
    step_text: str
    step_type: str

    verification_score: float | None = None
    consistency_score: float | None = None
    fused_confidence: float | None = None


class InferenceResponse(BaseModel):
    question: str
    reasoning: list[ReasoningStepResponse]
    predicted_error_step: int | None = None
    final_answer: str | None = None