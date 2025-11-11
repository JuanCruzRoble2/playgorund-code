# 🎨 Deploy en Easypanel - Guía Completa

**Tiempo estimado:** 15-20 minutos
**Costo:** Depende del servidor (VPS desde $4/mes)
**Dificultad:** ⭐⭐☆☆☆ (Fácil)

---

## 🎯 ¿Qué es Easypanel?

Easypanel es un **panel de control** que instalas en tu propio servidor (VPS) y te permite deployar aplicaciones con Docker de forma visual, similar a Railway o Vercel, pero con control total.

**Ventajas para tu proyecto:**
- ✅ **Soporta Docker-in-Docker nativo** (perfecto para tu Worker)
- ✅ **Interfaz visual** (no necesitas comandos complicados)
- ✅ **Lee docker-compose.yml** automáticamente
- ✅ **Dominio y SSL automático** (con Let's Encrypt)
- ✅ **Monitoreo incluido** (logs, recursos, métricas)
- ✅ **Templates y backups automáticos**

---

## 📋 Prerequisitos

### Opción A: Tienes un VPS (Digital Ocean, Hetzner, etc.)
- ✅ VPS con Ubuntu 22.04 (mínimo 1GB RAM)
- ✅ IP pública del servidor
- ✅ Acceso SSH como root

### Opción B: No tienes servidor
Necesitas crear uno primero. **Proveedores recomendados:**

| Proveedor | Plan Recomendado | Precio/mes |
|-----------|------------------|------------|
| **Hetzner** (mejor precio) | CX11 (2GB RAM) | €4 (~$4.50) |
| **Digital Ocean** | Basic 1GB | $6 |
| **Vultr** | Regular 1GB | $5 |
| **Contabo** | VPS S (8GB RAM) | €5 (~$5.50) |

---

## 🚀 Parte 1: Instalar Easypanel en tu Servidor

### Paso 1.1: Conectar a tu VPS por SSH

```bash
# Linux/Mac/Windows PowerShell
ssh root@TU_IP_DEL_SERVIDOR

# Ejemplo:
ssh root@164.90.123.456
```

### Paso 1.2: Instalar Easypanel (Un solo comando)

```bash
# Instalar Easypanel
curl -sSL https://get.easypanel.io | sh

# Esto instala:
# - Docker y Docker Compose
# - Easypanel
# - Traefik (reverse proxy)
# - Base de datos interna
```

⏱️ **Espera 2-3 minutos** para que termine la instalación.

### Paso 1.3: Acceder al Panel

1. **Abrir navegador:** `http://TU_IP:3000`
2. **Crear cuenta admin:**
   - Email: tu@email.com
   - Password: (tu contraseña segura)
3. **Login** con las credenciales creadas

**¡Listo! Ya tienes Easypanel instalado** 🎉

---

## 📦 Parte 2: Preparar tu Proyecto

### Paso 2.1: Crear archivo `easypanel.yml`

Easypanel puede leer tu `docker-compose.yml`, pero es mejor crear un archivo específico para mejor compatibilidad.

Crea el archivo `easypanel.yml` en la raíz de tu proyecto:

```yaml
version: '3.8'

services:
  # PostgreSQL Database
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: playground
      POSTGRES_USER: playground
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U playground"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis for RQ
  redis:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Backend API
  backend:
    build:
      context: .
      dockerfile: backend/Dockerfile
    environment:
      DATABASE_URL: postgresql://playground:${POSTGRES_PASSWORD}@postgres:5432/playground
      REDIS_URL: redis://redis:6379/0
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - ./backend:/app/backend:ro
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.backend.rule=Host(`api.${DOMAIN}`)"
      - "traefik.http.routers.backend.entrypoints=websecure"
      - "traefik.http.routers.backend.tls.certresolver=letsencrypt"
      - "traefik.http.services.backend.loadbalancer.server.port=8000"

  # RQ Worker
  worker:
    build:
      context: .
      dockerfile: worker/Dockerfile
    environment:
      DATABASE_URL: postgresql://playground:${POSTGRES_PASSWORD}@postgres:5432/playground
      REDIS_URL: redis://redis:6379/0
      RUNNER_IMAGE: py-playground-runner:latest
      WORKSPACE_DIR: /workspaces
      HOST_WORKSPACE_DIR: /app/workspaces
      PYTHONPATH: /app
      DOCKER_HOST: unix:///var/run/docker.sock
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./backend:/app/backend:ro
      - ./worker:/app/worker:ro
      - ./workspaces:/workspaces

  # Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    environment:
      VITE_API_URL: https://api.${DOMAIN}
    depends_on:
      - backend
    volumes:
      - ./frontend/src:/app/src
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.frontend.rule=Host(`${DOMAIN}`)"
      - "traefik.http.routers.frontend.entrypoints=websecure"
      - "traefik.http.routers.frontend.tls.certresolver=letsencrypt"
      - "traefik.http.services.frontend.loadbalancer.server.port=5173"

volumes:
  postgres_data:
```

### Paso 2.2: Crear archivo `.env.example` para Easypanel

```bash
# PostgreSQL
POSTGRES_PASSWORD=change_this_password_123

# Domain (will be configured in Easypanel)
DOMAIN=miapp.com
```

### Paso 2.3: Subir código a GitHub (si aún no lo hiciste)

```bash
# En tu PC local
git init
git add .
git commit -m "Prepare for Easypanel deployment"
git remote add origin https://github.com/tu-usuario/runner10novi.git
git push -u origin main
```

---

## 🎨 Parte 3: Deploy en Easypanel

### Paso 3.1: Crear Proyecto

1. **En Easypanel Dashboard**, click **"+ Create Project"**
2. **Nombre:** `python-playground`
3. **Click:** "Create"

### Paso 3.2: Opción 1 - Deploy desde GitHub (Recomendado)

1. **Click:** "Add Service" → **"GitHub"**
2. **Conectar GitHub:**
   - Autorizar Easypanel
   - Seleccionar repositorio: `runner10novi`
   - Branch: `main`
3. **Configuración:**
   - **Build Method:** Docker Compose
   - **Compose File:** `easypanel.yml` (o `docker-compose.yml`)
   - **Auto Deploy:** ✅ (deploy automático en cada push)
4. **Click:** "Deploy"

### Paso 3.3: Opción 2 - Deploy Manual

Si no quieres usar GitHub:

1. **Click:** "Add Service" → **"Docker Compose"**
2. **Copiar contenido de `easypanel.yml`**
3. **Pegar en el editor**
4. **Click:** "Deploy"

Luego necesitas subir archivos manualmente:

```bash
# Desde tu PC, copiar proyecto al servidor
scp -r . root@TU_IP:/easypanel/projects/python-playground/
```

---

## ⚙️ Parte 4: Configurar Variables de Entorno

### Paso 4.1: Variables del Proyecto

1. **En Easypanel**, ir a: `Projects` → `python-playground` → **"Settings"**
2. **Tab "Environment"**
3. **Agregar variables:**

```bash
POSTGRES_PASSWORD=tu_password_seguro_123
DOMAIN=miapp.com  # Tu dominio (o usa la IP temporalmente)
```

### Paso 4.2: Variables Específicas por Servicio

Easypanel lee las variables del `easypanel.yml`, pero puedes sobrescribir:

**Para Backend:**
```bash
DATABASE_URL=postgresql://playground:tu_password@postgres:5432/playground
REDIS_URL=redis://redis:6379/0
```

**Para Worker:**
```bash
DATABASE_URL=postgresql://playground:tu_password@postgres:5432/playground
REDIS_URL=redis://redis:6379/0
RUNNER_IMAGE=py-playground-runner:latest
WORKSPACE_DIR=/workspaces
PYTHONPATH=/app
```

**Para Frontend:**
```bash
VITE_API_URL=https://api.miapp.com  # Cambiar por tu dominio
```

---

## 🏗️ Parte 5: Construir Runner Image

El Worker necesita la imagen `py-playground-runner`. Easypanel la construirá automáticamente si detecta el `Dockerfile`.

### Opción A: Build Automático (en docker-compose)

Ya está configurado en `easypanel.yml`. Easypanel construirá todas las imágenes.

### Opción B: Build Manual (si falla)

1. **SSH al servidor:**
   ```bash
   ssh root@TU_IP
   ```

2. **Construir imagen manualmente:**
   ```bash
   cd /easypanel/projects/python-playground
   docker build -t py-playground-runner:latest ./runner
   ```

---

## 🌍 Parte 6: Configurar Dominio

### Paso 6.1: Sin Dominio (Usar IP)

Si no tienes dominio, puedes acceder temporalmente por IP:

1. **En Easypanel**, cada servicio tiene:
   - **Backend:** `http://TU_IP:8000`
   - **Frontend:** `http://TU_IP:5173`

2. **Actualizar frontend ENV:**
   ```bash
   VITE_API_URL=http://TU_IP:8000
   ```

### Paso 6.2: Con Dominio Propio

Si tienes un dominio (ej: `miapp.com`):

**1. Configurar DNS (en tu proveedor de dominio):**

| Tipo | Nombre | Valor | TTL |
|------|--------|-------|-----|
| A | @ | TU_IP | 300 |
| A | www | TU_IP | 300 |
| A | api | TU_IP | 300 |

**2. En Easypanel:**

1. **Ir a:** `Projects` → `python-playground` → `backend` → **"Domains"**
2. **Add Domain:** `api.miapp.com`
3. **SSL:** ✅ Enable (Easypanel usa Let's Encrypt automático)
4. **Repetir para frontend:**
   - Domain: `miapp.com` y `www.miapp.com`
   - SSL: ✅ Enable

**3. Actualizar variables:**
```bash
DOMAIN=miapp.com
VITE_API_URL=https://api.miapp.com
```

**4. Redeploy servicios** para aplicar cambios.

⏱️ **Espera 5-10 minutos** para propagación DNS.

---

## ✅ Parte 7: Verificar Deployment

### Paso 7.1: Ver Logs

En Easypanel:

1. **Projects** → `python-playground`
2. **Click en cada servicio** (backend, worker, frontend)
3. **Tab "Logs"** → Ver logs en tiempo real

### Paso 7.2: Health Check

**Backend:**
```bash
curl https://api.miapp.com/api/health
# O con IP:
curl http://TU_IP:8000/api/health
```

**Output esperado:**
```json
{
  "status": "ok",
  "database": "connected",
  "redis": "connected",
  "problems_loaded": 31
}
```

### Paso 7.3: Probar Frontend

**Con dominio:**
```
https://miapp.com
```

**Con IP:**
```
http://TU_IP:5173
```

### Paso 7.4: Test de Submission

1. **Abrir frontend**
2. **Seleccionar un problema**
3. **Escribir código**
4. **Click "Ejecutar"**
5. **Ver resultados** (debe tardar 2-3 segundos)

---

## 📊 Parte 8: Monitoreo en Easypanel

Easypanel incluye monitoreo integrado:

### Dashboard Principal

1. **Metrics:** CPU, RAM, Network usage
2. **Logs:** Logs en tiempo real de todos los servicios
3. **Events:** Historial de deployments y errores
4. **Backups:** Configurar backups automáticos

### Ver Recursos por Servicio

1. **Click en servicio** (ej: backend)
2. **Tab "Metrics":**
   - CPU Usage
   - Memory Usage
   - Network I/O
   - Restart count

### Configurar Alertas (Opcional)

1. **Settings** → **"Notifications"**
2. **Add Webhook** (Discord, Slack, etc.)
3. **Configurar alertas:**
   - Service down
   - High CPU usage
   - High memory usage

---

## 🔄 Parte 9: Actualizar la Aplicación

### Método 1: Auto-Deploy desde GitHub

Si configuraste GitHub en Paso 3.2:

```bash
# En tu PC
git add .
git commit -m "Update feature X"
git push origin main

# Easypanel auto-deploya en 1-2 minutos
```

### Método 2: Manual

1. **En Easypanel:**
   - Ir al servicio
   - Click **"Redeploy"**
2. **O desde terminal:**
   ```bash
   ssh root@TU_IP
   cd /easypanel/projects/python-playground
   git pull
   docker compose up -d --build
   ```

---

## 🐛 Parte 10: Troubleshooting

### Problema: "Service failed to start"

**Solución:**
1. **Ver logs del servicio en Easypanel**
2. **Errores comunes:**
   - Variables de entorno faltantes
   - Puerto ya en uso
   - Imagen no construida

```bash
# SSH al servidor
ssh root@TU_IP

# Ver logs completos
docker compose -f /easypanel/projects/python-playground/docker-compose.yml logs backend
```

### Problema: "Cannot connect to Docker daemon" (Worker)

**Causa:** Worker no tiene acceso al Docker socket.

**Solución:**
```bash
# SSH al servidor
ssh root@TU_IP

# Verificar permisos
ls -la /var/run/docker.sock

# Dar permisos (temporal)
chmod 666 /var/run/docker.sock

# Permanente: agregar usuario al grupo docker
usermod -aG docker easypanel
```

### Problema: "Database connection failed"

**Causa:** PostgreSQL no está ready o password incorrecto.

**Solución:**
1. **Verificar servicio postgres está "Running"** en Easypanel
2. **Verificar password en variables de entorno**
3. **Esperar healthcheck** (puede tardar 30-60 segundos)

### Problema: Frontend no se conecta a Backend

**Causa:** `VITE_API_URL` incorrecto.

**Solución:**
```bash
# Verificar variable en frontend service
# Debe ser: https://api.miapp.com (con dominio)
# O: http://TU_IP:8000 (sin dominio)

# Cambiar y redeploy frontend
```

### Problema: SSL no funciona

**Causa:** DNS no propagado o dominio mal configurado.

**Solución:**
1. **Verificar DNS:**
   ```bash
   nslookup api.miapp.com
   # Debe resolver a TU_IP
   ```
2. **Esperar propagación DNS** (5-15 minutos)
3. **En Easypanel:** Re-generar certificado SSL

### Problema: "No space left on device"

**Causa:** Disco lleno.

**Solución:**
```bash
# Limpiar Docker
docker system prune -a -f

# Ver uso de disco
df -h

# Limpiar logs viejos
journalctl --vacuum-time=7d
```

---

## 💾 Parte 11: Backups (IMPORTANTE)

### Backup Automático en Easypanel

1. **Settings** → **"Backups"**
2. **Enable Automated Backups:**
   - Frequency: Daily
   - Retention: 7 days
   - Include volumes: ✅
3. **Backup destination:**
   - Local (en el mismo servidor)
   - S3 (recomendado para seguridad)

### Backup Manual de Base de Datos

```bash
# SSH al servidor
ssh root@TU_IP

# Crear backup
docker exec -it python-playground-postgres-1 pg_dump -U playground playground > backup_$(date +%Y%m%d).sql

# Descargar a tu PC
scp root@TU_IP:~/backup_*.sql ./backups/
```

### Restaurar Backup

```bash
# Subir backup al servidor
scp backup_20250111.sql root@TU_IP:~/

# SSH al servidor
ssh root@TU_IP

# Restaurar
cat backup_20250111.sql | docker exec -i python-playground-postgres-1 psql -U playground playground
```

---

## 🔐 Parte 12: Seguridad

### Firewall (UFW)

```bash
# SSH al servidor
ssh root@TU_IP

# Configurar firewall
ufw allow 22/tcp    # SSH
ufw allow 80/tcp    # HTTP
ufw allow 443/tcp   # HTTPS
ufw allow 3000/tcp  # Easypanel dashboard

# Habilitar
ufw enable
```

### Cambiar Puerto SSH (Opcional)

```bash
nano /etc/ssh/sshd_config

# Cambiar:
Port 2222  # En lugar de 22

# Reiniciar SSH
systemctl restart sshd

# Actualizar firewall
ufw allow 2222/tcp
ufw delete allow 22/tcp
```

### Proteger Easypanel Dashboard

1. **Easypanel** → **"Settings"** → **"Security"**
2. **Enable 2FA** (Two-Factor Authentication)
3. **IP Whitelist** (opcional)

---

## 💰 Costos Estimados

| Opción | Servidor | Easypanel | Total/mes |
|--------|----------|-----------|-----------|
| **Mínimo** | Hetzner CX11 (2GB) | Gratis | $4.50 |
| **Recomendado** | Digital Ocean 1GB | Gratis | $6 |
| **Óptimo** | Hetzner CX21 (4GB) | Gratis | $9 |

**Easypanel es 100% gratis** (open source)

---

## 📝 Checklist Final

- [ ] Easypanel instalado en VPS
- [ ] Proyecto subido a GitHub (opcional)
- [ ] Archivo `easypanel.yml` creado
- [ ] Proyecto creado en Easypanel
- [ ] Variables de entorno configuradas
- [ ] 5 servicios deployados
- [ ] Runner image construida
- [ ] Health check responde OK
- [ ] Frontend accesible
- [ ] Submission de prueba funciona
- [ ] (Opcional) Dominio configurado
- [ ] (Opcional) SSL activado
- [ ] (Opcional) Backups configurados

---

## 🎯 Ventajas de Easypanel vs Otras Opciones

| Feature | Easypanel | Railway | Digital Ocean Manual |
|---------|-----------|---------|---------------------|
| **Interfaz visual** | ✅ | ✅ | ❌ |
| **Docker-in-Docker** | ✅ Nativo | ⚠️ Necesita DinD | ✅ |
| **Costo** | $4-6 VPS | $5-20 variable | $6 fijo |
| **Auto-deploy GitHub** | ✅ | ✅ | ❌ |
| **SSL automático** | ✅ | ✅ | ⚠️ Manual |
| **Monitoreo** | ✅ | ✅ | ❌ |
| **Backups** | ✅ | ⚠️ Pago | ❌ Manual |
| **Control total** | ✅ | ❌ | ✅ |

---

## 📚 Recursos Adicionales

- **Easypanel Docs:** https://easypanel.io/docs
- **Easypanel GitHub:** https://github.com/easypanel-io/easypanel
- **Discord Community:** https://discord.gg/easypanel
- **Video Tutorial:** https://www.youtube.com/easypanel

---

## 🆘 Soporte

### Opción 1: Documentación Oficial
https://easypanel.io/docs

### Opción 2: Discord Community
Únete a Discord de Easypanel - responden rápido

### Opción 3: GitHub Issues
https://github.com/easypanel-io/easypanel/issues

---

## 🎉 ¡Listo!

**Tu aplicación está corriendo en Easypanel con:**
- ✅ Interfaz visual fácil de usar
- ✅ Docker-in-Docker funcionando
- ✅ SSL automático
- ✅ Monitoreo en tiempo real
- ✅ Auto-deploy desde GitHub
- ✅ Backups automáticos

**¡Disfruta de tu plataforma educativa! 🚀**
