# Legacy Files

These files represent the original MVP monolithic architecture before the microservices refactoring (Oct 2025).

## ⚠️ DO NOT USE THESE FILES IN PRODUCTION

This directory contains historical code preserved for reference only.

## Files

### `app.py` (previously `app.py.legacy`)
Original monolithic FastAPI application. This has been replaced by:
- `backend/app.py` - FastAPI REST API
- `worker/tasks.py` - RQ worker for job processing
- `backend/services/` - Service layer architecture

### `runner.py`
Original Docker execution logic (130 lines). Now replaced by:
- `worker/services/docker_runner.py` - Modern Docker execution with path translation
- `worker/tasks.py` - Job orchestration

### `Dockerfile.monolithic` (previously `Dockerfile`)
Original single-container Dockerfile. Now replaced by:
- `backend/Dockerfile` - Backend service container
- `worker/Dockerfile` - Worker service container
- `frontend/Dockerfile` - Frontend service container
- `runner/Dockerfile` - Minimal sandbox container

### `requirements.txt`
Original monolithic dependencies. Now replaced by:
- `backend/requirements.txt` - Backend dependencies
- `worker/requirements.txt` - Worker dependencies
- Each service has its own isolated dependencies

## Migration History

**October 25, 2025**: Microservices refactoring completed
- Separated concerns into backend, worker, frontend services
- Implemented service layer architecture
- Added structured logging and validation
- Migrated to Pydantic v2 schemas

**November 10, 2025**: Legacy files moved to this directory
- Cleaned up root directory structure
- Improved architectural clarity

## References

See `LEGACY_FILES.md` in the root directory for detailed migration notes and rationale.
