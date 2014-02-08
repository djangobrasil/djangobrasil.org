clean:
	@find . -name "*.pyc" -delete

deps: 
	@pip install -qr test_requirements.txt

test: clean deps
	@./src/djangobrasil/manage.py test
