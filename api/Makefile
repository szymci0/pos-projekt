clean:
	@rm -f */version.txt
	@rm -fr ./*/*/__pycache__
	@rm -fr ./*/__pycache__
	@rm -fr ./__pycache__
	@rm -fr pos_api-*.dist-info
	@rm -fr pos_api.egg-info
	@echo '  => Clean done'

dev_install:
	@pip install -e .

dev_run:
	@python pos_api/app.py

db_fixtures_load:
	@pos_apicli database-defaults
