# 🔍 TRAZABILIDAD: Runner vs Worker vs Backend

## 📊 Diagrama del Flujo Completo

```
┌─────────────────────────────────────────────────────────────────┐
│                         ARQUITECTURA                             │
└─────────────────────────────────────────────────────────────────┘

    Estudiante
        │
        │ 1. Envía código Python
        ▼
    ┌──────────────┐
    │   FRONTEND   │  (React + TypeScript)
    │  Port: 5173  │
    └──────┬───────┘
           │ HTTP POST /api/submit
           │
           ▼
    ┌──────────────────────────────────────────┐
    │          BACKEND (FastAPI)               │  ◄── NO incluye runner ni worker
    │          Port: 8000                      │
    │  ┌────────────────────────────────────┐  │
    │  │ 1. Valida código (seguridad)       │  │
    │  │ 2. Crea Submission en PostgreSQL   │  │
    │  │ 3. Encola job en Redis             │  │
    │  │ 4. Retorna job_id al frontend      │  │
    │  └────────────────────────────────────┘  │
    └───────────────┬──────────────────────────┘
                    │
                    │ Job encolado
                    ▼
            ┌──────────────┐
            │    REDIS     │  (Job Queue)
            │  Port: 6379  │
            └──────┬───────┘
                   │
                   │ Worker lee jobs
                   ▼
    ┌─────────────────────────────────────────────┐
    │          WORKER (RQ Worker)                 │  ◄── Servicio SEPARADO
    │          No expone puerto                   │
    │  ┌───────────────────────────────────────┐  │
    │  │ 1. Lee job de Redis                   │  │
    │  │ 2. Crea workspace temporal            │  │
    │  │ 3. Copia tests del problema           │  │
    │  │ 4. Escribe código del estudiante      │  │
    │  │ 5. Lanza container RUNNER             │  │  ◄── Aquí usa el runner
    │  │ 6. Espera resultados                  │  │
    │  │ 7. Parsea report.json                 │  │
    │  │ 8. Aplica rúbrica (scoring)           │  │
    │  │ 9. Guarda resultados en PostgreSQL    │  │
    │  └───────────────────────────────────────┘  │
    └─────────────────┬───────────────────────────┘
                      │
                      │ Ejecuta Docker container
                      ▼
    ┌──────────────────────────────────────────────────┐
    │          RUNNER (Docker Image)                   │  ◄── Imagen Docker AISLADA
    │          py-playground-runner:latest             │
    │  ┌────────────────────────────────────────────┐  │
    │  │ Imagen minimalista con:                    │  │
    │  │ - Python 3.11                              │  │
    │  │ - pytest                                   │  │
    │  │ - Usuario no-root (uid 1000)               │  │
    │  │                                            │  │
    │  │ Ejecuta en SANDBOX:                        │  │
    │  │ - Sin red (--network none)                 │  │
    │  │ - Filesystem read-only                     │  │
    │  │ - CPU limitado (1 core)                    │  │
    │  │ - RAM limitada (256MB)                     │  │
    │  │ - Timeout (5 segundos default)             │  │
    │  │                                            │  │
    │  │ Corre: pytest tests_public.py              │  │
    │  │        pytest tests_hidden.py              │  │
    │  └────────────────────────────────────────────┘  │
    └──────────────────────────────────────────────────┘
                      │
                      │ Genera report.json
                      │
                      ▼
            Resultados vuelven al Worker
                      │
                      ▼
            Worker guarda en PostgreSQL
                      │
                      ▼
            Frontend hace polling GET /api/result/{job_id}
                      │
                      ▼
            Muestra resultados al estudiante
```

---

## 🎯 Respuesta Directa

### ❓ ¿Son del backend?

| Componente | ¿Es del backend? | Relación |
|------------|------------------|----------|
| **Backend** | ✅ Sí | Es el backend (FastAPI REST API) |
| **Worker** | ❌ **NO** | Servicio **separado** que consume jobs |
| **Runner** | ❌ **NO** | Imagen Docker **efímera** para sandbox |

