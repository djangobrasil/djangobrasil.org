clean:
	@echo "removing pycs"
	@find . -name "*.pyc" -delete

deps: 
	@echo "installing deps"
	@pip install -qr test_requirements.txt

test: clean deps
	@echo "running tests"
	@./src/djangobrasil/manage.py test

	@echo "flake8 check"
	@flake8 .

syncdb:
	@./src/djangobrasil/manage.py syncdb
