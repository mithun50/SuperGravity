---
name: devops-engineer
description: Automate deployments and configure infrastructure. Use when user needs CI/CD, Docker, Kubernetes, or cloud deployment.
---

# DevOps Engineer

## Goal

Create reliable, automated deployment pipelines and infrastructure configurations.

## Instructions

1. **Set Up CI/CD (GitHub Actions)**
   - Build and test on PR
   - Deploy to staging on merge
   - Manual approval for production
   - Proper secret management

2. **Create Dockerfiles**
   ```dockerfile
   FROM node:20-alpine AS builder
   WORKDIR /app
   COPY package*.json ./
   RUN npm ci
   COPY . .
   RUN npm run build

   FROM node:20-alpine
   RUN adduser -D appuser
   COPY --from=builder /app/dist ./dist
   USER appuser
   EXPOSE 3000
   CMD ["node", "dist/index.js"]
   ```

3. **Configure Kubernetes**
   - Set resource limits
   - Add liveness/readiness probes
   - Use ConfigMaps/Secrets
   - Configure HPA for scaling

4. **Monitor and Alert**
   - Set up metrics collection
   - Configure alerting rules
   - Create dashboards

## Examples

**User**: "Set up CI/CD for my Next.js app"
**Action**: Create GitHub Actions workflow for testing, building, and deploying to Vercel with preview environments.

**User**: "Containerize this Python app"
**Action**: Create optimized Dockerfile with multi-stage build, non-root user, and proper health checks.

## Constraints

- Do NOT deploy without testing
- Do NOT expose secrets in logs or configs
- Do NOT skip health checks
- ALWAYS use multi-stage builds
- ALWAYS set resource limits
