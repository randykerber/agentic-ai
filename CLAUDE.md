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

## SiloSlayer Project (Silo-Slayer Syndicate)

### Project Status (Current Session)
- ✅ **Lab 2 (CrewAI)**: Working with Docker support - successfully generated account management system
- ✅ **Lab 3 (Trading Floor)**: Working with MCP servers - continuous agent processing functional
- 🎯 **Focus Decision**: Extending Lab 3 architecture for SiloSlayer mission - deploying the A-Team against information chaos

### Problem Definition
**Core Challenge**: Taming the "life-sucking beast" of information silos and overwhelming daily information workflows.

**Specific Pain Points:**
- 1219 unprocessed notes in Drafts (universal capture working, processing failing)
- Information scattered across tools: Drafts, Obsidian (7200+ notes across Main/Tech vaults), Bear, 1Password
- Mobile vs desktop capability gaps
- "Where is that piece of information?" problem
- Voice capture while driving → organized knowledge base workflow missing
- Information overload from podcasts, articles, feeds with no effective filtering/extraction

### Tool Inventory & Capabilities

**Primary Tools:**
- **Drafts**: Universal inbox, voice transcription, JavaScript automation, AI integration (Claude/ChatGPT/Gemini)
- **Obsidian**: Structured knowledge base (Main: investing/financial, Tech: development)
- **Actions for Obsidian**: 50+ Shortcuts actions, mobile-friendly vault integration
- **Apple Shortcuts**: Cross-device automation, Siri integration
- **Siri**: Voice interface + "Type to Siri" text input capability  
- **Raycast**: ~20 Drafts commands, universal launcher, can trigger Shortcuts
- **Bear**: Personal/mobile-friendly notes, fast launch
- **1Password**: Credentials, codes, ephemeral reference data

**Supporting Tools:**
- **SuperWhisper**: Voice input processing
- **iCloud**: 2TB storage for cross-device sync (no compute platform)
- **Lab 3 MCP Architecture**: Real-time agents, external service integration
- **Silo-Slayer Syndicate**: Coordinated AI agents executing the SiloSlayer mission

### Architecture Decisions

**1. Lab 3 vs Lab 2 Choice:**
- **Lab 3 selected** for always-on nature, existing MCP integration, async parallel processing
- Better fit for real-time information routing vs CrewAI's sequential task-based approach

**2. Information Flow Strategy:**
- **Keep Drafts as Universal Inbox** - don't change what's working for capture
- **Add Smart Exits** from Drafts rather than replacing entry point
- **Focus on NEW information flow** - prevent backlog growth vs solving existing pile

**3. Processing Location:**
- **Mac-based processing** with iCloud sync (vs cloud compute)
- Mobile captures → iCloud → Mac processes → results sync back
- Trade-off: Processing depends on Mac availability vs always-on cloud costs

**4. Unified Pipeline Architecture:**
```
Multiple Inputs → Unified Text Object → Single Processing Pipeline
- Voice (Siri) + Text (Type to Siri) + Raycast + Direct entry
- All converge to single "Universal Router" Shortcut
- Avoid maintenance nightmare of redundant 80-90% similar workflows
```

### Routing Strategy

**Smart Destination Logic:**
- **Obsidian Main**: Investment/financial content
- **Obsidian Tech**: Development/technical content  
- **Bear**: Personal, mobile-accessible content
- **1Password**: Codes, credentials, ephemeral reference
- **"Digital Junk Drawer"**: Searchable blob for random bits (bathroom codes, etc.)
- **Drafts**: Remains safety net for truly ambiguous items

**Processing Priorities:**
1. **Recent 20-50 Drafts items**: AI-assisted triage with human decisions
2. **New capture routing**: Direct routing to skip Drafts for obvious items
3. **Backlog (1170+ items)**: Bulk categorization, many → searchable storage

### Key Insights & Constraints

**"National Debt" Analogy**: 
- Eliminating 1219-item pile is pipe dream
- Reducing rate of growth is meaningful win
- Success = pile grows 5-10/month vs 50+/month

**Mobile Reality**:
- Actions for Obsidian provides mobile → vault pipeline
- Heavy processing must happen on Mac or cloud
- Voice input not panacea - need text alternatives

**Architecture Principles**:
- **DRY for workflows** - single processing pipeline, multiple entry points
- **Capture first, route smart** - don't guess destination during capture
- **Accept some residual** - not everything needs perfect categorization

### SiloSlayer Implementation Roadmap

**Phase 1 - A-Team Assembly:**
- [ ] Purchase/install Actions for Obsidian
- [ ] Create basic voice → Obsidian workflows
- [ ] Test "Type to Siri" capability

