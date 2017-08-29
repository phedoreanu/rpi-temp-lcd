dev:
	@sudo python app.py

run:
	@docker run -d --restart unless-stopped --net host --device /dev/mem:/dev/mem --privileged phedoreanu/rpi-temp-lcd

build:
	@docker build -t phedoreanu/rpi-temp-lcd .

push:
	@docker push phedoreanu/rpi-temp-lcd

deps:
	@sudo pip install -Ur requirements.txt
