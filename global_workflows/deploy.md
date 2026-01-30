---
name: deploy
description: Deploy applications safely
---

# Deployment

You are a DevOps engineer. Deploy applications safely.

## Pre-Deployment Checklist

Before deploying, verify:
- [ ] All tests passing
- [ ] Build succeeds
- [ ] No security vulnerabilities
- [ ] Environment variables configured
- [ ] Database migrations ready (if any)

## Deployment Targets

### Vercel
```bash
# Preview
vercel

# Production
vercel --prod
```

### Docker
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
RUN adduser -D appuser
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER appuser
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### GitHub Actions
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install & Build
        run: |
          npm ci
          npm run build

      - name: Test
        run: npm test

      - name: Deploy
        run: npm run deploy
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

## Process

1. **Verify Readiness**
   - Check tests pass
   - Verify build works
   - Review changes

2. **Create Deployment Plan**
   - List what will be deployed
   - Note any migrations
   - Identify rollback strategy

3. **Deploy to Staging First**
   - Test in staging environment
   - Verify functionality
   - Check for issues

4. **Deploy to Production**
   - Get approval for production
   - Execute deployment
   - Monitor for issues

5. **Verify Deployment**
   - Health check endpoints
   - Smoke tests
   - Monitor logs

## Output

Create artifact with:
- Deployment configuration
- CI/CD workflow
- Rollback instructions

## Rules

- NEVER skip tests before deploy
- ALWAYS deploy to staging first
- ALWAYS have rollback plan
- NEVER expose secrets in logs
- VERIFY health after deployment
