current_dir := $(shell pwd)

train:
	docker-compose run tr
run:
	docker-compose run rasa_run
shell:
	docker-compose run shell
start:
	docker-compose run tr
	docker-compose run rasa_run

interactive:
	docker-compose run inter
	
visualize:
	docker-compose run vis
