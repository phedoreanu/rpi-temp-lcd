run:
	@sudo python app.py

build:
	@docker build -t phedoreanu/rpi-temp-lcd .

push:
	@docker push phedoreanu/rpi-temp-lcd

deps:
	@sudo pip install -Ur requirements.txt