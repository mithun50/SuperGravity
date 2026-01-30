---
description: Deploy applications safely with proper checks and rollback plans
---

1. Ask the user for the deployment target (Vercel, Docker, AWS, Railway, etc.).

2. Verify pre-deployment checklist:
   - All tests passing
   - Build succeeds locally
   - No security vulnerabilities
   - Environment variables configured
   - Database migrations ready (if any)

// turbo
3. Run `npm test` or `pytest` to verify tests pass.

// turbo
4. Run `npm run build` to verify build succeeds.

5. Create deployment plan identifying:
   - What will be deployed
   - Required migrations
   - Rollback strategy

6. Generate deployment configuration for the target platform.

7. For Docker deployments, create optimized Dockerfile with:
   - Multi-stage build
   - Non-root user
   - Minimal base image

8. For CI/CD, create GitHub Actions workflow with:
   - Checkout and setup
   - Install dependencies
   - Run tests
   - Build application
   - Deploy with secrets

9. Deploy to staging environment first.

10. Verify staging deployment:
    - Health check endpoints
    - Smoke tests
    - Check logs for errors

11. Get user approval for production deployment.

12. Deploy to production environment.

13. Verify production deployment:
    - Health check endpoints
    - Monitor logs
    - Verify functionality

14. Document rollback procedure if issues arise.

## Rules
- NEVER skip tests before deploy
- ALWAYS deploy to staging first
- ALWAYS have rollback plan
- NEVER expose secrets in logs
- VERIFY health after deployment
