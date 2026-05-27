from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.services.company_creation_service import CompanyCreationService
import subprocess
import os

proc: subprocess.Popen | None = None


def start_dramatique_process() -> None:
    global proc
    DETACHED_FLAG = 0
    if subprocess._mswindows:  # noqa: SLF001
        DETACHED_FLAG = 0x00000008
    proc = subprocess.Popen(
        "dramatiq --processes=4 --threads=4 app.dramatiq",
        shell=True,
        stdin=None,
        stdout=None,
        stderr=None,
        close_fds=True,
        creationflags=DETACHED_FLAG,
    )
    print("dramatiq background process started")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown lifecycle events.
    
    Replaces deprecated app.add_event_handler("startup"/"shutdown", ...)
    with the modern lifespan context manager pattern (FastAPI 0.93+).
    """
    # Startup
    CompanyCreationService.upgrade_all()
    if not os.getenv("IS_DOCKER"):
        start_dramatique_process()
    yield
    # Shutdown
    global proc  # noqa: PLW0405
    if proc:
        proc.kill()
        proc.wait()


def setup_event_handlers(app: FastAPI):
    """Compatibility wrapper - lifespan is now handled via FastAPI(lifespan=...) constructor."""
    # The lifespan is set directly on the FastAPI app in main.py
    # This function is kept for backward compatibility