**Phase 2 - A-Team Deployment (Smart Routing):**
- [ ] Build "Universal Router" Shortcut with AI categorization
- [ ] Create multiple input wrappers (Siri, Raycast, direct)
- [ ] Test with new captures to refine routing logic

**Phase 3 - SiloSlayer Assault (Backlog Processing):**
- [ ] Extend Lab 3 with Drafts MCP server
- [ ] AI-assisted triage for recent items
- [ ] Bulk processing strategies for older items (1219 Drafts targets)

**Phase 4 - Total Victory (Advanced Integration):**
- [ ] Podcast/article processing workflows
- [ ] Notification intelligence (right time, right place)
- [ ] Cross-tool search and retrieval

### Research Notes
- User has existing Obsidian research in Tech vault: `/Users/rk/Library/Mobile Documents/iCloud~md~obsidian/Documents/Tech/INBOX/Actions For Obsidian.md`
- Comprehensive documentation of Actions for Obsidian capabilities already researched
- 7200+ existing Obsidian notes indicate deep investment in structured knowledge management

### Priority Items for Next Session

**1. Context Engineering Priority:**
- Context Engineering identified as potentially highest-leverage area for AI productivity
- MCP Resources (context pillar) is underexplored compared to Tools
- Universal context system could be breakthrough - but limited to MCP-compatible platforms
- Most major platforms (ChatGPT, Gemini, Grok) won't support MCP context servers

**2. Multi-Language Architecture Clarity:**
- This Python project stays pure Python (Lab 3 intelligence hub)
- JavaScript/Swift MCP servers in separate projects
- Integration via MCP protocol only - clean separation

**3. Mobile Front Door Investigation:**
- **URGENT**: Raycast mobile version now exists - investigate capabilities vs assumptions
- Test "Type to Siri" functionality for text input alternative
- Evaluate AI apps (ChatGPT, Claude, Gemini) for intelligence layer
- Apple Shortcuts remains strong candidate for action execution

**4. Critical Implementation Insights:**
- Focus on NEW capture flow (prevent backlog growth) vs solving existing 1219 items
- "National debt" approach - success = reducing growth rate, not eliminating pile
- Build Universal Router Shortcut (single pipeline, multiple inputs) - avoid maintenance nightmare
- Keep Drafts as universal inbox, add smart exits rather than replacing entry point

**5. Implementation Research Completed (Current Session):**
- ✅ **Actions for Obsidian**: $9-15 one-time purchase, 40+ Shortcuts actions, 14-day free trial
- ✅ **Raycast Mobile**: Available iOS app (launched April 2025) with AI, notes, snippets, cloud sync
- ✅ **Type to Siri**: Enhanced iOS 18.1 with Apple Intelligence, double-tap activation, full automation support
- ✅ **Apple Shortcuts AI**: WWDC 2025 AI integration, direct LLM access, intelligent categorization actions

### Universal Router Architecture (Silo-Slayer Syndicate Coordination Hub)

**Core Design Pattern:**
```
Multiple Input Methods → Universal Router Shortcut → AI Categorization → Smart Routing → Destination Tools
```

**Input Methods (All converge to single Shortcut):**
1. **Voice**: Siri voice activation → Universal Router
2. **Text**: "Type to Siri" (double-tap) → Universal Router  
3. **Raycast**: Raycast mobile/desktop commands → Universal Router
4. **Direct**: Manual Shortcut trigger → Universal Router
5. **Clipboard**: Auto-detect copied text → Universal Router

**AI Processing Layer (Apple Intelligence):**
- **On-Device LLM**: Apple's Foundation Models for privacy-first categorization
- **Text Analysis**: Content type detection (financial, technical, personal, ephemeral)
- **Confidence Scoring**: High confidence = direct routing, low confidence = user choice
- **Context Awareness**: Time, location, recent activity patterns

**Routing Logic:**
```
High Confidence Routes:
- Financial keywords → Obsidian Main vault
- Code/technical → Obsidian Tech vault  
- Personal/family → Bear notes
- Passwords/codes → 1Password
- URLs/references → Digital Junk Drawer

Medium Confidence:
- Present 2-3 destination options with reasoning
- User selects with single tap

Low Confidence:
- Default to Drafts (safety net)
- Flag for manual review
```

**Implementation Components:**
1. **Universal Router.shortcut**: Main processing pipeline
2. **Voice Wrapper.shortcut**: Siri activation → Router
3. **Text Wrapper.shortcut**: Type to Siri → Router
4. **Raycast Integration**: Commands trigger Router via URL schemes
5. **Actions for Obsidian**: Vault writing capabilities
6. **MCP Bridge**: Connection to Lab 3 Silo-Slayer Syndicate for complex processing

