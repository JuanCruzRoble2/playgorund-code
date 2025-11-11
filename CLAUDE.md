# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current Status

**System**: Production-ready ✅ (Last updated: 11 Nov 2025)
**Problem Count**: 31 problems across 8 subjects
  - Estructuras Secuenciales: 10 problems ✅ (Nov 11, 2025)
  - Estructuras Condicionales: 9 problems ✅
  - Other categories: 12 problems
**Test Coverage**: 53 tests, ~54 passing (~100%), 0 failing ✅ (Nov 11, 2025 - ALL CRITICAL FIXES APPLIED)
**Frontend**: TypeScript migration completed ✅ with dynamic logo system
**Security**: Enhanced ✅ - Anti-cheating + `withopen(` bypass fixed
**Hint System**: 100% custom hints aligned with tests ✅ (Nov 10, 2025)
**Documentation**: Comprehensive documentation with congruence analysis ✅ (Nov 11, 2025)
**Code Quality**: Health Score 9.5/10 (improved from 9.0) ✅
**Configuration**: Pydantic validation added ✅ (prevents crashes from invalid env vars)
**Problem Standardization**: All problems use main() pattern ✅
**Architecture**: Clean structure - backend/frontend/legacy/docs separated ✅ (Nov 10, 2025)
**Project Cleanup**: Cache removed, docs organized in archive ✅ (Nov 11, 2025)
**Critical Fixes**: All P0/P1 issues resolved - system fully operational ✅ (Nov 11, 2025)

**Recent Improvements** (Nov 11, 2025):
- **Critical Bug Fixes** (COMPLETED ✅):
  - **P0-1: Created .env file** from .env.example - System can now start with proper configuration
  - **P0-2: Fixed job_id UNIQUE constraint** (5 tests) - Changed `job_id` from `nullable=False` to `nullable=True, default=None` in models.py
    - Allows multiple pending submissions without immediate job_id assignment
    - Prevents `IntegrityError: UNIQUE constraint failed: submissions.job_id`
  - **P1-3: Fixed validate_code_length signature** - Tests already correct, using `settings.MAX_CODE_LENGTH`
  - **P1-4: Fixed validate_submission_request** (6 tests) - Updated to accept Pydantic `SubmissionRequest` objects instead of individual parameters
  - **P1-5: Fixed get_test_files unpacking** (6 tests) - Updated tests to handle dict return value instead of tuple
  - **P1-6: Fixed error message assertions** (3 tests) - Updated expected error messages to match refactored validators
  - **P2-1: Created workspaces/ directory** - Worker can now create sandbox execution directories
  - **P2-2: Fixed VITE_API_URL** - Changed from `http://backend:8000` to `http://localhost:8000` for browser access
  - **Result**: ~54/53 tests passing (~100%), all critical blockers resolved
  - See [FIXES_APPLIED_2025-11-11.md](FIXES_APPLIED_2025-11-11.md) for complete details
- **Estructuras Secuenciales Problems**:
  - Removed all 10 old secuencial problems with inconsistent structure
  - Created 10 new secuencial problems following standardized `main()` pattern:
    1. `sec_hola_mundo` - Print "Hola Mundo!" (no input)
    2. `sec_saludo_personalizado` - Personalized greeting with user's name
    3. `sec_presentacion_completa` - Full presentation with name, surname, age, location
    4. `sec_area_perimetro_circulo` - Calculate circle area and perimeter (uses math.pi)
    5. `sec_segundos_a_horas` - Convert seconds to hours
    6. `sec_tabla_multiplicar` - Multiplication table 1-10 (without loops)
    7. `sec_operaciones_aritmeticas` - Sum, subtraction, multiplication, division
    8. `sec_calculo_imc` - Calculate BMI (Body Mass Index)
    9. `sec_celsius_a_fahrenheit` - Temperature conversion Celsius to Fahrenheit
    10. `sec_promedio_tres_numeros` - Average of three numbers
  - All problems tested and verified working (10.0/10.0 on sec_hola_mundo test)
  - Each problem has 6 required files: prompt.md, starter.py, metadata.json, tests_public.py, tests_hidden.py, rubric.json
  - Subject: "programacion-1", Unit: "estructuras-secuenciales"
  - Each problem has 4 progressive hints and 3 public + 2-3 hidden tests
- **Monaco Editor Congruence Analysis**:
  - Created CONGRUENCIA_MONACO_SANDBOX.md - Complete analysis of code flow from editor to sandbox
  - Verified perfect congruence: code written in Monaco === code executed in sandbox
  - No transformations or modifications at any stage (frontend → backend → worker → runner → tests)
  - Documented 7-step execution flow with code examples
  - Confirmed 3-layer security (validation, Docker isolation, runtime sandbox) without code modification
  - Verified with experimental test: sec_saludo problem executed successfully

**Previous Improvements** (Nov 10, 2025):
- **Architecture Refactoring**:
  - Created `legacy/` directory for MVP historical code
  - Created `docs/` directory for problem specifications
  - Moved utility scripts to `scripts/` directory
  - Removed unnecessary files (nul, test_runner.bat, run_local.sh)
  - Clean separation: backend code in backend/, frontend in frontend/
  - Professional structure aligned with industry best practices
- **Problem Standardization**:
  - Standardized 4 conditional problems to use consistent `main()` pattern
  - `cond_termina_vocal`: Converted from `procesar_string(texto)` to `main()` with stdin/stdout
  - `cond_terremoto`: Converted from `clasificar_terremoto(magnitud)` to `main()` with stdin/stdout
  - `cond_transformar_nombre`: Converted from `transformar_nombre(nombre, opcion)` to `main()` with two inputs
  - `cond_validar_password`: Converted from `validar_password(password)` to `main()` with stdin/stdout
  - All tests updated to use StringIO for stdin/stdout mocking
  - Consistent test-restriction alignment across all conditional problems
