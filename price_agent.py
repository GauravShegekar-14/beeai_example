import asyncio

from beeai_framework.agents.requirement import RequirementAgent
from beeai_framework.agents.requirement.requirements.conditional import ConditionalRequirement
from beeai_framework.backend import ChatModel
from beeai_framework.errors import FrameworkError
from beeai_framework.middleware.trajectory import GlobalTrajectoryMiddleware
from beeai_framework.tools import Tool
from beeai_framework.tools.think import ThinkTool
from beeai_framework.tools.weather import OpenMeteoTool


async def main() -> None:
    # ---- Single Intelligent Agent ----
    single_agent = RequirementAgent(
        name="UniversalAgent",
        role="General Query Solver",
        instructions=(
            "You are a single AI agent responsible for handling all tasks: "
            "general knowledge lookup, reasoning, and weather forecasting. "
            "Use the provided tools efficiently."
        ),
        llm=ChatModel.from_name("ollama:granite3.3:8b"),

        tools=[
            ThinkTool(),
            OpenMeteoTool(),     # Weather tool
        ],

        requirements=[ConditionalRequirement(ThinkTool, force_at_step=1)],
        middlewares=[GlobalTrajectoryMiddleware(included=[Tool])]
    )

    # ---- Command-line input ----
    question = input("Enter your question: ")

    print(f"\nUser: {question}")

    try:
        response = await single_agent.run(
            question,
            expected_output="Concise, accurate, well-structured answer."
        )
        print("\nAgent:", response.last_message.text)

    except FrameworkError as err:
        print("\nError:", err.explain())


if __name__ == "__main__":
    asyncio.run(main())
