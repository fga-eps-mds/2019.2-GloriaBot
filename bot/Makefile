current_dir := $(shell pwd)

train:
	docker-compose run rasa_train

run:
	docker-compose run --service-ports --rm rasa_run
	docker container stop mongo-express
	docker container stop mongo
	docker container stop action_server

shell:
	docker-compose run rasa_shell
	docker container stop mongo-express
	docker container stop mongo
	docker container stop action_server

interactive:
	docker-compose run --service-ports rasa_interactive
	docker container stop mongo-express
	docker container stop mongo
	docker container stop action_server	

visualize:
	docker-compose run rasa_visualize
