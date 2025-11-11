FROM python:3.11-slim

# Install only Docker CLI (not the full docker.io package)
# We use Docker's official APT repository for a smaller footprint
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y --no-install-recommends docker-ce-cli && \
    apt-get purge -y curl gnupg && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy worker requirements
COPY worker/requirements.txt ./worker/
RUN pip install --no-cache-dir -r worker/requirements.txt

# Copy backend and worker code
COPY backend ./backend
COPY worker ./worker

# Run RQ worker
CMD ["python", "-m", "rq.cli", "worker", "--url", "redis://redis:6379/0", "submissions"]
