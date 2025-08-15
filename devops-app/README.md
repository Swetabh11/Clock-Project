# DevOps FastAPI Project

A minimal FastAPI service with Docker, Compose, Kubernetes manifests, a Helm chart, Terraform example, tests, and CI.

## Quickstart

- Python (local):
  - `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`
  - `PYTHONPATH=src uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
  - Open http://localhost:8000

- Docker:
  - `docker build -t devops-app:local .`
  - `docker run --rm -p 8000:8000 devops-app:local`

- Docker Compose:
  - `docker compose up --build`

- Tests:
  - `pytest -q`

## Kubernetes (manifests)

- Apply: `kubectl apply -f k8s/`
- Port-forward: `kubectl port-forward svc/fastapi-app 8080:80`
- Then open http://localhost:8080

Note: The default Deployment image is `devops-app:local`. For kind/minikube you may need to load the image into the cluster:
- kind: `kind load docker-image devops-app:local`
- minikube: `minikube image load devops-app:local`

## Helm

- Lint: `helm lint helm/fastapi-app`
- Install: `helm install devops-app helm/fastapi-app --namespace dev --create-namespace`
- Override image/tag: `helm install devops-app helm/fastapi-app --set image.repository=devops-app --set image.tag=local`

## Terraform (AWS S3 sample)

Example Terraform config that creates an S3 bucket. Requires AWS credentials.

- `cd terraform`
- `terraform init -backend=false`
- `terraform plan`
- `terraform apply`

## Endpoints

- `/` basic metadata
- `/health` health check
- `/ping` returns `{"message": "pong"}`

## CI

GitHub Actions workflow runs tests, lints Helm, builds Docker image (push to GHCR) and validates Terraform.