clean:
	@rm -f */version.txt .coverage
	@find . -name '__pycache__' |xargs rm -fr {} \;
	@rm -fr pos_pkg-*.dist-info
	@rm -fr pos_pkg.egg-info

dev_install:
	@pip install -e .