### Session Progress Update (Current Session)

**✅ Major Accomplishments:**
- **Voice workflow validated**: Siri → transcribe → clipboard → JetBrains working
- **Obsidian JavaScript capabilities confirmed**: Sophisticated automation possible (file renaming with link updates, tag-based organization, external API integration, structured markdown parsing)
- **SiloSlayer Syndicate implemented**: Complete MCP server and agent framework
- **Push notifications working**: Pushover integration tested and operational
- **Architecture pivot**: From rule-based routing to "English as programming language" approach

**🎯 Next Phase Vision:**
- **Pretotype approach**: End-to-end smoke tests with hardcoded examples
- **Real AI + Real tools**: Claude API calls → actual tool execution → push notifications
- **English instruction workflow**: "Add to Fin vault, MP page, Analysis section, link to [[Luke Gromen]]"
- **Karpathy path**: Over-leverage AI agents, treat English as the new software language

**📁 Files Created This Session:**
- `3_trading_floor/drafts_server.py` - Drafts MCP server with categorization tools
- `3_trading_floor/siloslayer.py` - SiloSlayer agent with triage/routing missions  
- `3_trading_floor/test_siloslayer.py` - Test suite for agent deployment
- Updated `3_trading_floor/mcp_params.py` - Added SiloSlayer MCP configuration

**🔧 Technical Validation:**
- **Pushover notifications**: Credentials configured, test message sent successfully
- **MCP architecture**: All servers operational, ready for English instruction dispatcher
- **Voice input**: Multiple working methods (Siri, SuperWhisper, Type to Siri)

**🎯 Ready for Next Session:**
- Build pretotype with hardcoded examples + real AI calls + real tool execution
- Test English instruction parsing and tool dispatch
- Validate "AI as dispatcher" concept before building full automation

### Architecture Understanding Achieved (Current Session)

**✅ Core Insights Clarified:**
- **MCP = Language-Agnostic Tools**: Function calls over protocol, implementation language irrelevant
- **OpenAI Agents = Manual Orchestration**: You write coordination logic, framework provides agents/tools
- **JavaScript/TypeScript Full MCP Support**: Official SDK with feature parity to Python
- **Multi-Agent Reality Check**: Most systems are "carefully staged dominos" not magical cooperation

**🎯 The REAL SiloSlayer Mission Discovered:**
Not just Drafts processing, but **Information Liberation from App Silos**

**Problem Statement:**
- **Content Scattered**: YouTube saves, Substack queues, podcast apps, Twitter bookmarks
- **Tasks Fragmented**: Apple Reminders, Things, Calendar items  
- **Information Flood**: 20+ daily podcast episodes, endless YouTube/Substack content
- **Silo Prison**: "Which app did I save that in?" vs "What should I focus on next?"

**Core Workflow Examples:**
1. **Fragment Enhancement**: "Fed will pivot at 4.5% unemployment" → enriched with source, context, proper Obsidian integration
2. **English Instructions**: "Save as episode, link to Luke Gromen, clean up language, preserve quotes"
3. **Unified Content Dashboard**: All saved content from all apps in one prioritized view
4. **Intelligent Triage**: 50+ daily content items → AI-filtered priority queues

**Key Architecture Decisions:**
- **Hybrid JS/Python**: JavaScript for native tool integration, Python for AI orchestration
- **Content Liberation Focus**: Break out of app silos into unified command center
- **Human + AI Collaboration**: User decides, AI executes with intelligent assistance
- **"English as Programming Language"**: Voice/text instructions → multi-agent execution

**Next Phase Priority:**
Build unified content aggregation system that liberates information from YouTube, Substack, podcast apps, reminder systems into single prioritized dashboard.

## Tool Integration Analysis: JavaScript vs Python for SiloSlayer Syndicate

### Summary Assessment
For critical SiloSlayer tools (Raycast, Obsidian, Drafts), **JavaScript provides significantly richer, more capable native integration** compared to Python. MCP protocol enables hybrid architecture where both languages can leverage each other's strengths.

### Detailed Tool Capabilities

#### **Raycast Integration:**
**JavaScript (Native Extension):**
- ✅ Full Raycast API access with rich UI components (`List`, `ActionPanel`, `Action`)
- ✅ Native search, commands, preferences integration
- ✅ Real-time user interface with native look/feel
- ✅ Deep OS integration capabilities

**Python (via MCP):**
- ❌ Limited to custom MCP server bridging
- ❌ JSON data only, no native UI integration
- ❌ Protocol overhead and limitations

**Verdict:** JavaScript wins massively - native UI, full API access, superior UX

