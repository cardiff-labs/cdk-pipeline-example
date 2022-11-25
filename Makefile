dev:
	pip3 install -U pip poetry
	poetry install

update-requirements:
	poetry export --format=requirements.txt > software/src/requirements.txt
