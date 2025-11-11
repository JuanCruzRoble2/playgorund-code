"""
Centralized configuration for the application with Pydantic validation
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import List


class Settings(BaseSettings):
    """
    Application settings with environment variable support and validation.

    Uses Pydantic BaseSettings for automatic validation and type coercion.
    Values are loaded from environment variables with fallback to defaults.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    # Database
    # Use postgres service name for Docker, localhost for local development
    DATABASE_URL: str = Field(
        default="postgresql://playground:playground@postgres:5432/playground",
        description="PostgreSQL connection string"
    )

    # Redis
    REDIS_HOST: str = Field(default="redis", description="Redis host")
    REDIS_PORT: int = Field(default=6379, ge=1, le=65535, description="Redis port")
    REDIS_DB: int = Field(default=0, ge=0, le=15, description="Redis database number")

    # API
    API_HOST: str = Field(default="0.0.0.0", description="API host")
    API_PORT: int = Field(default=8000, ge=1, le=65535, description="API port")

    # CORS
    CORS_ORIGINS: str = Field(
        default="http://localhost:5173,http://localhost:3000",
        description="Comma-separated list of allowed CORS origins"
    )

    # Docker Runner
    RUNNER_IMAGE: str = Field(
        default="py-playground-runner:latest",
        description="Docker image for code execution"
    )
    DEFAULT_TIMEOUT_SEC: float = Field(
        default=5.0,
        gt=0,
        le=60,
        description="Default execution timeout in seconds"
    )
    DEFAULT_MEMORY_MB: int = Field(
        default=256,
        ge=64,
        le=2048,
        description="Default memory limit in MB"
    )
    DEFAULT_CPUS: str = Field(
        default="1.0",
        description="Default CPU limit (Docker format)"
    )

    # Limits
    MAX_CODE_LENGTH: int = Field(
        default=50000,
        ge=1000,
        le=1000000,
        description="Maximum code length in characters"
    )
    MAX_SUBMISSION_POLL_ATTEMPTS: int = Field(
        default=30,
        ge=1,
        le=100,
        description="Maximum polling attempts for results"
    )
    POLL_INTERVAL_SEC: float = Field(
        default=1.0,
        gt=0,
        le=10,
        description="Polling interval in seconds"
    )

    # Paths
    PROBLEMS_DIR: str = Field(
        default="backend/problems",
        description="Directory containing problem definitions"
    )
    BACKEND_DIR: str = Field(
        default="backend",
        description="Backend code directory"
    )

    # Logging
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
    )

    @field_validator("CORS_ORIGINS")
    @classmethod
    def parse_cors_origins(cls, v: str) -> List[str]:
        """Parse comma-separated CORS origins into a list"""
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v

    @field_validator("LOG_LEVEL")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate log level is one of the allowed values"""
        allowed = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        v_upper = v.upper()
        if v_upper not in allowed:
            raise ValueError(f"LOG_LEVEL must be one of {allowed}, got '{v}'")
        return v_upper


# Singleton instance with automatic validation
try:
    settings = Settings()
except Exception as e:
    # Provide helpful error message if configuration is invalid
    print(f"❌ Configuration Error: {e}")
    print("Please check your environment variables or .env file")
    raise
