build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show-logs:
	docker compose -f local.yml logs

show-logs-webapp:
	docker compose -f local.yml logs webapp

makemigrations:
	docker compose -f local.yml run --rm webapp python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm webapp python manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm webapp python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm webapp python manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v

volume:
	docker volume inspect src_local_postgres_data

admin-db:
	docker compose -f local.yml exec postgres psql --username=portaluser --dbname=jobdb

flake8:
	docker compose -f local.yml exec webapp flake8 .

black-check:
	docker compose -f local.yml exec webapp black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec webapp black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec webapp black --exclude=migrations .

isort-check:
	docker compose -f local.yml exec webapp isort . --check-only --skip venv --skip migrations

isort-diff:
	docker compose -f local.yml exec webapp isort . --diff --skip venv --skip migrations

isort:
	docker compose -f local.yml exec webapp isort . --skip venv --skip migrations

search-create:
	docker compose -f local.yml exec webapp python manage.py search_index --create

search-populate:
	docker compose -f local.yml exec webapp python manage.py search_index --populate

search-rebuild:
	docker compose -f local.yml exec webapp python manage.py search_index --rebuild
