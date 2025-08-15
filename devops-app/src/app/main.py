from fastapi import FastAPI
from . import __version__

app = FastAPI(
	title="DevOps FastAPI App",
	description="A minimal FastAPI service used in a DevOps scaffold",
	version=__version__,
)


@app.get("/")
async def root() -> dict:
	return {
		"name": "devops-fastapi-app",
		"version": __version__,
		"docs_url": "/docs",
		"health_url": "/health",
	}


@app.get("/health")
async def health() -> dict:
	return {"status": "ok"}


@app.get("/ping")
async def ping() -> dict:
	return {"message": "pong"}