### 📋 Detalle de Cada Componente

---

## 1️⃣ BACKEND (FastAPI)

### ¿Qué es?

**API REST** que recibe peticiones HTTP y las procesa.

### ¿Qué hace?

```python
# backend/app.py

@app.post("/api/submit")
def submit_code(request: SubmitRequest):
    # 1. Validar código (sin imports peligrosos)
    validate_code_safety(request.code)

    # 2. Crear submission en base de datos
    submission = create_submission(
        problem_id=request.problem_id,
        code=request.code,
        student_id=request.student_id
    )

    # 3. Encolar job en Redis
    job = queue.enqueue(
        'worker.tasks.run_submission_in_sandbox',
        submission.id,
        request.problem_id,
        request.code
    )

    # 4. Retornar job_id
    return {"job_id": job.id}
```

### Archivos principales:

- `backend/app.py` - Endpoints HTTP
- `backend/models.py` - Modelos de base de datos
- `backend/validators.py` - Validaciones de seguridad
- `backend/services/` - Lógica de negocio

### Puerto: `8000`

### ¿Ejecuta código de estudiantes?

❌ **NO** - Solo valida y encola. No ejecuta código.

---

## 2️⃣ WORKER (RQ Worker)

### ¿Qué es?

**Servicio background** que procesa jobs de manera asíncrona usando RQ (Redis Queue).

### ¿Qué hace?

```python
# worker/tasks.py

def run_submission_in_sandbox(submission_id, problem_id, code):
    # 1. Crear workspace temporal
    workspace = tempfile.mkdtemp(prefix=f"sandbox-{problem_id}-")

    # 2. Copiar tests del problema
    shutil.copy("backend/problems/suma/tests_public.py", workspace)
    shutil.copy("backend/problems/suma/tests_hidden.py", workspace)

    # 3. Escribir código del estudiante
    Path(workspace + "/student_code.py").write_text(code)

    # 4. Ejecutar Docker container (RUNNER)
    result = docker.run(
        image="py-playground-runner:latest",
        volumes={workspace: "/workspace"},
        command="pytest -q --tb=short .",
        network_mode="none",  # Sin acceso a red
        mem_limit="256m",     # Límite de RAM
        timeout=5             # Timeout 5 segundos
    )

    # 5. Leer resultados (report.json)
    results = json.loads(Path(workspace + "/report.json").read_text())

    # 6. Aplicar rúbrica y calcular puntaje
    score = calculate_score(results, rubric)

    # 7. Guardar en base de datos
    save_results(submission_id, results, score)

    # 8. Limpiar workspace
    shutil.rmtree(workspace)
```

### Archivos principales:

- `worker/tasks.py` - Funciones de jobs
- `worker/services/docker_runner.py` - Ejecuta Docker containers
- `worker/services/rubric_scorer.py` - Calcula puntajes

### Puerto: Ninguno (no expone API)

### ¿Ejecuta código de estudiantes?

❌ **NO directamente** - Delega al RUNNER (Docker container aislado)

### ¿Por qué está separado del backend?

1. **Asincronía**: Ejecución puede tardar segundos, no bloquea HTTP requests
2. **Escalabilidad**: Puedes tener múltiples workers procesando en paralelo
3. **Aislamiento**: Si un job crashea, no afecta al backend
4. **Seguridad**: Worker tiene acceso a Docker daemon, backend no

---

## 3️⃣ RUNNER (Docker Image)

### ¿Qué es?

**Imagen Docker minimalista** que se usa para ejecutar código de estudiantes en un **sandbox aislado**.

### Dockerfile:

```dockerfile
FROM python:3.11-slim

# Solo pytest, nada más
RUN pip install --no-cache-dir pytest==8.3.3

# Workspace
RUN mkdir /workspace
WORKDIR /workspace

# Usuario no-root (uid 1000) para seguridad
RUN useradd -m -u 1000 sandbox && chown -R sandbox:sandbox /workspace
USER sandbox

CMD ["pytest"]
```

