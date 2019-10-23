current_dir := $(shell pwd)

train:
	docker-compose run rasa_train
run:
	docker-compose run --service-ports rasa_run

shell:
	docker-compose run rasa_shell

interactive:
	docker-compose run --service-ports rasa_interactive

visualize:
  docker-compose run rasa_visualize
