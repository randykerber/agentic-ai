# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational repository for "Agentic AI in Action" - a hands-on workshop on building autonomous, multi-agent systems in Python. The codebase originates from a 4-hour YouTube overview: https://youtu.be/LSk5KaEGVk4?si=mzMfZXo13MhdO3lv

Source repository: https://github.com/ed-donner/action
This fork: https://github.com/randykerber/agentic-ai

The repo contains three main lab exercises showcasing different AI agent frameworks and patterns:

1. **Deep Research** (1_deep_research/) - Multi-agent research system using OpenAI Agents
2. **Engineering Team** (2_engineering_team/) - CrewAI-based software development team simulation  
3. **Trading Floor** (3_trading_floor/) - Real-time trading agents using various LLM providers

## Development Environment

This project uses **uv** for Python dependency management. The main `pyproject.toml` requires Python >=3.12.

### System Context
- **Terminal:** Warp (note: Shift+Enter doesn't work for prompt continuation)
- **IDE:** Transitioning from Warp terminal to PyCharm
- **Package Management:** Homebrew for system tools, uv for Python, transitioning from global to local npm packages
- **Python:** Clean isolation - no global packages, using Python 3.13 via Homebrew
- **Available Tools:** ollama, aichat, gh, docker, direnv, and comprehensive development stack

### Common Commands

#### Environment Setup
```bash
# Install dependencies for the main project
uv sync

# Install CrewAI tools for lab 2
uv tool install crewai
uv tool upgrade crewai

# Install dependencies for engineering team lab
cd 2_engineering_team/engineering_team && crewai install
```

#### Running Labs

**Lab 1 - Deep Research:**
```bash
cd 1_deep_research
python deep_research/deep_research.py
# Launches Gradio UI for research queries
```

**Lab 2 - Engineering Team:**
```bash
cd 2_engineering_team/engineering_team
crewai run
# Available commands: run_crew, train, replay, test
```

**Lab 3 - Trading Floor:**
```bash
cd 3_trading_floor
python trading_floor.py
# Runs trading simulation every N minutes
```

#### Interactive Development
Jupyter notebooks are used extensively for lab exercises and guides:
```bash
# Launch any .ipynb file in the project
jupyter lab <notebook_file>
```

## Architecture Overview

### 1. Deep Research System (Lab 1)
- **Pattern**: Multi-agent pipeline with specialized roles
- **Core Components**:
  - `ResearchManager`: Orchestrates the research workflow
  - `search_agent.py`: Web search and data gathering
  - `planner_agent.py`: Creates search plans from queries
  - `writer_agent.py`: Synthesizes findings into reports
  - `push_agent.py`: Handles notifications
- **UI**: Gradio-based web interface for research queries
- **Key Dependencies**: OpenAI Agents, Gradio, various web scraping tools

### 2. Engineering Team (Lab 2)  
- **Pattern**: CrewAI-based role-playing agents
- **Core Components**:
  - `crew.py`: Defines agent roles (lead, backend, frontend, test engineers)
  - `config/agents.yaml`: Agent configurations and backstories
  - `config/tasks.yaml`: Task definitions and workflows
- **Output**: Generates complete Python modules with design docs and tests
- **Key Dependencies**: CrewAI framework with tools

### 3. Trading Floor (Lab 3)
- **Pattern**: Autonomous trading agents with real-time market data
- **Core Components**:
  - `trading_floor.py`: Main scheduler and orchestrator
  - `traders.py`: Individual trader agent implementations
  - `market.py`: Market data and trading hours logic  
  - `accounts_server.py`: Account management and portfolio tracking
  - `agents.py`: Core agent framework and MCP integrations
- **Multi-Model Support**: GPT-4, DeepSeek, Gemini, Grok
- **Key Dependencies**: Multiple LLM providers, MCP servers, real-time data APIs

## Configuration

### Environment Variables
Required for different labs:
- `OPENAI_API_KEY`: For OpenAI models (all labs)
- `DEEPSEEK_API_KEY`: For DeepSeek models (trading floor)
- `GOOGLE_API_KEY`: For Gemini models (trading floor)
- `GROK_API_KEY`: For Grok models (trading floor)
- `OPENROUTER_API_KEY`: For OpenRouter models (trading floor)
- `RUN_EVERY_N_MINUTES`: Trading frequency (default: 60)
- `USE_MANY_MODELS`: Enable multi-model trading (trading floor)

### Key Configuration Files
- `pyproject.toml`: Main project dependencies
- `2_engineering_team/engineering_team/pyproject.toml`: CrewAI project config
- `2_engineering_team/engineering_team/config/`: Agent and task definitions
- `.env`: Environment variables (create from examples in setup docs)

## Testing and Development

No centralized testing framework is configured. Each lab has its own testing approach:
- Lab 2 (CrewAI): Uses `crewai test` command
- Lab 3 (Trading): Manual testing through simulation runs
- Jupyter notebooks: Interactive testing and exploration

## MCP (Model Context Protocol) Integration

Lab 3 extensively uses MCP servers for:
- Real-time market data fetching
- Account management and portfolio operations  
- Trading execution and monitoring
- Custom tool integrations

MCP configurations are defined in `mcp_params.py` with separate parameter sets for trader and researcher agents.