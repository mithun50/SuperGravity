---
name: scaffold
description: Generate complete project structures
category: workflow
mcp-servers: [context7]
agents: [fullstack, devops]
---

# /sg:scaffold - Project Scaffolding

> **Context Framework Note**: Generates production-ready project structures.

## Triggers
- `/sg:scaffold [type] [name] [--flags]`
- New project requests
- Project generation needs

## Syntax
```
/sg:scaffold [template] [project-name] [options]

Templates:
  nextjs      Next.js with App Router
  react       React with Vite
  fastapi     Python FastAPI
  express     Node.js Express
  fullstack   Next.js + API

Options:
  --with-prisma    Add Prisma ORM
  --with-auth      Add authentication
  --with-docker    Add Docker configs
  --with-ci        Add GitHub Actions
  --database postgres|mysql|sqlite
```

## Behavioral Flow

1. **Detect** - Identify template and options
2. **Generate** - Create directory structure
3. **Configure** - Set up configs and dependencies
4. **Initialize** - Create base files
5. **Document** - Generate README

## Templates

### Next.js
```
project/
├── src/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── types/
├── public/
├── package.json
├── tsconfig.json
└── tailwind.config.js
```

### FastAPI
```
project/
├── app/
│   ├── api/v1/
│   ├── core/
│   ├── models/
│   └── main.py
├── tests/
├── pyproject.toml
└── Dockerfile
```

## Examples

### Next.js SaaS
```
/sg:scaffold nextjs my-saas --with-prisma --with-auth --with-docker
```

### FastAPI Backend
```
/sg:scaffold fastapi my-api --database postgres --with-ci
```

### Full-Stack App
```
/sg:scaffold fullstack my-app --with-prisma --with-auth --with-docker --with-ci
```

## Outputs
- Complete project structure
- Configured dependencies
- Docker and CI files
- README with setup instructions

## Boundaries
**Will:** Generate production-ready scaffolds
**Won't:** Create incomplete or placeholder code
