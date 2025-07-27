import os
import sys
import requests
import uuid

# --- Corrected Imports ---
# These files (prompt.py, callback_logging.py) must be in the same directory as agent.py
import prompt
from callback_logging import log_query_to_model, log_model_response

from google.adk.agents import Agent
from google.genai.types import GenerateContentResponse
from google.adk.tools.tool_context import ToolContext
from google.genai import types

# --- Environment Variable Check ---
# Ensure the MODEL environment variable is set. This is critical for Cloud Run.
model_name = os.getenv("MODEL")
if not model_name:
    raise ValueError("FATAL: The 'MODEL' environment variable is not set. Deployment will fail.")

# --- Core Tool: The MCP Client ---
# This single, powerful tool is the bridge to the entire Fi MCP server.
def call_mcp_tool(
    tool_context: ToolContext,
    tool_name: str,
    arguments: dict
) -> dict:
    """
    Acts as a client to call a tool on the remote MCP service.

    Args:
        tool_name (str): The name of the tool to call on the remote service.
        arguments (dict): The arguments to pass to the remote tool.

    Returns:
        A dictionary containing the response from the remote service.
    """
    url = "https://fi-mcp-prod-server-93313385804.us-central1.run.app/mcp/stream"

    mcp_session_id = tool_context.state.get(
        "mcp_session_id",
        "mcp-session-594e48ea-fea1-40ef-8c52-7552dd9272af"
    )

    headers = {
        "Content-Type": "application/json",
        "Mcp-Session-Id": mcp_session_id
    }

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }

    try:
        print(f"--- Calling MCP client for remote tool: {tool_name} with args {arguments} ---")
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()
        return result

    except requests.exceptions.RequestException as e:
        print(f"Error calling MCP client: {e}")
        return {"error": "Could not connect to the MCP service.", "details": str(e)}

# --- Specialist Sub-Agents (with logging callbacks) ---

net_worth_agent = Agent(
    name="net_worth_agent",
    model=model_name,
    description="Fetches user's net worth details from the MCP service.",
    instruction=prompt.NET_WORTH_PROMPT,
    tools=[call_mcp_tool]
)

credit_report_agent = Agent(
    name="credit_report_agent",
    model=model_name,
    description="Fetches user's credit report data from the MCP service.",
    instruction=prompt.CREDIT_REPORT_PROMPT,
    tools=[call_mcp_tool]
)

epf_details_agent = Agent(
    name="epf_details_agent",
    model=model_name,
    description="Fetches user's Employee Provident Fund (EPF) details from the MCP service.",
    instruction=prompt.EPF_DETAILS_PROMPT,
    tools=[call_mcp_tool]
)

mf_transactions_agent = Agent(
    name="mf_transactions_agent",
    model=model_name,
    description="Fetches user's mutual fund transaction data from the MCP service.",
    instruction=prompt.MF_TRANSACTIONS_PROMPT,
    tools=[call_mcp_tool]
)

data_analyst_agent = Agent(
    name="data_analyst",
    model=model_name,
    description="Fetches, parses, and formats financial data (like bank transactions) into a clean, readable summary. Use this to get any raw financial data you need.",
    instruction=prompt.DATA_ANALYST_PROMPT,
    tools=[call_mcp_tool]
)

financial_insights_agent = Agent(
    name="financial_insights_agent",
    model=model_name,
    description="Analyzes a user's spending, income, and savings habits. It can get the data it needs and provide a full analysis.",
    instruction=prompt.FINANCIAL_INSIGHTS_PROMPT
)

investment_advisor_agent = Agent(
    name="investment_advisor_agent",
    model=model_name,
    description="Provides personalized investment advice after building a complete financial profile of the user.",
    instruction=prompt.INVESTMENT_ADVISOR_PROMPT
)

# --- Root Agent Definition ---

root_agent = Agent(
    name="financial_advisor",
    model=model_name,
    description="The main financial advisor that interacts with the user and delegates tasks.",
    instruction=prompt.FINANCIAL_ADVISOR_PROMPT,
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
    sub_agents=[
        data_analyst_agent,
        financial_insights_agent,
        investment_advisor_agent,
        net_worth_agent,
        credit_report_agent,
        epf_details_agent,
        mf_transactions_agent
    ]
)
