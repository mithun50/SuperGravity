---
name: performance-optimizer
description: Analyze and optimize application performance. Use when user has slow app, needs profiling, bundle optimization, or query tuning.
---

# Performance Optimizer

## Goal

Identify performance bottlenecks and implement data-driven optimizations.

## Instructions

1. **Measure First**
   - Establish baseline metrics
   - Profile before optimizing
   - Set performance budgets

2. **Key Metrics**

   **Web Vitals:**
   - LCP < 2.5s (Largest Contentful Paint)
   - FID < 100ms (First Input Delay)
   - CLS < 0.1 (Cumulative Layout Shift)

   **Backend:**
   - P50, P95, P99 latency
   - Requests per second
   - Error rate

3. **Frontend Optimization**
   - Code splitting
   - Lazy loading
   - Image optimization
   - Tree shaking
   - Caching strategies

4. **Backend Optimization**
   - Query optimization (EXPLAIN ANALYZE)
   - Connection pooling
   - Response caching
   - Async processing

5. **Database Optimization**
   - Add missing indexes
   - Rewrite slow queries
   - Use read replicas
   - Implement caching

## Examples

**User**: "My app is slow"
**Action**: Profile the application, identify bottlenecks, measure baseline, implement targeted optimizations, verify improvements.

**User**: "Reduce bundle size"
**Action**: Analyze bundle with webpack-bundle-analyzer, identify large dependencies, implement code splitting and lazy loading.

## Constraints

- Do NOT optimize prematurely
- Do NOT guess - always profile
- Do NOT sacrifice readability blindly
- ALWAYS measure before and after
- ALWAYS document trade-offs
