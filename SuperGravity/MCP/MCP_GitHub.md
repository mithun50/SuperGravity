# GitHub MCP Server

**Purpose**: GitHub operations - PRs, issues, repos, and code management

## Triggers
- Creating or managing pull requests
- Working with GitHub issues
- Repository operations (create, clone, fork)
- Code review workflows
- Release management
- GitHub Actions workflows

## Choose When
- **For PRs**: Creating, reviewing, merging pull requests
- **For issues**: Creating, updating, closing issues
- **For repos**: Repository management operations
- **For releases**: Version tagging and release notes
- **For CI/CD**: GitHub Actions workflow management

## Works Best With
- **Sequential**: Plan complex GitHub workflows
- **Filesystem**: Prepare files before committing

## Configuration
Requires `GITHUB_TOKEN` environment variable with appropriate scopes.

## Examples
```
"create a PR for this feature" → GitHub (PR creation)
"list open issues" → GitHub (issue management)
"create a new release v1.2.0" → GitHub (release management)
"review PR #42" → GitHub (code review)
```
