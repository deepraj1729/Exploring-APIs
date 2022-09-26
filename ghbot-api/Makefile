container_build:
	docker build -t ghbot .

container_run:
	docker run --rm -it -d --name ghbot -p 8000:8000 ghbot 

container_down:
	docker rm --force ghbot