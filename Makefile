scss:
	sass dashboard/scss/style.scss:dashboard/static/style.css

scss-watch:
	sass --watch dashboard/scss/style.scss:dashboard/static/style.css

pip-freeze:
	pip freeze > requirements.txt