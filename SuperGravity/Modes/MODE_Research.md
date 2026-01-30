---
name: research
description: Deep investigation and information gathering
activation: Learning new tech, investigating issues, exploring options
---

# Research Mode

> **Context Framework Note**: Optimizes for information gathering and analysis.

## When to Use
- Learning new technologies
- Investigating bugs
- Exploring solutions
- Comparing options
- Understanding codebases

## Behavioral Changes

### Thorough Investigation
- Multiple source consultation
- Cross-reference findings
- Verify information
- Document sources

### Tool Usage
- Web search via Tavily
- Documentation via Context7
- Code analysis tools
- Browser for live docs

### Comprehensive Output
- Detailed explanations
- Multiple options presented
- Pros/cons analysis
- Recommendations with rationale

### Knowledge Building
- Save to knowledge base
- Create reference artifacts
- Link related findings
- Build understanding

## Research Process

1. **Gather** - Collect information from multiple sources
2. **Verify** - Cross-check facts and claims
3. **Analyze** - Compare options and approaches
4. **Synthesize** - Combine into recommendations
5. **Document** - Save findings for future use

## Example Output

```markdown
## Research: State Management Options

### Options Analyzed
1. **Zustand** - Simple, minimal boilerplate
2. **Jotai** - Atomic model, fine-grained
3. **Redux Toolkit** - Mature, full-featured

### Comparison
| Feature | Zustand | Jotai | Redux |
|---------|---------|-------|-------|
| Bundle Size | 1.1kb | 2.4kb | 10kb |
| Learning Curve | Low | Low | Medium |
| DevTools | Yes | Yes | Yes |
| TypeScript | Excellent | Excellent | Good |

### Recommendation
For this project, **Zustand** is recommended because:
- Simple API matches project complexity
- Smallest bundle size
- Excellent TypeScript support

### Sources
- Zustand docs: github.com/pmndrs/zustand
- Bundle analysis: bundlephobia.com
- Benchmarks: ...
```

## Activation
```
/sg:mode research
```
Or automatic when:
- "research", "investigate", "explore" detected
- "compare options", "what's best" questions
- Learning new technology

## Deactivation
- `/sg:mode planning` to start implementing
- `/sg:mode fast` for quick execution
