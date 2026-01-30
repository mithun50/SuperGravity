# Skills Guide

Complete guide to SuperGravity skills for Google Antigravity IDE.

---

## What Are Skills?

Skills are specialized AI capabilities that activate on-demand. Unlike rules (always active), skills load only when your request matches their description.

**Key Concept: Progressive Disclosure**
- Skills sit dormant until needed
- Loaded into context only when relevant
- Prevents context saturation
- Maintains lean token usage

---

## Included Skills (12)

SuperGravity installs these skills to `~/.gemini/antigravity/skills/`:

| Skill | Trigger Phrases |
|-------|-----------------|
| `fullstack-architect` | "scaffold project", "design architecture", "build full-stack" |
| `backend-engineer` | "create API", "build backend", "server-side" |
| `frontend-specialist` | "build UI", "create component", "responsive design" |
| `api-designer` | "design API", "REST endpoints", "GraphQL schema" |
| `database-expert` | "design schema", "optimize query", "database migration" |
| `security-engineer` | "security audit", "OWASP scan", "vulnerability check" |
| `test-engineer` | "write tests", "test coverage", "unit testing" |
| `devops-engineer` | "CI/CD pipeline", "Docker setup", "Kubernetes" |
| `code-reviewer` | "review code", "check quality", "PR review" |
| `refactoring-expert` | "refactor code", "clean up", "improve structure" |
| `performance-optimizer` | "optimize performance", "speed up", "reduce bundle" |
| `documentation-writer` | "write docs", "README", "API documentation" |

---

## Skill Scopes

### Global Skills
Available across all projects.

```
~/.gemini/antigravity/skills/
├── fullstack-architect/
│   └── SKILL.md
├── security-engineer/
│   └── SKILL.md
└── ...
```

### Workspace Skills
Available only in specific project.

```
your-project/.agent/skills/
├── my-custom-skill/
│   └── SKILL.md
└── project-deployer/
    └── SKILL.md
```

---

## Skill Directory Structure

```
skill-name/
├── SKILL.md           # Required - Main skill definition
├── scripts/           # Optional - Executable scripts
│   ├── run.py
│   └── util.sh
├── resources/         # Optional - Templates, configs
│   └── template.txt
├── examples/          # Optional - Sample inputs/outputs
│   └── example.json
└── assets/            # Optional - Images, data files
```

---

## SKILL.md Format

```markdown
---
name: skill-identifier
description: Clear trigger phrase describing when to use this skill.
---

# Skill Name

## Goal

Clear statement of what this skill does.

## Instructions

1. **Step One**
   - Details
   - More details

2. **Step Two**
   - Details

## Examples

**User**: "Example user request"
**Action**: What the skill does in response.

**User**: "Another example"
**Action**: Another response pattern.

## Constraints

- Do NOT do this
- Do NOT do that
- ALWAYS do this
- NEVER do that
```

### Required Fields

| Field | Location | Description |
|-------|----------|-------------|
| `name` | Frontmatter | Skill identifier (optional, defaults to directory name) |
| `description` | Frontmatter | **Critical** - Trigger phrase for activation |
| `Goal` | Body | Clear capability statement |
| `Instructions` | Body | Step-by-step logic |
| `Examples` | Body | Few-shot demonstrations |
| `Constraints` | Body | Boundaries and rules |

---

## Creating Custom Skills

### Step 1: Create Skill Directory

**For global skill:**
```bash
mkdir -p ~/.gemini/antigravity/skills/my-skill
```

**For workspace skill:**
```bash
mkdir -p .agent/skills/my-skill
```

### Step 2: Create SKILL.md

```bash
cat > ~/.gemini/antigravity/skills/my-skill/SKILL.md << 'EOF'
---
name: my-skill
description: Does X when user asks for Y. Use when user needs Z.
---

# My Custom Skill

## Goal

Accomplish X by doing Y.

## Instructions

1. **Analyze the Request**
   - Understand what user needs
   - Identify key requirements

2. **Execute the Task**
   - Perform the main action
   - Handle edge cases

3. **Verify Results**
   - Check output
   - Confirm with user

## Examples

**User**: "Do the thing"
**Action**: Analyze request, execute main task, verify results.

## Constraints

- Do NOT skip verification
- ALWAYS confirm before destructive actions
EOF
```

### Step 3: Test the Skill

In Antigravity IDE, try a request matching your description:
- "Help me with my-skill task"
- The skill should automatically activate

---

## Example: Git Commit Formatter

