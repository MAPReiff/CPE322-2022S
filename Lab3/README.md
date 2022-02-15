# Lab 3 - Python
I pledge my honor that I have abided by the Stevens Honor System.
I am performing these actions on my own local machine and not the Raspberry Pi.

## Assignment
![](assets/Lab3.png)

### cd
![](assets/cd.png)

### julian
![](assets/julian.png)

### date_example
![](assets/date_example.png)

### datetime_example
![](assets/datetime_example.png)

### time_example
![](assets/time_example.png)

### sun
![](assets/sun.png)

### moon
![](assets/moon.png)

### coordinates
![](assets/coordinates.png)

### address
![](assets/address.png)

### cpu
On my host machine
![](assets/cpu.png)

On my Raspberry Pi
![](assets/cpu_pi.png)

### battery
![](assets/battery.png)

### documentstats
![](assets/documentstats.png)

## Other
As a basic exercise, I decided to write a [Python script](systemInfo.py) that displays some basic system information including stats about the CPU system memory, SWAP, disk, and battery. I based this of the [cpu.py](https://github.com/kevinwlu/iot/blob/master/lesson3/cpu.py) example from the class repository utilizing [psutil](https://pypi.org/project/psutil/).


On my laptop
![](assets/systemInfo_laptop.png)

On my desktop
![](assets/systemInfo_pc.png)

On my Raspberry Pi
![](assets/systemInfo_pi.png)
Despite SWAP being enabled and functional on the Pi, the stats reported using `psutil` regarding the current SWAP usage are incorrect and do not match what is reported by `htop` or `free -h`. This might be due to how little SWAP space is allocated on the Pi (100 MiB) compared to my desktop (17 GiB) or laptop (8 GiB).