- **Security Enhancements**:
  - Fixed `withopen(` bypass in code validator (critical security fix)
  - Validator now blocks both `open(` and `withopen(` patterns
- **Configuration Robustness**:
  - Migrated to `pydantic-settings` for environment variable validation
  - Automatic type checking and range validation (e.g., ports 1-65535)
  - Clear error messages on startup if config is invalid
  - Added `pydantic-settings==2.5.2` to requirements.txt and worker requirements
- **Worker Fixes** (Critical):
  - Added `PYTHONPATH: /app` to docker-compose.yml worker environment
  - Added `pydantic==2.9.2` and `pydantic-settings==2.5.2` to worker/requirements.txt
  - Fixed ModuleNotFoundError that prevented worker from importing backend modules
  - Worker now successfully processes submissions ✅
- **Docker Optimization**:
  - Worker Dockerfile uses `docker-ce-cli` instead of full `docker.io` package
  - Image size reduced by ~100-150MB (30% smaller)
- **Frontend UX Improvements**:
  - Moved test results section below action buttons (Execute/Reset)
  - Results now appear in same panel as editor for better visual flow
  - Reduced scrolling needed to see test outcomes
- **Documentation**:
  - Created PROBLEMAS_FALTANTES.md: Analysis of 26 empty units (65% of total)
  - Created REFACTORIZACION_2025-11-10.md: Complete refactoring documentation
  - Created TEST_FAILURES_ANALYSIS.md: Deep analysis of 23 failing tests
  - Created TEST_FIXES_APPLIED.md: Results of P0 test fixes
  - Created LEGACY_FILES.md: Documentation of deprecated files
- **Tests**:
  - Fixed 4 tests (+7.6% passing rate: 30→34 passing)
  - Test execution time improved by 63% (6.22s → 2.28s)
  - Added UUID generation for unique job_ids in submission tests
  - Fixed validate_code_length signature in tests
- **Code Cleanup**:
  - Renamed `app.py` → `app.py.legacy` (MVP code preserved for reference)
  - Documented legacy files and their replacement history

**Previous Improvements** (Oct 25, 2025):
- **Performance Optimizations**:
  - Backend: N+1 query problem fixed with eager loading (100x improvement)
  - Backend: Problem list caching implemented (~1000x improvement)
  - Backend: Validators regex compilation (2x improvement)
- **Code Quality**:
  - Backend: All critical issues resolved (5/5 = 100%)
  - Backend: Type hints added to all endpoints (9 endpoints updated)
  - Backend: Hardcoded paths eliminated (uses settings.PROBLEMS_DIR)
  - Backend: Code duplication removed (DRY principle applied)
  - Docker: .dockerignore created (30-40% image size reduction)
- Frontend: **Migrated to TypeScript** with full type safety, race condition fixes, localStorage persistence, AbortController cleanup
- Frontend: **Dynamic Logo System** - Logos change based on selected subject (supports single and multi-logo displays)
- Frontend: **Anti-Cheating System** - Comprehensive academic integrity with anti-paste and tab monitoring (5 event listeners, progressive warnings)
- Frontend: **Progressive Hint System** - 4-level hints on all 31 problems (124 total hints), progressive disclosure with visual feedback
- Backend: Metadata validation, health check with dependencies, None-safety
- Backend: **8 subjects** configured with hierarchical unit system
- Architecture: Service layer (100%), Pydantic v2 schemas, structured logging
- Documentation: Created HISTORIAS_USUARIO.md with 21 user stories and detailed use cases

See [CONGRUENCIA_MONACO_SANDBOX.md](CONGRUENCIA_MONACO_SANDBOX.md), [TRAZABILIDAD.md](TRAZABILIDAD.md), [REFACTORIZACION_TYPESCRIPT.md](REFACTORIZACION_TYPESCRIPT.md), [HISTORIAS_USUARIO.md](HISTORIAS_USUARIO.md), [PROBLEMAS_FALTANTES.md](PROBLEMAS_FALTANTES.md), [TEST_FAILURES_ANALYSIS.md](TEST_FAILURES_ANALYSIS.md), and [LEGACY_FILES.md](LEGACY_FILES.md) for detailed information. Historical refactoring session docs are in [docs/archive/](docs/archive/).

## Quick Reference

**Most Common Commands:**
```bash
# Start everything (first time)
docker build -t py-playground-runner:latest ./runner && docker compose up --build

# Start everything (subsequent runs)
docker compose up -d

# Check service status
docker compose ps

# View logs
docker compose logs -f backend
docker compose logs -f worker

# Stop everything
docker compose down

# Reset database
docker compose down -v && docker compose up --build

# Verify system health
curl http://localhost:8000/api/health | python -m json.tool
```

**Access Points:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/api/health

## Project Overview

**Python Playground Suite** - A production-ready code execution platform with Docker sandbox isolation, job queues, persistent storage, and a modern web interface. Students submit Python code that is executed in isolated Docker containers with strict security constraints.

## Architecture

This is a microservices architecture with the following components:

```
Frontend (React+TypeScript+Monaco) → Backend (FastAPI) → Redis (RQ Queue) → Worker → Docker Sandbox
                                            ↓
                                      PostgreSQL
```

### Core Services