```markdown
---
name: git-commit-formatter
description: Format git commit messages using Conventional Commits. Use when user asks to commit or write commit messages.
---

# Git Commit Formatter

## Goal

Create properly formatted commit messages following Conventional Commits specification.

## Instructions

1. **Analyze Changes**
   - Review staged changes with `git diff --staged`
   - Identify the type of change (feat, fix, docs, etc.)

2. **Determine Type**
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation
   - `style`: Formatting
   - `refactor`: Code restructure
   - `perf`: Performance
   - `test`: Tests
   - `chore`: Maintenance

3. **Format Message**
   - Format: `<type>(<scope>): <description>`
   - Keep description under 50 characters
   - Use imperative mood ("add" not "added")

4. **Add Body if Needed**
   - Explain "why" not "what"
   - Wrap at 72 characters

## Examples

**User**: "Commit my changes"
**Action**: Run `git diff --staged`, analyze changes, suggest formatted commit message.

**User**: "Write commit message for auth feature"
**Action**: Suggest `feat(auth): add user authentication with JWT`

## Constraints

- Do NOT use past tense in subject
- Do NOT exceed 50 chars in subject line
- ALWAYS use conventional commit format
- ALWAYS analyze actual changes before suggesting
```

---

## Example: Project Deployer

```markdown
---
name: project-deployer
description: Deploy this project to production. Use when user asks to deploy, release, or push to production.
---

# Project Deployer

## Goal

Safely deploy the current project to production environment.

## Instructions

1. **Pre-flight Checks**
   - Verify on main/master branch
   - Check for uncommitted changes
   - Run test suite

2. **Build Application**
   - Run production build
   - Verify build succeeds
   - Check bundle size

3. **Deploy**
   - Push to production
   - Monitor deployment logs
   - Verify health checks

4. **Post-Deploy**
   - Run smoke tests
   - Check error rates
   - Notify team

## Examples

**User**: "Deploy to production"
**Action**: Run pre-flight checks, build, deploy, verify health.

**User**: "Release new version"
**Action**: Tag release, build, deploy, create release notes.

## Constraints

- Do NOT deploy with failing tests
- Do NOT skip pre-flight checks
- ALWAYS verify health after deploy
- ALWAYS have rollback plan ready
```

---

## Adding Scripts to Skills

Skills can include executable scripts for automation.

### Directory Structure

```
my-skill/
├── SKILL.md
└── scripts/
    ├── analyze.py
    └── deploy.sh
```

### Reference in SKILL.md

```markdown
## Instructions

1. **Run Analysis**
   - Execute `scripts/analyze.py` to gather data
   - Review output for issues

2. **Deploy**
   - Run `scripts/deploy.sh` for deployment
```

### Example Script (Python)

```python
#!/usr/bin/env python3
# scripts/analyze.py

import subprocess
import json

def analyze_codebase():
    # Run analysis
    result = subprocess.run(
        ["npx", "eslint", ".", "--format", "json"],
        capture_output=True,
        text=True
    )

    issues = json.loads(result.stdout)
    print(f"Found {len(issues)} files with issues")
    return issues

if __name__ == "__main__":
    analyze_codebase()
```

---

## Best Practices

### 1. Write Clear Descriptions
The `description` field is critical for activation:

**Good:**
```yaml
description: Generate database migrations for schema changes. Use when user asks to create migration, update schema, or add database columns.
```

**Bad:**
```yaml
description: Database stuff
```

### 2. Provide Concrete Examples
Help the AI understand expected behavior:

```markdown
## Examples

**User**: "Add email column to users table"
**Action**: Generate migration file `add_email_to_users.sql` with ALTER TABLE statement.

**User**: "Create posts table with user relationship"
**Action**: Generate migration with foreign key constraint to users table.
```

### 3. Set Clear Constraints
Prevent unwanted behavior:

```markdown
## Constraints

- Do NOT run migrations automatically without confirmation
- Do NOT drop columns without explicit user request
- ALWAYS create reversible migrations (up and down)
- ALWAYS backup data before destructive migrations
```

### 4. Keep Skills Focused
One skill = one capability. Don't create "kitchen sink" skills.

### 5. Test Activation
Verify your skill activates with various phrasings:
- "Help me with X"
- "I need to do X"
- "Can you X"
- "X please"

---

## Troubleshooting

### Skill Not Activating

1. **Check description field** - Make it more specific
2. **Verify file location** - Must be in `skills/name/SKILL.md`
3. **Check YAML syntax** - Frontmatter must be valid
4. **Restart Antigravity** - Skills load on startup

### Skill Conflicts

If multiple skills match:
- More specific descriptions win
- Workspace skills override global skills
- Consider combining into one skill

### Debugging

Add explicit trigger phrases to description:
```yaml
description: "Do X. Triggers: 'help with X', 'I need X', 'please X'"
```

---

## Managing Skills

### List Installed Skills

```bash
ls ~/.gemini/antigravity/skills/
ls .agent/skills/  # workspace skills
```

### View Skill Details

```bash
cat ~/.gemini/antigravity/skills/security-engineer/SKILL.md
```

### Remove a Skill

```bash
rm -rf ~/.gemini/antigravity/skills/skill-name
```

### Check SuperGravity Status

```bash
supergravity status
# Shows: Skills | 12 installed | path
```
