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
build:
	docker build -t unifesp-api .
run:
	docker run -p 8000:8000 --rm unifesp-api:lastest
deploy:
	#deploy
all:
	install lint test deploy