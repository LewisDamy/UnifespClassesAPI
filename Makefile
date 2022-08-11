install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
freeze:
	pip freeze > requirements.txt
format:
	black *.py
lint:
	pylint --disable=R,C *.py
test:
	#test
deploy:
	#deploy
all:
	install lint test deploy