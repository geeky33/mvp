from dataclasses import dataclass


@dataclass
class LLMResponse:
    text: str
    final_answer: str | None = None


class LLMService:
    """
    Provider-neutral interface.

    The mock implementation allows us to test the complete
    backend before connecting a real LLM API.
    """

    def __init__(
        self,
        provider: str = "mock",
        model: str = "mock-model",
    ):
        self.provider = provider
        self.model = model

    def generate_reasoning(
        self,
        question: str,
    ) -> LLMResponse:

        return LLMResponse(
            text=(
                "Step 1: Identify the quantities and operations needed.\n"
                "Step 2: Perform the calculation using the information in the question.\n"
                "Step 3: State the resulting answer."
            ),
            final_answer="Development mock answer",
        )

    def generate_with_prefix(
        self,
        question: str,
        prefix: str,
    ) -> LLMResponse:

        return self.generate_reasoning(question)


    #mock service for testing purposes