# Tavily MCP Server

**Purpose**: Web search for real-time information and research

## Triggers
- Questions about current events or recent developments
- Need for real-time data not in training data
- Research tasks requiring multiple sources
- Fact-checking or verification needs
- Documentation for newly released tools/libraries

## Choose When
- **Over Context7**: When you need current/live information vs static docs
- **Over native knowledge**: When information might be outdated
- **For research**: Gathering information from multiple web sources
- **For verification**: Cross-checking facts with current sources

## Works Best With
- **Context7**: Tavily finds current info → Context7 provides implementation patterns
- **Sequential**: Tavily gathers research → Sequential synthesizes findings

## Configuration
Requires `TAVILY_API_KEY` environment variable.

## Examples
```
"what's new in React 19" → Tavily (current release info)
"latest security vulnerabilities" → Tavily (real-time security data)
"compare Next.js vs Remix in 2024" → Tavily (current comparisons)
"how to implement useEffect" → Context7 (static documentation better)
```
