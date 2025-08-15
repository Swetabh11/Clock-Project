PYTHON=python3
PIP=./.venv/bin/pip
UVICORN=./.venv/bin/uvicorn
PYTEST=./.venv/bin/pytest

.PHONY: install run test docker-build docker-run k8s-apply k8s-delete helm-install helm-uninstall terraform-init terraform-validate terraform-plan terraform-apply

install:
	$(PYTHON) -m venv .venv
	./.venv/bin/pip install -r requirements.txt

run:
	PYTHONPATH=src $(UVICORN) app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	PYTHONPATH=src $(PYTEST) -q

docker-build:
	docker build -t devops-app:local .

docker-run:
	docker run --rm -p 8000:8000 devops-app:local

k8s-apply:
	kubectl apply -f k8s/

k8s-delete:
	kubectl delete -f k8s/ --ignore-not-found

helm-install:
	helm upgrade --install devops-app helm/fastapi-app --namespace dev --create-namespace --set image.repository=devops-app --set image.tag=local

helm-uninstall:
	helm uninstall devops-app --namespace dev || true

terraform-init:
	cd terraform && terraform init -backend=false

terraform-validate:
	cd terraform && terraform validate

terraform-plan:
	cd terraform && terraform plan -var='bucket_name=devops-app-demo-$(shell date +%s)'

terraform-apply:
	cd terraform && terraform apply -auto-approve -var='bucket_name=devops-app-demo-$(shell date +%s)'