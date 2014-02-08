deps: 
	@pip install -qr test_requirements.txt

test: deps
	@./src/djangobrasil/manage.py test