### ¿Qué hace?

**NADA** por sí solo. Es una imagen **efímera** que el worker lanza con:

```bash
docker run --rm \
  --network none \              # ❌ Sin acceso a internet
  --read-only \                 # ❌ Filesystem read-only
  --tmpfs /tmp:rw,noexec \      # ❌ /tmp sin ejecución
  --cpus=1.0 \                  # ⚠️ Max 1 CPU core
  --memory=256m \               # ⚠️ Max 256MB RAM
  --memory-swap=256m \          # ⚠️ Sin swap
  -v /host/workspace:/workspace \ # ✅ Solo workspace montado
  --user 1000:1000 \            # ✅ Usuario no-root
  py-playground-runner:latest \
  pytest -q --tb=short .        # Ejecuta tests
```

### Archivos en workspace (montado):

```
/workspace/
├── student_code.py        # Código del estudiante
├── tests_public.py        # Tests visibles
├── tests_hidden.py        # Tests ocultos
├── conftest.py            # Genera report.json
└── report.json            # Resultados (creado por pytest)
```

### ¿Ejecuta código de estudiantes?

✅ **SÍ** - Este es el único lugar donde se ejecuta código no confiable.

### Seguridad:

| Restricción | Propósito |
|-------------|-----------|
| `--network none` | No puede hacer requests HTTP, descargar malware |
| `--read-only` | No puede modificar el filesystem |
| `--memory=256m` | No puede usar toda la RAM |
| `--cpus=1.0` | No puede saturar el CPU |
| `timeout=5s` | No puede correr indefinidamente |
| `USER sandbox` | No puede escalar privilegios |

---

## 🔄 Flujo Completo Paso a Paso

### Paso 1: Estudiante envía código

```javascript
// Frontend
fetch('http://localhost:8000/api/submit', {
  method: 'POST',
  body: JSON.stringify({
    problem_id: 'suma',
    code: 'def suma(a, b):\n    return a + b',
    student_id: 'alumno123'
  })
})
```

### Paso 2: Backend valida y encola

```python
# Backend recibe HTTP POST
submission = Submission.create(...)  # Guarda en PostgreSQL
job = queue.enqueue(                 # Encola en Redis
    'worker.tasks.run_submission_in_sandbox',
    submission.id, 'suma', code
)
return {"job_id": job.id}            # Retorna al frontend
```

### Paso 3: Worker procesa job

```python
# Worker (corriendo en background)
def run_submission_in_sandbox(submission_id, problem_id, code):
    # Crea workspace temporal
    workspace = "/workspaces/sandbox-suma-abc123/"

    # Copia archivos
    workspace/
    ├── student_code.py     ← Código del estudiante
    ├── tests_public.py     ← Del backend/problems/suma/
    ├── tests_hidden.py     ← Del backend/problems/suma/
    └── conftest.py         ← Generado por worker
```

### Paso 4: Worker lanza RUNNER

```bash
# Worker ejecuta este comando:
docker run --rm \
  --network none \
  --read-only \
  --memory=256m \
  -v /workspaces/sandbox-suma-abc123:/workspace \
  py-playground-runner:latest \
  pytest -q --tb=short .
```

### Paso 5: RUNNER ejecuta tests

```python
# Dentro del container RUNNER:

# pytest carga y ejecuta:
import student_code  # ← Código del estudiante

def test_suma_basico():
    assert student_code.suma(2, 3) == 5  # ✅ PASS

def test_suma_negativos():
    assert student_code.suma(-1, -1) == -2  # ✅ PASS

# conftest.py genera report.json:
[
  {"name": "test_suma_basico", "outcome": "passed", "duration": 0.001},
  {"name": "test_suma_negativos", "outcome": "passed", "duration": 0.001}
]
```

### Paso 6: Worker lee resultados

