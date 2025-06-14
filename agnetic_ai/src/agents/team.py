# src/agents/team.py
from mcp import Team
from src.agents.calendar_mcp import mcp as calendar_mcp

team = Team(
    name="Agnetic AI MCP Team",
    agents=[calendar_mcp],
    description="Handles travel scheduling, health monitoring, and local intelligence"
)