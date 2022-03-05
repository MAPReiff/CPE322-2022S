# Lab 5 - Paho-MQTT

I pledge my honor that I have abided by the Stevens Honor System.

## Assignment

![](assets/Lab5.png)

## Eclipse Mosquitto and Eclipse Paho

### apt install mosquitto mosquitto-clients
![](assets/apt_install_A.png)

### mosquitto_sub -h localhost -v -t "\$SYS/#"
![](assets/mosquitto_sub.png)

### service mosquitto status
![](assets/service_mosquitto_status.png)

### netstat -tln
![](assets/netstat.png)

### mosquitto_sub in two terminals
![](assets/two_terminal_sub.png)

### pip3 install -U paho-mqtt and git clone
![](assets/pip_install_git_clone.png)

### cd iot/lesson5 and client.py
![](assets/cd_iot_clientpy.png)

### python sub, pup, sub-multiple, pub-multiple
![](assets/python_sub_pub.png)

### python subcpu and pubcpu
![](assets/python_subcpu_pubcpu.png)

### subraspi and pubraspi
![](assets/subraspi_pubraspi.png)

## Crossbar.io

### docker version
![](assets/docker_version.png)

### docker images
![](assets/docker_images_pi.png)

As the Raspberry Pi has not been used for Docker prior, there are not many installed images. I run Docker on a home server, which houses many more Docker images and containers.
![](assets/docker_images_server.png)

### docker run hello-world
![](assets/docker_hello-world.png)

### docker run ubuntu
![](assets/docker_ubuntu.png)

### git clone and tree
![](assets/git_clone_tree.png)

### docker pull and docker run crossbar
![](assets/docker_pull_docker_crossbar.png)

### crossbar info in browser
![](assets/crossbar_info.png)

### cd crossbar and cat config.json
![](assets/cd_crossbar_cat_config.png)

### run publish-client and subscribe-client
![](assets/sub_pub_client.png)