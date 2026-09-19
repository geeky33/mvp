from fastapi import APIRouter

from app.api.schemas.reasoning import (
    InferenceRequest,
    InferenceResponse,
    ReasoningStepResponse,
)

from app.core.config import settings

from app.services.consistency_service import (
    consistency_score,
)

from app.services.fusion_service import (
    fuse_confidence,
    predict_error_step,
)

from app.services.llm_service import (
    LLMService,
)

from app.services.reasoning_service import (
    decompose_reasoning,
)

from app.services.verification_service import (
    verify_step,
)


router = APIRouter(
    prefix="/inference",
    tags=["inference"],
)


@router.post(
    "",
    response_model=InferenceResponse,
)
def run_inference(
    payload: InferenceRequest,
):

    llm = LLMService(
        provider=settings.llm_provider,
        model=settings.llm_model,
    )

    generated = llm.generate_reasoning(
        payload.question
    )

    steps = decompose_reasoning(
        generated.text
    )

    results: list[
        ReasoningStepResponse
    ] = []

    for step in steps:

        verification = verify_step(
            payload.question,
            step.text,
        )

        # Development placeholder.
        # Later this becomes K actual LLM generations
        # conditioned on the same reasoning prefix.

        samples = [
            step.text
            for _ in range(
                payload.num_consistency_samples
            )
        ]

        consistency = consistency_score(
            samples
        )

        fused = fuse_confidence(
            verification,
            consistency,
        )

        results.append(
            ReasoningStepResponse(
                step_number=step.step_number,
                step_text=step.text,
                step_type=step.step_type,
                verification_score=verification,
                consistency_score=consistency,
                fused_confidence=fused,
            )
        )

    confidence_map = {
        item.step_number: item.fused_confidence
        for item in results
        if item.fused_confidence is not None
    }

    predicted_error = predict_error_step(
        confidence_map
    )

    return InferenceResponse(
        question=payload.question,
        reasoning=results,
        predicted_error_step=predicted_error,
        final_answer=generated.final_answer,
    )