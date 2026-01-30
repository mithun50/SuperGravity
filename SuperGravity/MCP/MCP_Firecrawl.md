# Firecrawl MCP Server

**Purpose**: Web scraping and content extraction from websites

## Triggers
- Need to extract content from web pages
- Scraping documentation or articles
- Gathering data from websites
- Converting web content to structured data

## Choose When
- **Over Tavily**: When you need full page content, not search results
- **For extraction**: Pulling specific data from web pages
- **For documentation**: Scraping docs not in Context7
- **For data**: Gathering structured data from websites

## Works Best With
- **Sequential**: Plan scraping workflows
- **Context7**: Supplement with official docs

## Configuration
Requires `FIRECRAWL_API_KEY` environment variable.

## Ethical Notes
- Respect robots.txt
- Don't overload target servers
- Only scrape publicly available content
- Follow terms of service

## Examples
```
"extract the main content from this URL" → Firecrawl
"scrape the pricing table from this page" → Firecrawl
"get all code examples from this tutorial" → Firecrawl
"search for React hooks info" → Tavily (search better)
```