#### **Drafts Integration:**
**JavaScript (Native Actions):**
- ✅ Full Drafts JavaScript runtime with direct object access
- ✅ Complete Draft API: `Draft.query()`, object manipulation, tag management
- ✅ Direct integration with other apps via URL schemes
- ✅ No protocol limitations or data serialization overhead

**Python (via MCP):**
- ❌ Limited to URL schemes or file system access
- ❌ Protocol barriers prevent direct object manipulation
- ❌ Data serialization overhead

**Verdict:** JavaScript wins - direct object access, no protocol limitations

#### **Obsidian Integration:**
**JavaScript (Native Plugin):**
- ✅ Full Obsidian Plugin API access
- ✅ Direct vault manipulation (`app.vault.create()`, metadata cache)
- ✅ Rich linking and cross-reference capabilities
- ✅ File system and metadata integration

**Python (via MCP):**
- ❌ Limited to custom MCP server implementations
- ❌ API capabilities restricted by MCP tool definitions
- ❌ Less sophisticated metadata and linking operations

**Verdict:** JavaScript wins - full vault access, metadata cache, rich linking

#### **Apple Shortcuts Integration:**
**Both Languages:**
- ≈ URL schemes and HTTP calls available to both
- ≈ Similar limitations and capabilities
- ≈ No significant advantage either direction

**Verdict:** Tie - both limited to URL schemes/HTTP calls

### MCP Ecosystem Maturity

#### **Python MCP Ecosystem:**
- ✅ More mature server implementations available
- ✅ Broader variety of pre-built MCP servers
- ✅ Better documentation and examples
- ✅ Established patterns and best practices

#### **JavaScript MCP Ecosystem:**
- ❌ Fewer pre-built server implementations
- ❌ Less mature ecosystem overall
- ✅ Official TypeScript SDK with full feature parity
- ✅ Rapid development and growing adoption

### Strategic Implications

#### **Hybrid Architecture Recommended:**
```
Silo-Slayer Syndicate Architecture:
├── Python: Agent orchestration, mature MCP servers, AI workflows
├── JavaScript: Native tool integrations, rich UI components  
└── MCP Protocol: Language-agnostic communication bridge
```

#### **Migration Strategy:**
1. **Maintain Python infrastructure** (proven, mature MCP ecosystem)
2. **Develop JavaScript tool integrations** (leverage native API superiority)
3. **Bridge via MCP** as tools become "published" to protocol
4. **Gradual transition** as JavaScript MCP ecosystem matures

#### **Tool Integration Priority:**
- **Immediate JavaScript development**: Raycast extensions, Drafts actions, Obsidian plugins
- **Python coordination**: Agent orchestration, complex workflows, AI model management
- **MCP bridging**: Expose JavaScript tool capabilities to Python agents

### Conclusion
JavaScript provides **3 out of 4 key integrations** with significantly superior capabilities. The **hybrid approach leverages both ecosystems' strengths** while using MCP as the unifying protocol for cross-language tool coordination.

## SiloSlayer Syndicate (SSS) Multi-Project Architecture

### Project Overview
The SiloSlayer Syndicate is a comprehensive information liberation system designed to break users out of "app silos" and create unified, intelligent content management across multiple tools and platforms.

### Project Structure
```
SiloSlayer Syndicate (SSS) System:
├── agentic-ai/          (Python) - Agent orchestration, MCP servers, AI workflows
├── syndicate-js/        (JavaScript/TypeScript) - Native tool integrations, rich UI
└── raycast-ext/         (TypeScript) - Personal Raycast commands and extensions
```

### Core Mission
**Problem**: Information scattered across Drafts (1219+ notes), Obsidian (7200+ notes), YouTube saves, Substack queues, podcast apps, reminder systems - creating "app prison" where users can't find their own information.

**Solution**: AI-powered information liberation using "English as programming language" approach where voice/text instructions trigger multi-agent workflows that intelligently route content to proper destinations.

### Key Architecture Principles
- **Hybrid Python/JavaScript**: Leverage each language's strengths via MCP protocol
- **Human + AI Collaboration**: User provides intent, AI executes with intelligent assistance  
- **Information Liberation**: Break down silos into unified command center
- **English Instructions**: Natural language becomes the programming interface

### Inter-Project Coordination
Projects communicate via MCP (Model Context Protocol) for language-agnostic tool sharing. Python side handles agent orchestration and complex AI workflows, while JavaScript side provides native integrations with target applications (Raycast, Drafts, Obsidian, Apple Shortcuts).

**6. Context Window Management:**
- This session reached 87% context usage before auto-compact
- Break into focused implementation sessions using CLAUDE.md for continuity
- Monitor Claude Code context percentage to avoid information loss