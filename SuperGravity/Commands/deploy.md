---
name: deploy
description: Deploy applications to various platforms
category: workflow
agents: [devops]
---

# /sg:deploy - Deployment

> **Context Framework Note**: Automates deployment to cloud platforms.

## Triggers
- `/sg:deploy [target] [--flags]`
- Deployment requests
- CI/CD setup needs

## Syntax
```
/sg:deploy [environment] [options]

Environments:
  staging       Deploy to staging
  production    Deploy to production
  preview       Create preview deploy

Options:
  --dry-run     Preview without deploying
  --force       Skip confirmations
  --rollback    Rollback last deploy
  --artifact    Create deploy artifact
```

## Behavioral Flow

1. **Check** - Verify build and tests pass
2. **Plan** - Show what will be deployed
3. **Confirm** - Get approval (unless --force)
4. **Deploy** - Execute deployment
5. **Verify** - Health check
6. **Report** - Deployment artifact

## Platform Support

### Vercel
```bash
# Auto-detected from vercel.json
vercel deploy --prod
```

### Docker/K8s
```bash
docker build -t app:latest .
kubectl apply -f k8s/
```

### GitHub Actions
```yaml
# Generated workflow
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
      - run: npm run deploy
```

## Examples

### Deploy to Staging
```
/sg:deploy staging
```

### Preview Deploy
```
/sg:deploy preview --artifact
```

### Production (Careful!)
```
/sg:deploy production --dry-run
# Review, then:
/sg:deploy production
```

### Rollback
```
/sg:deploy --rollback
```

## Safety Checks
- Tests must pass
- Build must succeed
- Staging before production
- Approval for production

## Outputs
- Deployment logs
- Health check results
- Deployment artifact
- Rollback instructions

## Boundaries
**Will:** Deploy safely with proper checks
**Won't:** Deploy broken code, skip approvals