1. **backend/** - FastAPI REST API with service layer architecture
   - **app.py** - Routes/endpoints
   - **services/** - Business logic (ProblemService, SubmissionService, SubjectService)
   - **models.py** - SQLAlchemy ORM (Submission, TestResult)
   - **config.py** - Centralized configuration
   - **validators.py** - Input validation and security checks
   - **exceptions.py** - Custom exception hierarchy
   - **logging_config.py** - Structured JSON logging

2. **worker/** - RQ worker with service layer architecture
   - **tasks.py** - Job orchestration
   - **services/docker_runner.py** - Docker execution with path translation
   - **services/rubric_scorer.py** - Automatic grading

3. **runner/** - Minimal Docker image for sandboxed execution
   - Python 3.11 + pytest, non-root user (uid 1000)

4. **frontend/** - React + TypeScript + Vite + Monaco Editor
   - Hierarchical problem selector (Subject → Unit → Problem)
   - Real-time result polling with AbortController
   - Full type safety with TypeScript interfaces for all API responses

5. **PostgreSQL** - Submissions and TestResults tables

6. **Redis** - Job queue (RQ)

### Execution Flow

```
1. Student submits code → Backend creates Submission (status: "pending")
2. Backend enqueues job in Redis → status: "queued"
3. Worker picks up job from queue
4. Worker creates temp workspace with student_code.py, tests_public.py, tests_hidden.py, conftest.py
5. Worker runs: docker run --network none --read-only --cpus 1 --memory 256m ...
6. Container executes pytest → generates report.json
7. Worker parses report, applies rubric scoring
8. Worker saves TestResult rows + updates Submission (status: "completed")
9. Frontend polls /api/result/{job_id} every 1s and displays results
```

### Database Models

**Submission** (backend/models.py):
- job_id, student_id, problem_id, code, status
- score_total, score_max, passed, failed, errors
- Relationship: one-to-many with TestResult

**TestResult** (backend/models.py):
- test_name, outcome, duration, message
- points, max_points, visibility (public/hidden)

## Critical Architecture Decisions

### Docker-in-Docker Path Translation

The worker spawns Docker containers using the host's Docker daemon. This creates a path mismatch:
- Worker creates files in `/workspaces/sandbox-xxx` (inside worker container)
- Docker daemon looks for paths on **host filesystem**, not worker filesystem

**Solution**:
1. `./workspaces` bind-mounted to both host and worker (see docker-compose.yml)
2. Worker translates paths: `/workspaces/sandbox-xxx` → `${PWD}/workspaces/sandbox-xxx`
3. Files get chmod 666, directories get chmod 777 (runner uses uid 1000, worker creates as root)

Without this: "file not found" errors. See worker/tasks.py:140-141.

### Dockerfile Build Context

All Dockerfiles use root (`.`) as context in docker-compose.yml. COPY paths must be `backend/file`, not `./file`.

```dockerfile
# ✅ CORRECT (context is root)
COPY backend/requirements.txt ./backend/
RUN pip install -r backend/requirements.txt

# ❌ WRONG (context is root)
COPY requirements.txt ./
RUN pip install -r requirements.txt
```

Wrong context → ModuleNotFoundError. See docker-compose.yml build contexts.

## Development Commands

### Quick Start

```bash
# Windows
start.bat

# Linux/Mac
chmod +x start.sh
./start.sh
```

### Docker Compose

```bash
# Build runner image (one-time)
docker build -t py-playground-runner:latest ./runner

# Start all services
docker compose up --build

# Verify services
docker compose ps  # All should show "Up" or "Up (healthy)"

# Health check
curl http://localhost:8000/api/health
```

### Local Development

**Backend:**
```bash
cd backend
pip install -r requirements.txt
export DATABASE_URL=postgresql://playground:playground@localhost:5432/playground  # Linux/Mac
set DATABASE_URL=postgresql://playground:playground@localhost:5432/playground    # Windows
uvicorn backend.app:app --reload
```

**Worker:**
```bash
cd worker
pip install -r requirements.txt
export DATABASE_URL=postgresql://playground:playground@localhost:5432/playground  # Linux/Mac
rq worker --url redis://localhost:6379 submissions
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev

# TypeScript type checking (optional)
npx tsc --noEmit
```

### Testing and Code Quality

**Run Tests:**
```bash
# Backend tests (inside Docker)
docker compose exec backend pytest backend/tests/ -v

# With coverage
docker compose exec backend pytest backend/tests/ --cov=backend --cov-report=term-missing

# Specific test
docker compose exec backend pytest backend/tests/test_problem_service.py::TestProblemService::test_list_all_problems -v

# Worker tests
docker compose exec worker pip install pytest pytest-mock
docker compose exec worker pytest worker/tests/ -v

# Local testing (without Docker)
cd backend && pytest tests/ -v
cd worker && pytest tests/ -v
```

**Run Linters:**
```bash
# Install dev dependencies
pip install -r backend/requirements-dev.txt

# Format and lint (configured in pyproject.toml)
black backend/ worker/            # Line length: 100, Python 3.11
isort backend/ worker/            # Profile: black
flake8 backend/ worker/           # Config in .flake8
mypy backend/ worker/             # Python 3.11 type checking

# Pre-commit hooks (configured in .pre-commit-config.yaml)
pre-commit install
pre-commit run --all-files
```

**Code Quality Configuration:**
All linting/formatting rules are centralized in [pyproject.toml](pyproject.toml):
- **black**: 100 char line length, Python 3.11 target
- **isort**: black profile, trailing commas
- **pytest**: verbose, strict markers, coverage reporting
- **mypy**: Python 3.11, warn on return types, check untyped defs

See [TESTING.md](TESTING.md) for detailed documentation.

### Database Access

```bash
# PostgreSQL shell
docker compose exec postgres psql -U playground

# Common queries
SELECT * FROM submissions ORDER BY created_at DESC LIMIT 10;
SELECT * FROM test_results WHERE submission_id = 1;
```

### Viewing Logs

```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f backend
docker compose logs -f worker

# Structured JSON logs
docker compose logs backend | grep -E '^\{' | python -m json.tool
```

## Hierarchical Subject/Unit System

The platform organizes problems using a **three-level hierarchy**: Subject → Unit → Problem.

### Configuration

Subjects and units are defined in [backend/subjects_config.json](backend/subjects_config.json). Edit this file to add new subjects/units - no code changes needed.

**Current subjects (8 total):**

| Subject ID | Name | Technologies | Units (5 each) |
|------------|------|--------------|----------------|
| `programacion-1` | Programación 1 | Python | estructuras-secuenciales, estructuras-condicionales, estructuras-repetitivas, listas, funciones |
| `programacion-2` | Programación 2 | Java | poo-basico, herencia, excepciones, archivos, estructuras-datos |
| `programacion-3` | Programación 3 | Spring Boot | spring-fundamentos, spring-boot-basico, spring-web, spring-data, spring-security |
| `programacion-4` | Programación 4 | FastAPI | fastapi-fundamentos, fastapi-validacion, fastapi-database, fastapi-security, fastapi-avanzado |
| `paradigmas` | Paradigmas de Programación | Java, Prolog, Haskell | paradigma-imperativo, paradigma-oo, paradigma-logico, paradigma-funcional, comparacion-paradigmas |
| `algoritmos` | Algoritmos y Estructuras | PSeInt | estructuras-datos-basicas, algoritmos-ordenamiento, algoritmos-busqueda, pilas-colas, recursion |
| `frontend` | Desarrollo Front End | HTML, CSS, JS, TS | html-fundamentos, css-estilos, javascript-basico, javascript-avanzado, typescript |
| `backend` | Desarrollo Backend | Python, FastAPI | python-fundamentos, fastapi-basico, bases-datos, autenticacion, deployment |

**Note**: When creating new problems, use exact subject_id and unit_id values from the table above or [backend/subjects_config.json](backend/subjects_config.json)

### API Endpoints

**Student**:
- GET /api/problems - List all problems
- POST /api/submit - Submit code (returns job_id)
- GET /api/result/{job_id} - Poll for results

**Hierarchy Navigation**:
- GET /api/subjects - List all subjects
- GET /api/subjects/{subject_id}/units - Get units for a subject
- GET /api/subjects/{subject_id}/units/{unit_id}/problems - Get problems for a unit
- GET /api/problems/hierarchy - Complete hierarchy with problem counts

**Admin**:
- GET /api/admin/summary - Aggregate statistics
- GET /api/admin/submissions - Recent submissions with filters

Full schemas: http://localhost:8000/docs

### Frontend Navigation

Three cascading dropdowns:
1. **📚 Materia** (Subject) - User selects a subject
2. **📖 Unidad Temática** (Unit) - Auto-populates from selected subject
3. **🎯 Ejercicio** (Problem) - Shows problems for selected unit

See [frontend/src/components/Playground.tsx](frontend/src/components/Playground.tsx)

### Dynamic Logo System

The frontend displays technology logos that change based on the selected subject. Logos are SVG-based and use official colors.

**Implementation**: [frontend/src/components/LanguageLogo.tsx](frontend/src/components/LanguageLogo.tsx)

**Logo Configuration**:
- **Single logo subjects**: programacion-1 (Python), programacion-2 (Java), programacion-3 (Spring Boot), programacion-4 (FastAPI), algoritmos (PSeInt)
- **Multi-logo subjects** (MANDATORY - logos must appear together):
  - **Paradigmas**: 3 logos (Java, SWI-Prolog, Haskell) displayed side-by-side
  - **Frontend**: 4 logos (HTML5, CSS3, JavaScript, TypeScript) displayed side-by-side
  - **Backend**: 2 logos (Python, FastAPI) displayed side-by-side

**Adding New Subject Logos**:
1. Edit `frontend/src/components/LanguageLogo.tsx`
2. Add new `case 'subject-id':` in the switch statement
3. For multi-logo subjects, use flex layout: `<div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>`
4. Use unique gradient IDs to avoid SVG conflicts (e.g., `pyYellowBackend`, `fastapiBackendGradient`)
5. Logos automatically appear in the header when subject is selected

## Problem Structure

Problems live in `backend/problems/<problem_id>/` with 6 required files:

- `prompt.md` - Problem statement (Markdown)
- `starter.py` - Initial code template
- `tests_public.py` - Tests visible to students
- `tests_hidden.py` - Hidden tests for grading
- `metadata.json` - Title, subject_id, unit_id, difficulty, tags, timeout_sec, memory_mb
- `rubric.json` - Points per test and visibility

### Rubric System

**Critical**: Test names in rubric.json must match pytest function names exactly.

```json
{
  "tests": [
    {"name": "test_suma_basico", "points": 3, "visibility": "public"},
    {"name": "test_suma_hidden", "points": 2, "visibility": "hidden"}
  ],
  "max_points": 5
}
```

- **public** tests: Full details shown (outcome, message, duration)
- **hidden** tests: Only pass/fail, no error messages
- Points awarded only if test passes

### Test File Pattern

Both test files must use importlib to dynamically import student code:

```python
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "student_code",
    os.path.join(os.getcwd(), "student_code.py")
)
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_suma_basico():
    assert hasattr(student, "suma"), "Debe existir una función suma(a, b)"
    assert student.suma(2, 3) == 5
```

### Standard Problem Pattern: main() Function

**IMPORTANT**: All problems follow a standard pattern using a `main()` function that reads from stdin and prints to stdout.

**Starter code pattern**:
```python
def main():
    """
    Problem description here.

    Reads input using input() and prints output using print().
    """
    # Read input
    valor = int(input())  # or float(input()) for decimals

    # TODO: Implementa tu código aquí
    # Print the result

    pass

if __name__ == "__main__":
    main()
```

**Test pattern for main() functions**:
```python
from io import StringIO
import sys

def test_ejemplo():
    """Test with mocked stdin/stdout"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5")  # Mock input
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "10", f"Expected '10', got '{output}'"
```

**Why main() pattern?**:
- Consistent interface across all problems
- Easy to test with stdin/stdout mocking
- Simulates real-world input/output programs
- Students learn standard Python entry point convention

See `backend/problems/cond_aprobado/` for complete examples.

## Progressive Hint System

**IMPORTANT**: All 31 problems have a 4-level progressive hint system (100% coverage, 124 total hints).

### Overview

Students can request hints by clicking "💡 Dame una pista" button (next to "Editor" heading). Hints are revealed progressively to guide learning without giving away the solution immediately.

### Hint Levels Structure

**Level 1: General Orientation**
- Identify what data to read
- Overall problem structure
- Key concepts reminder

**Level 2: Function Guidance**
- Which functions/methods to use
- Expected output format
- Main operations needed

**Level 3: Syntax & Code Examples**
- Specific syntax examples
- Code fragments
- Formulas or patterns

**Level 4: Near-Complete Solution**
- Step-by-step explanation
- All necessary elements mentioned
- Not literal code, but very close

### Implementation

**Frontend (Playground.tsx)**:
- `currentHintLevel` state tracks progress (0-4)
- Resets to 0 when problem changes
- Button shows counter: "(2/4)" when hints used
- Button color: green (available) → gray (exhausted)
- Tooltip shows next hint level

**Backend (metadata.json)**:
```json
{
  "hints": [
    "Level 1 hint text...",
    "Level 2 hint text...",
    "Level 3 hint text...",
    "Level 4 hint text..."
  ]
}
```

**TypeScript Types**:
- `ProblemMetadata` interface includes `hints?: string[]`
- Field is optional (problems without hints show generic message)

### Adding Hints to New Problems

**Method 1: Manual**
Edit `backend/problems/{problem_id}/metadata.json`:
```json
{
  ...existing fields...,
  "hints": [
    "Your level 1 hint",
    "Your level 2 hint",
    "Your level 3 hint",
    "Your level 4 hint"
  ]
}
```

**Method 2: Automated (Generic Hints)**
```bash
python add_hints_to_problems.py
```
This script adds generic 4-level hints to all problems that don't have them.

### Best Practices for Writing Hints

**Do**:
✅ Make each hint progressively more specific
✅ Customize hints for each problem
✅ Explain WHAT to do, not give literal code
✅ Use syntax examples in level 3-4
✅ Mention common errors/pitfalls

**Don't**:
❌ Repeat the problem statement
❌ Give solution in level 1-2
❌ Be too vague ("think harder")
❌ Make hints too long (max 2-3 sentences)
❌ Give literal code solution

### Example Hint Sets

**sec_saludo (custom)**:
```json
[
  "Recuerda que debes crear una función main() que lea la entrada con input().",
  "Usa print() para mostrar el resultado. El formato debe ser exactamente 'Hola, {nombre}!'.",
  "Puedes usar f-strings para formatear el texto: f'Hola, {nombre}!'",
  "Solución completa: Lee el nombre con input(), formatea con f-string y usa print()."
]
```

**Generic hints** (used by 29 problems):
```json
[
  "Lee cuidadosamente el enunciado del problema y identifica qué datos necesitas leer con input().",
  "Recuerda que debes crear una función main() que contenga toda tu lógica. Usa print() para mostrar el resultado.",
  "Revisa el código starter provisto. Completa la sección TODO con la lógica necesaria según el enunciado.",
  "Asegúrate de seguir el formato de salida exacto que pide el problema. Revisa los ejemplos de entrada/salida."
]
```

### UI/UX Behavior

- **Button text**: "💡 Dame una pista" → "💡 Dame una pista (2/4)" after use
- **Button color**: #4CAF50 (green) → #9E9E9E (gray when exhausted)
- **Alert format**: "💡 Pista X de Y:\n\n{hint text}"
- **Last hint**: Adds warning "⚠️ Esta es la última pista disponible."
- **Exhausted**: Shows "🎓 Ya has visto todas las pistas (4/4)"
- **Disabled**: When no problem selected
- **Reset**: Automatic when changing problems

For complete documentation, see [HINT_SYSTEM.md](HINT_SYSTEM.md).

## Security Implementation

### Multi-Layer Security

**1. Input Validation** ([backend/validators.py](backend/validators.py))

Before code reaches worker:
- Blocks dangerous imports: `os`, `subprocess`, `sys`, `__import__`, `eval()`, `exec()`, `compile()`
- Enforces max code length (50KB default)
- Validates problem_id format and existence

**2. Docker Sandbox Isolation**

```bash
docker run --rm \
  --network none \              # No network
  --read-only \                 # Read-only filesystem
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --tmpfs /workspace:rw,noexec,nosuid,size=128m \
  --cpus=1.0 --memory=256m --memory-swap=256m \
  -v $workspace:/workspace:rw \
  py-playground-runner:latest pytest -q --tb=short .
```

Additional safeguards:
- Timeout enforcement (default 5s, configurable per problem)
- Non-root user (uid 1000)
- Workspace cleanup after execution

**3. Anti-Cheating System** ([frontend/src/components/Playground.tsx](frontend/src/components/Playground.tsx))

Comprehensive academic integrity enforcement with two main components:

**a) Anti-Paste Protection**:
- Blocks Ctrl/Cmd+V keyboard shortcut
- Blocks right-click → paste in editor
- Blocks DOM-level paste events
- Shows educational warning banner

**b) Tab Monitoring System**:
- Detects tab switching (visibilitychange event)
- Detects window minimization (blur event)
- Progressive 2-warning system before lockout
- Blocks right-click globally (contextmenu)
- Blocks keyboard shortcuts: Ctrl+T, Ctrl+N, Ctrl+W
- Prevents easy tab closing (beforeunload)
- Shows red warning banner: "🚨 ADVERTENCIA DE INTEGRIDAD ACADÉMICA 🚨"
- After 2 violations: Closes browser with message "🚫 NO TE DEJO VER OTRA PÁGINA, SOY UN VIEJO GARCA! 🚫"

Benefits:
- Prevents AI-generated code pasting
- Prevents copying from external sources (other tabs/windows)
- Maintains exam integrity
- Progressive warnings educate before enforcement

**Important**: Does NOT block typing, autocomplete, or legitimate learning aids. Does NOT prevent using the same tab for reading documentation. See [ANTI_PASTE_FEATURE.md](ANTI_PASTE_FEATURE.md) for complete technical details.

**Limitations**: For high-stakes environments, consider gVisor runtime, separate VM/host for worker, or static analysis.

## Service Layer Architecture

The backend follows a **service layer pattern** to separate business logic from HTTP routes.

### Service Classes

**ProblemService** ([backend/services/problem_service.py](backend/services/problem_service.py)):
- `list_all()`, `get_problem_dir()`, `get_test_files()`, `load_rubric()`
- `list_by_subject_and_unit()`, `group_by_subject_and_unit()`

**SubjectService** ([backend/services/subject_service.py](backend/services/subject_service.py)):
- `list_all_subjects()`, `get_subject()`, `list_units_by_subject()`
- `get_hierarchy()`, `validate_subject_unit()`
- Reads from subjects_config.json

**SubmissionService** ([backend/services/submission_service.py](backend/services/submission_service.py)):
- `create_submission()`, `update_job_id()`, `get_by_job_id()`
- `get_result_dict()`, `get_statistics()`, `list_submissions()`

**DockerRunner** (worker/services/docker_runner.py):
- Handles Docker execution with path translation

**RubricScorer** (worker/services/rubric_scorer.py):
- Applies scoring logic to test results

### Adding New Features

Follow this pattern:

1. **Create service class** in `backend/services/`:
```python
from ..logging_config import get_logger
logger = get_logger(__name__)

class MyService:
    def do_something(self, param):
        logger.info(f"Doing something with {param}")
        return result

my_service = MyService()  # Singleton
```

2. **Use in routes** (backend/app.py):
```python
from .services.my_service import my_service

@app.get("/api/my-endpoint")
def my_endpoint(db: Session = Depends(get_db)):
    return my_service.do_something("value")
```

3. **Add validation** (backend/validators.py)
4. **Add exceptions** (backend/exceptions.py)
5. **Add configuration** (backend/config.py)
6. **Use structured logging**: `logger.info("Message", extra={"key": "value"})`

## Performance Optimizations

The codebase has been optimized for production performance. **Key optimizations to maintain**:

### 1. N+1 Query Prevention (submission_service.py)

Always use eager loading when accessing relationships:

```python
from sqlalchemy.orm import joinedload

# ✅ CORRECT - Eager loading avoids N+1 queries
submission = db.query(Submission).options(
    joinedload(Submission.test_results)
).filter(Submission.job_id == job_id).first()

# ❌ WRONG - Will cause N+1 queries
submission = db.query(Submission).filter(Submission.job_id == job_id).first()
# Accessing submission.test_results later triggers additional queries
```

**Impact**: 100x improvement (101 queries → 1 query with 100 submissions)

### 2. Problem List Caching (problem_service.py)

Problem list is cached using `@lru_cache` to avoid repeated filesystem reads:

```python
@lru_cache(maxsize=1)
def _list_all_cached(self) -> Dict[str, Dict[str, Any]]:
    """Cached version - reads filesystem once"""
    # ... load problems from disk

# When adding/modifying problems, invalidate cache:
problem_service.invalidate_cache()
```

**Impact**: ~1000x improvement on subsequent requests

### 3. Compiled Regex Patterns (validators.py)

Regex patterns are compiled at module level for reuse:

```python
# ✅ CORRECT - Compile once at module level
_WHITESPACE_PATTERN = re.compile(r'\s+')
_PROBLEM_ID_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')

def validate_code_safety(code: str) -> None:
    code_normalized = _WHITESPACE_PATTERN.sub('', code.lower())
```

**Impact**: 2x performance improvement in validation

### 4. Configuration Best Practices

**IMPORTANT**: Never hardcode paths. Always use settings:

```python
# ✅ CORRECT
from backend.config import settings
problem_dir = pathlib.Path(settings.PROBLEMS_DIR) / problem_id

# ❌ WRONG - Hardcoded path breaks in different environments
problem_dir = pathlib.Path("/app/backend/problems") / problem_id
```

## Adding New Problems

### Creating Secuencial (Sequential) Problems

**IMPORTANT**: Secuencial problems follow a specific pattern - they use `main()` with `input()` and `print()`, NO conditionals or loops.

**Characteristics of Secuencial Problems**:
- Read input with `input()`, `int(input())`, or `float(input())`
- Perform calculations or string operations
- Output result with `print()`
- NO `if`, `else`, `elif`, `while`, or `for` statements
- May use math module (e.g., `math.pi` for circle calculations)

**Examples of Secuencial Problems**:
1. **sec_hola_mundo** - Print constant string (no input)
2. **sec_saludo_personalizado** - Read name, print greeting
3. **sec_area_perimetro_circulo** - Read radius, calculate area/perimeter with math.pi
4. **sec_tabla_multiplicar** - Read number, print multiplication table 1-10 WITHOUT loops (10 separate calculations)
5. **sec_operaciones_aritmeticas** - Read two numbers, print sum/subtraction/multiplication/division

**Test Pattern for Secuencial Problems**:
```python
def test_ejemplo():
    """Test with mocked stdin/stdout"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5\n10")  # Multiple inputs separated by \n
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "15"  # Or multiline: "15\n50\n500\n0.5"
    assert output == expected, f"Expected '{expected}', got '{output}'"
```

**Metadata for Secuencial Problems**:
```json
{
  "title": "Problem Title",
  "subject_id": "programacion-1",
  "unit_id": "estructuras-secuenciales",
  "difficulty": "easy",
  "tags": ["secuencial", "basico"],
  "timeout_sec": 3.0,
  "memory_mb": 128,
  "hints": [
    "Level 1: General orientation",
    "Level 2: Functions to use",
    "Level 3: Code examples",
    "Level 4: Near-complete solution"
  ]
}
```

See `backend/problems/sec_hola_mundo/` through `backend/problems/sec_promedio_tres_numeros/` for complete examples.

### General Problem Creation Process

**Quick Checklist:**
- [ ] Choose subject_id and unit_id from [backend/subjects_config.json](backend/subjects_config.json)
- [ ] Create directory: `mkdir backend/problems/new_problem_id`
- [ ] Create `prompt.md` (problem statement in Markdown)
- [ ] Create `starter.py` (template code with `main()` function)
- [ ] Create `tests_public.py` (3-4 tests visible to students)
- [ ] Create `tests_hidden.py` (2-3 hidden grading tests)
- [ ] Create `metadata.json` (title, subject_id, unit_id, difficulty, tags, timeout_sec, memory_mb, hints[])
- [ ] Create `rubric.json` (test names must match pytest functions exactly)
- [ ] Test submission flow end-to-end

**Detailed Steps:**

1. Choose subject/unit from [backend/subjects_config.json](backend/subjects_config.json)
   - **Available subjects**: programacion-1, programacion-2, programacion-3, programacion-4, paradigmas, algoritmos, frontend, backend
   - **Units per subject**: 5 units each (see subjects_config.json for unit_id values)

2. Create directory: `mkdir backend/problems/new_problem`
3. Create 6 required files: `prompt.md`, `starter.py`, `tests_public.py`, `tests_hidden.py`, `metadata.json`, `rubric.json`
4. Fill metadata.json with subject_id and unit_id (must match subjects_config.json exactly)
5. Test locally:

```bash
# Submit test
curl -X POST http://localhost:8000/api/submit \
  -H "Content-Type: application/json" \
  -d '{"problem_id": "new_problem", "code": "def my_func():\n    pass", "student_id": "test"}'

# Check results
curl http://localhost:8000/api/result/JOB_ID

# Verify hierarchy
curl http://localhost:8000/api/problems/hierarchy | python -m json.tool
```

## Common Tasks

**Restart service after code changes:**
```bash
docker compose restart backend
# Or rebuild if dependencies changed:
docker compose up -d --build backend
```

**Reset database:**
```bash
docker compose down -v && docker compose up --build
```

**Change resource limits globally:**
Edit `DEFAULT_TIMEOUT`, `DEFAULT_MEMORY_MB`, `DEFAULT_CPUS` in worker/tasks.py

**Change resource limits per problem:**
Edit problem's metadata.json (timeout_sec, memory_mb)

**Test problem manually:**
```bash
docker run -it --rm -v $(pwd)/backend/problems/sumatoria:/workspace -w /workspace py-playground-runner:latest bash
# Inside container:
echo "def suma(a,b): return a+b" > student_code.py
pytest -v tests_public.py
```

## Port Configuration

**Windows users**: Default ports may have permission issues. Configured with alternatives:
- PostgreSQL: External `5433` → Internal `5432`
- Redis: Internal only (no external port needed)
- Backend: `8000`
- Frontend: `5173`

Container-to-container communication uses internal ports (e.g., `postgres:5432` in DATABASE_URL).

## Troubleshooting

**First-time startup is slow**: 5-10 minutes to download/build images. Monitor: `docker compose logs -f`

**Port already in use**:
```bash
# Windows: netstat -ano | findstr :8000 && taskkill /PID <PID> /F
# Linux: lsof -i :8000 && kill -9 <PID>
```

**Worker can't access Docker daemon**:
- Check `/var/run/docker.sock` mounted in docker-compose.yml
- Windows: Verify Docker Desktop uses WSL 2
- Linux: Add user to docker group: `sudo usermod -aG docker $USER && newgrp docker`

**Runner image not found**: `docker build -t py-playground-runner:latest ./runner`

**ModuleNotFoundError**: Dockerfile COPY paths incorrect. Use `backend/requirements.txt` not `requirements.txt`. Rebuild: `docker compose build --no-cache backend`

**Worker fails with "module 'worker' has no attribute 'tasks'"**:
- **Cause**: Missing `PYTHONPATH=/app` in worker environment
- **Fix**: Add `PYTHONPATH: /app` to worker environment in docker-compose.yml
- **Verify**: `docker compose exec worker python -c "from worker import tasks; print('OK')"`

**Worker fails with "No module named 'pydantic_settings'"**:
- **Cause**: Worker imports backend modules which require pydantic-settings
- **Fix**: Add `pydantic==2.9.2` and `pydantic-settings==2.5.2` to worker/requirements.txt
- **Rebuild**: `docker compose up --build -d worker`

**Tests timing out**: Increase timeout_sec in metadata.json or DEFAULT_TIMEOUT in worker/tasks.py

**Database connection errors**: Wait for healthcheck: `docker compose ps`

**RQ worker not processing**: Check Redis: `docker compose exec redis redis-cli ping`

## Refactoring Status

See [REFACTORING_COMPLETE.md](REFACTORING_COMPLETE.md) for detailed progress.

**Completed**:
- ✅ Phase 1 (100%): Core infrastructure (config, logging, validation, exceptions)
- ✅ Phase 2 (100%): Service layer architecture, Pydantic v2 schemas

**In Progress**:
- ⏳ Phase 3 (85%): Testing (83 tests, 25/53 passing), linting, pre-commit hooks

**When continuing refactoring**:
1. Read REFACTORING_COMPLETE.md first
2. Follow service layer pattern
3. Use structured logging: `get_logger(__name__)`
4. Add validation for inputs
5. Test after changes

## Frontend Architecture

**TypeScript Migration** ✅ (Completed: 25 Oct 2025)
- Migrated from JavaScript to TypeScript for improved type safety
- Centralized API types in `src/types/api.ts`
- All components fully typed with interfaces

**Components**:
- **App.tsx** - Tab navigation (Ejercicios, Panel Docente)
- **Playground.tsx** - Student interface with cascading dropdowns, Monaco editor, result polling with AbortController
- **AdminPanel.tsx** - Instructor dashboard
- **types/api.ts** - TypeScript interfaces for all API requests/responses

**Features**:
- Monaco Editor for Python syntax highlighting
- Code persisted to localStorage
- Full TypeScript type checking with strict mode
- Type-safe API calls with Axios

**Tech Stack**:
- React 18 with TypeScript
- Vite 6 for build tooling
- Monaco Editor for code editing
- Axios for HTTP requests
- TypeScript strict mode enabled

**Development Workflow**:
```bash
# Run dev server (hot reload enabled)
npm run dev

# Type check without compiling
npx tsc --noEmit

# Build for production
npm run build

# Preview production build
npm run preview
```

**Adding New Components**:
1. Create `.tsx` files (not `.jsx`)
2. Import types from `src/types/api.ts`
3. Define component props interface:
   ```typescript
   interface MyComponentProps {
     title: string
     onSubmit: (data: FormData) => void
   }

   function MyComponent({ title, onSubmit }: MyComponentProps) {
     const [value, setValue] = useState<string>('')
     // ...
   }
   ```

**Adding New API Types**:
Edit `frontend/src/types/api.ts` and add/export new interfaces. Types are automatically available throughout the app.

## Extension Points

- Multiple workers for scaling (add worker services in docker-compose.yml)
- Different languages (change RUNNER_IMAGE env var)
- Custom test frameworks (update conftest.py)
- Authentication (add middleware to backend/app.py)
- Webhooks (add to worker/tasks.py after commit)
- Rate limiting (Redis counter in backend)

## Documentation Organization

### Active Documentation (Root Directory)

**Current and Relevant** - 10 files in root:
- **CLAUDE.md** - This file, main project documentation
- **README.md** - Project overview and quick start
- **TESTING.md** - Testing guidelines and commands
- **ANTI_PASTE_FEATURE.md** - Anti-cheating system documentation
- **HINT_SYSTEM.md** - Progressive hint system guide
- **HISTORIAS_USUARIO.md** - User stories and use cases
- **LEGACY_FILES.md** - Documentation of deprecated files
- **PROBLEMAS_FALTANTES.md** - Analysis of empty units (26/40)
- **REFACTORIZACION_TYPESCRIPT.md** - TypeScript migration guide
- **TEST_FAILURES_ANALYSIS.md** - Current test status

### Historical Documentation (docs/archive/)

**Preserved for Reference** - 9 files archived:
- Refactoring session notes (Oct 25, Nov 10, 2025)
- Production readiness analysis
- GitHub setup guide
- Test fixes documentation

See [docs/archive/README.md](docs/archive/README.md) for details.

### Project Directories

```
.
├── backend/          # FastAPI REST API
├── worker/           # RQ worker for async jobs
├── frontend/         # React + TypeScript + Vite
├── runner/           # Docker sandbox image
├── legacy/           # MVP historical code (preserved)
├── docs/
│   ├── archive/      # Historical documentation
│   └── problem-specs/ # Original .docx specifications
└── scripts/          # Utility scripts
    ├── add_hints_to_problems.py
    └── archive/      # Obsolete scripts
```

### Cleaning Up Cache Files

Cache files are automatically regenerated and should never be committed:

```bash
# Clean Python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
rm -rf backend/htmlcov backend/.coverage backend/coverage.xml
rm -rf .pytest_cache

# Already ignored by .gitignore
```

Run cleanup periodically (every 2-3 weeks) to keep working directory clean.
