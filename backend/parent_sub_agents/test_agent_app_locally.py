import logging
import asyncio

from vertexai.preview import reasoning_engines
import agent

logging.basicConfig(level=logging.INFO)

async def main():
    agent_app = reasoning_engines.AdkApp(
        agent=agent.root_agent,
        enable_tracing=True,
    )

    session = agent_app.create_session(user_id="u_123")

    for event in agent_app.stream_query(
        user_id="u_123",
        session_id=session.id,
        message="""
                User: I'm thinking about investing some of my savings, but I'm not sure where to start. Can you help me figure out a good strategy?
                Virtual Agent: I can certainly help with that. To provide personalized advice, I first need to understand your overall financial situation.
                User: That makes sense. What do you need to know?
                Virtual Agent: I will now gather your latest financial data to create a complete profile. This includes your net worth, transaction history to understand your income and expenses, and any existing investments. Please wait a moment.
            """,
    ):
        # FIX: Check if the event part has text before trying to print it.
        # This handles cases where the event is a tool/function call.
        text_part = event["content"]["parts"][0].get("text")
        if text_part:
            logging.info("[local test] " + text_part)
        else:
            # This part is optional, but it's useful to see when a non-text event occurs.
            logging.info("[local test] Received a non-text event (likely a tool call).")

if __name__ == "__main__":
    asyncio.run(main())
