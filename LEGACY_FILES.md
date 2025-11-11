git init# Legacy Files Documentation

This document explains legacy files that have been replaced in the refactored architecture.

## app.py.legacy

**Original Location**: `./app.py` (root)
**Status**: Replaced by `backend/app.py`
**Date Deprecated**: October 2025

### Why it was replaced:

The original `app.py` in the root was part of the MVP monolithic architecture. It has been replaced by a microservices architecture with:

1. **backend/app.py** - FastAPI REST API with service layer
2. **worker/tasks.py** - RQ worker for async execution
3. **frontend/** - React + TypeScript frontend

### Key differences:

**Old (app.py.legacy)**:
- Synchronous execution (blocking)
- Direct Docker calls in endpoint
- No job queue
- No persistent storage
- Simple problem loading from `problems/` directory

**New (backend/app.py)**:
- Asynchronous with Redis Queue (RQ)
- Job-based execution with status tracking
- PostgreSQL persistence
- Service layer architecture
- Hierarchical problem organization (Subject → Unit → Problem)
- Security validation layer
- Structured logging
- Health checks

### Migration notes:

If you need to reference the old implementation:
- See `app.py.legacy` for the original simple API
- See `runner.py` for the original Docker execution logic

The new architecture is documented in `CLAUDE.md`.

---

**DO NOT USE app.py.legacy IN PRODUCTION**

This file is kept for historical reference only.