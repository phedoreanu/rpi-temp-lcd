# rpi-temp-lcd
A Python app that reads temperature and humidity from an __AM2302__ and displays them onto a __LCM1602C__.

## [Demo](https://youtu.be/94KnTv1vbm4)
![Demo gif](https://github.com/phedoreanu/rpi-temp-lcd/raw/master/demo.gif "Demo gif")

## [Wiring diagram](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/)
![Wiring diagram](https://github.com/phedoreanu/rpi-temp-lcd/raw/master/RPI3-AM2302-LCD-Wiring-Diagram.png "Wiring diagram")

## Running
`$ docker run -d --restart unless-stopped --device /dev/mem:/dev/mem --privileged phedoreanu/rpi-temp-lcd`

## Building
```bash
$ git clone https://github.com/phedoreanu/rpi-temp-lcd.git
$ cd rpi-temp-lcd/
$ docker build -t phedoreanu/rpi-temp-lcd .
```

## Pushing to DockerHub
`$ docker push phedoreanu/rpi-temp-lcd`

## Debug running container
`$ docker exec -it <container-name/id> /bin/sh`