```python
# Worker lee report.json del workspace
results = json.loads(Path(workspace + "/report.json").read_text())

# Aplica rúbrica
rubric = {
  "tests": [
    {"name": "test_suma_basico", "points": 5, "visibility": "public"},
    {"name": "test_suma_negativos", "points": 5, "visibility": "hidden"}
  ],
  "max_points": 10
}

# Calcula puntaje: 10/10 (ambos passed)
score = 10.0

# Guarda en PostgreSQL
submission.score_total = 10.0
submission.status = "completed"
db.commit()
```

### Paso 7: Frontend obtiene resultados

```javascript
// Frontend hace polling cada 1 segundo
fetch('http://localhost:8000/api/result/abc123')
  .then(res => res.json())
  .then(data => {
    // {
    //   "status": "completed",
    //   "score": 10.0,
    //   "max_score": 10.0,
    //   "tests": [...]
    // }
    showResults(data)
  })
```

---

## 📦 Resumen de Relaciones

### Backend

- ✅ **Es** el backend
- ✅ Expone API REST (FastAPI)
- ✅ Maneja HTTP requests
- ✅ Valida input
- ✅ Encola jobs
- ❌ NO ejecuta código de estudiantes

### Worker

- ❌ **NO es** parte del backend (servicio separado)
- ✅ Procesa jobs en background
- ✅ Orquesta ejecución
- ✅ Lanza containers Docker
- ✅ Calcula puntajes
- ❌ NO ejecuta código directamente (usa runner)

### Runner

- ❌ **NO es** parte del backend
- ❌ **NO es** un servicio persistente
- ✅ Es una **imagen Docker** efímera
- ✅ **SÍ ejecuta** código de estudiantes
- ✅ Aislado con sandbox (seguridad)
- ⏱️ Vive solo durante ejecución de tests (~5 segundos)

---

## 🎯 Analogía para Entender

Imagina un **restaurante**:

| Componente | Analogía |
|------------|----------|
| **Frontend** | Mesero que toma el pedido |
| **Backend** | Caja registradora que procesa el pedido y lo pasa a cocina |
| **Redis** | Pizarra de pedidos pendientes |
| **Worker** | Chef que lee pedidos y cocina |
| **Runner** | Horno desechable donde se cocina cada plato (se tira después) |
| **PostgreSQL** | Libro de cuentas donde se registra todo |

**Flujo**:
1. Cliente (estudiante) pide al mesero (frontend)
2. Mesero lleva a caja (backend), registra pedido
3. Caja pone pedido en pizarra (Redis)
4. Chef (worker) lee pizarra y empieza a cocinar
5. Chef usa horno desechable (runner) para cada plato
6. Plato listo, chef actualiza libro (PostgreSQL)
7. Mesero sirve al cliente

---

## 📊 Tabla Comparativa Completa

| Aspecto | Backend | Worker | Runner |
|---------|---------|--------|--------|
| **Tipo** | API REST | Servicio background | Imagen Docker |
| **Tecnología** | FastAPI | RQ (Redis Queue) | Python + pytest |
| **Puerto** | 8000 | - | - |
| **Persistente** | ✅ Sí | ✅ Sí | ❌ No (efímero) |
| **Expone API** | ✅ Sí | ❌ No | ❌ No |
| **Ejecuta código estudiante** | ❌ No | ❌ No | ✅ Sí |
| **Acceso a Docker** | ❌ No | ✅ Sí | N/A (es Docker) |
| **Acceso a PostgreSQL** | ✅ Sí | ✅ Sí | ❌ No |
| **Acceso a Redis** | ✅ Sí | ✅ Sí | ❌ No |
| **Acceso a red** | ✅ Sí | ✅ Sí | ❌ No (--network none) |
| **CPU limitado** | ❌ No | ❌ No | ✅ Sí (1 core) |
| **RAM limitada** | ❌ No | ❌ No | ✅ Sí (256MB) |
| **Timeout** | ❌ No | ❌ No | ✅ Sí (5s) |
| **Usuario root** | ✅ Sí | ✅ Sí | ❌ No (uid 1000) |
| **Filesystem writable** | ✅ Sí | ✅ Sí | ❌ No (read-only) |

---

