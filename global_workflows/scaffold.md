---
description: Generate complete project structures for various technology stacks
---

1. Ask the user what type of project they want to create (Next.js, React, Vue, FastAPI, Django, Express, etc.).

2. Detect and confirm requirements:
   - Frontend framework
   - Backend type
   - Database
   - Authentication
   - Deployment target

3. Generate the complete project structure with proper directory hierarchy.

// turbo
4. Run `mkdir -p src tests docs` to create base directories.

5. Create package.json or pyproject.toml with all required dependencies.

6. Set up TypeScript configuration (tsconfig.json) for JavaScript projects.

7. Create ESLint and Prettier configuration files.

// turbo
8. Run `git init` to initialize git repository.

9. Generate .gitignore with proper entries for the stack.

10. Create .env.example with documented environment variables.

11. Set up Docker configuration (Dockerfile and docker-compose.yml).

12. Create CI/CD workflow file (.github/workflows/ci.yml).

13. Generate base application files with proper error handling.

14. Set up database configuration and migrations if requested.

15. Add authentication boilerplate if requested.

16. Create basic test structure with sample tests.

17. Generate README.md with setup instructions.
