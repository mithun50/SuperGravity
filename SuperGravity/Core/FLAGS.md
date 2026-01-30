# SuperGravity Flags

> **Framework Note**: Flags modify command behavior in Google Antigravity.

## Safety Flags

| Flag | Effect |
|------|--------|
| `--safe` | Maximum safety checks, confirmations, backups |
| `--dry-run` | Preview without executing |
| `--force` | Bypass confirmations (use carefully) |

## Verbosity Flags

| Flag | Effect |
|------|--------|
| `--verbose` / `-v` | Detailed output with reasoning |
| `--quiet` / `-q` | Minimal output, errors only |
| `--debug` | Maximum diagnostics |

## Execution Flags

| Flag | Effect |
|------|--------|
| `--fast` | Speed over thoroughness |
| `--thorough` | Completeness over speed |
| `--parallel` | Multi-agent execution |

## Output Flags

| Flag | Effect |
|------|--------|
| `--json` | JSON output for pipelines |
| `--markdown` | Formatted markdown |
| `--artifact` | Create Antigravity artifact |

## Scope Flags

| Flag | Effect |
|------|--------|
| `--workspace` | Current workspace only |
| `--global` | Cross-workspace |
| `--recursive` / `-r` | Include subdirectories |

## Feature Flags

| Flag | Effect |
|------|--------|
| `--with-tests` | Include test generation |
| `--with-docs` | Include documentation |
| `--coverage` | Generate coverage report |
| `--changelog` | Update changelog |

## Usage Examples

```bash
# Safe implementation with tests
/sg:implement payment --safe --with-tests

# Fast quiet build
/sg:build --fast --quiet

# Thorough security audit as JSON
/sg:security --thorough --json

# Dry-run deployment with artifact
/sg:deploy staging --dry-run --artifact
```

## Precedence

1. `--safe` overrides `--force`
2. `--dry-run` overrides execution
3. Explicit flags override defaults
4. Later flags override earlier