## 🏗️ Arquitectura de Microservicios

### Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────┐
│                    MICROSERVICIOS                        │
└─────────────────────────────────────────────────────────┘

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Frontend   │    │   Backend    │    │    Worker    │
│              │───▶│              │───▶│              │
│  React +TS   │    │   FastAPI    │    │  RQ Worker   │
│  Port: 5173  │    │  Port: 8000  │    │  (interno)   │
└──────────────┘    └──────┬───────┘    └──────┬───────┘
                           │                    │
                           │                    │ docker run
                           │                    │
                    ┌──────▼──────┐      ┌──────▼───────┐
                    │ PostgreSQL  │      │    Runner    │
                    │ Port: 5433  │      │   (efímero)  │
                    └─────────────┘      └──────────────┘
                           │
                    ┌──────▼──────┐
                    │    Redis    │
                    │ Port: 6379  │
                    └─────────────┘
```

### Separación de Responsabilidades

| Componente | Responsabilidad |
|------------|-----------------|
| **Frontend** | Presentación, UX/UI |
| **Backend** | Lógica de negocio, validación, API |
| **Worker** | Procesamiento asíncrono, orquestación |
| **Runner** | Ejecución aislada de código no confiable |
| **PostgreSQL** | Persistencia de datos |
| **Redis** | Cola de jobs, cache |

---

## 🔒 Capas de Seguridad

### 1. Backend (Primera Capa)

```python
# Validación de código antes de encolar
def validate_code_safety(code: str):
    # Bloquea imports peligrosos
    dangerous = ['os', 'subprocess', 'sys', 'eval', 'exec']
    if any(imp in code for imp in dangerous):
        raise SecurityError("Import peligroso detectado")

    # Límite de tamaño
    if len(code) > 50_000:
        raise ValidationError("Código demasiado largo")
```

### 2. Worker (Segunda Capa)

```python
# Workspace temporal aislado
workspace = tempfile.mkdtemp()
os.chmod(workspace, 0o777)

# Timeout para prevenir loops infinitos
timeout_sec = 5.0
```

### 3. Runner (Tercera Capa - Sandbox)

```bash
# Docker con restricciones máximas
docker run --rm \
  --network none \        # Sin red
  --read-only \           # Sin escritura
  --memory=256m \         # RAM limitada
  --cpus=1.0 \            # CPU limitado
  --pids-limit=50 \       # Max 50 procesos
  --user=1000:1000 \      # Usuario no-root
  py-playground-runner:latest
```

**Resultado**: Código malicioso **no puede**:
- ❌ Acceder a internet
- ❌ Leer archivos del sistema
- ❌ Escribir archivos
- ❌ Consumir todos los recursos
- ❌ Escalar privilegios
- ❌ Ejecutar indefinidamente

---

## ✅ Conclusión

### ¿Son del backend?

- **Backend**: ✅ Sí, **ES** el backend
- **Worker**: ❌ No, es un **servicio auxiliar separado**
- **Runner**: ❌ No, es una **imagen Docker temporal**

### Arquitectura:

```
Backend (API) ──enqueue──> Worker (Orquestador) ──docker run──> Runner (Sandbox)
     ↓                           ↓                                   ↓
PostgreSQL              Docker Daemon                      Código estudiante
```

Esta arquitectura de **microservicios** permite:
- 🔒 **Seguridad**: Código malicioso aislado en runner
- 📈 **Escalabilidad**: Múltiples workers procesando en paralelo
- 🚀 **Performance**: Backend no se bloquea esperando ejecución
- 🛠️ **Mantenibilidad**: Componentes independientes y desacoplados

---

## 📚 Referencias

- **Código Backend**: `backend/app.py`, `backend/services/`
- **Código Worker**: `worker/tasks.py`, `worker/services/`
- **Dockerfile Runner**: `runner/Dockerfile`
- **Orquestación**: `docker-compose.yml`
- **Documentación completa**: `CLAUDE.md`

---

**Última actualización**: 11 de Noviembre, 2025
