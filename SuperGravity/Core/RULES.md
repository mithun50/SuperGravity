# SuperGravity Rules

> **Framework Note**: These rules are always active in Google Antigravity IDE.

## Mandatory Rules

### R1: Read Before Write
**Always** read existing code before modifying. Never change code you haven't examined.

### R2: Verify Before Execute
**Check** paths and commands before execution. Use artifacts to confirm.

### R3: Backup Before Destructive
**Create** backups before destructive operations (deletions, migrations, resets).

### R4: Test After Change
**Verify** changes work by running tests or manual checks.

### R5: Document Decisions
**Record** significant decisions in artifacts or knowledge base.

## Code Rules

### C1: Type Safety
- Use TypeScript for JavaScript projects
- Use type hints for Python
- Avoid `any` types
- Define interfaces for complex objects

### C2: Error Handling
- Wrap external calls in try/catch
- Provide meaningful error messages
- Log errors appropriately
- Never swallow exceptions

### C3: Security
- Never hardcode secrets
- Validate all inputs
- Use parameterized queries
- Follow least privilege

### C4: Naming
- Descriptive, searchable names
- Follow language conventions
- Avoid abbreviations
- Name functions by what they do

## Git Rules

### G1: Commit Hygiene
- Meaningful commit messages
- One logical change per commit
- Never commit secrets
- Reference issues when applicable

### G2: Branch Safety
- Never force push to main
- Create feature branches
- Keep branches short-lived
- Delete merged branches

## Artifact Rules

### A1: Implementation Plans
- Create before major changes
- Include scope and risks
- Get approval first
- Update if scope changes

### A2: Code Diffs
- Generate for all changes
- Highlight security modifications
- Include context
- Link related artifacts

### A3: Verification
- Screenshot UI changes
- Record browser interactions
- Document test results
- Capture error states

## Autonomy Rules

### Secure Mode
- Approval for all commands
- No auto JavaScript
- Manual review required

### Review-Driven
- Execute approved commands
- Pause at checkpoints
- Request review for risky ops

### Agent-Driven
- Execute within bounds
- Self-verify with artifacts
- Report completion
- Flag unexpected situations
