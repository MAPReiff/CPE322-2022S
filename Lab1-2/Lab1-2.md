# Labs 1 and 2 - Command Line
I pledge my honor that I have abided by the Stevens Honor System.
I am performing these actions on my own local machine and not the Raspberry Pi.

## Assignment
![](assets/assignment.png)

### hostname
![](assets/hostname.png)

### env
![](assets/env.png)

### ps
![](assets/ps.png)

### pwd
![](assets/pwd.png)

### git clone
![](assets/git_clone.png)

### cd iot, ls and cd
![](assets/cd_iot_ls_cd.png)

### df
![](assets/df.png)

### mkdir demo and cd demo
![](assets/mkdir_cd_demo.png)

### nano file
![](assets/nano.png)

### cat file
![](assets/cat.png)

### cp, mv and rm
![](assets/cp_mv_rm.png)

### clear
![](assets/clear.png)

### man uname
![](assets/man_uname.png)

### uname -a
![](assets/uname-a.png)

### ifconfig
![](assets/ifconfig.png)

### ping localhost
![](assets/ping_localhost.png)

### netstat
The output is too long for a screenshot.
```
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 starship:54110          151.101.210.137:https   ESTABLISHED
tcp        0      0 starship:42618          Google-Home-Mini:32213  ESTABLISHED
tcp      220      0 starship:57998          chungus:netbios-ssn     ESTABLISHED
tcp        0      0 starship:47288          192.168.1.232:nvme-disc ESTABLISHED
tcp        0   1204 10.108.209.15:46048     47.224.186.35.bc.:https ESTABLISHED
tcp        0      0 starship:37532          lga25s74-in-f8.1e:https ESTABLISHED
tcp        0      0 starship:39226          143.244.210.202:https   TIME_WAIT  
tcp        0      0 starship:33716          Google-Nest-M:nvme-disc ESTABLISHED
tcp        0      0 starship:42550          162.159.133.232:https   ESTABLISHED
tcp        0      0 starship:57222          104.244.42.129:https    ESTABLISHED
tcp        0      0 starship:50566          lb-140-82-114-25-:https ESTABLISHED
tcp        0      0 starship:39356          185-70-42-25.prot:https ESTABLISHED
tcp        0      0 starship:51896          ec2-54-90-223-72.:https ESTABLISHED
tcp        0      0 starship:39176          53.16.211.130.bc.:https ESTABLISHED
tcp        0      0 starship:39228          143.244.210.202:https   TIME_WAIT  
tcp        0      0 starship:42242          104.16.95.65:https      ESTABLISHED
tcp        0      0 starship:51898          ec2-54-90-223-72.:https ESTABLISHED
tcp        0      0 starship:47686          lga25s78-in-f14.1:https ESTABLISHED
tcp        0      0 starship:37422          Google-Home-Mini:32056  ESTABLISHED
tcp        0      0 starship:40886          40.71.11.167:https      ESTABLISHED
tcp        0      0 starship:35380          server-13-225-231:https ESTABLISHED
tcp        0      0 starship:55834          mreiff.dev:microsoft-ds ESTABLISHED
tcp        0      0 starship:40326          162.159.130.234:https   ESTABLISHED
tcp        0      0 starship:40968          104.18.12.33:https      ESTABLISHED
tcp        0      0 starship:55502          70.28.209.35.bc.g:https ESTABLISHED
tcp        0      0 starship:32972          Chromecast-Ul:nvme-disc ESTABLISHED
tcp        0      0 starship:54766          Google-Home-M:nvme-disc ESTABLISHED
tcp        0      0 starship:37964          ec2-54-68-158-125:https ESTABLISHED
tcp        0      0 starship:55266          ec2-34-199-187-11:https ESTABLISHED
tcp        0      0 starship:40930          104.21.59.235:https     ESTABLISHED
udp        0      0 starship:50387          lga34s38-in-f10.1:https ESTABLISHED
udp        0      0 starship:38718          lga34s34-in-f10.1:https ESTABLISHED
udp        0      0 starship:58810          lga34s34-in-f3.1e:https ESTABLISHED
udp        0      0 starship:bootpc         G3100.myfiosgate:bootps ESTABLISHED
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ]         DGRAM                    34057    /run/user/1000/systemd/notify
unix  4      [ ]         DGRAM      CONNECTED     27720    /run/systemd/notify
unix  16     [ ]         DGRAM      CONNECTED     21016    @var/run/nvidia-xdriver-d5b75fea@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
unix  18     [ ]         DGRAM      CONNECTED     20518    /run/systemd/journal/dev-log
unix  10     [ ]         DGRAM      CONNECTED     20520    /run/systemd/journal/socket
unix  3      [ ]         SEQPACKET  CONNECTED     43567    @0000d
unix  3      [ ]         SEQPACKET  CONNECTED     113357   @0001f
unix  3      [ ]         SEQPACKET  CONNECTED     43581    @0000e
unix  3      [ ]         SEQPACKET  CONNECTED     113355   @0001e
unix  3      [ ]         SEQPACKET  CONNECTED     43583    @0000f
unix  3      [ ]         SEQPACKET  CONNECTED     43566    @0000a
unix  3      [ ]         SEQPACKET  CONNECTED     46752    @0000b
unix  3      [ ]         SEQPACKET  CONNECTED     46753    @0000c
unix  2      [ ]         DGRAM                    21017    /var/run/nvidia-xdriver-d5b75fea
unix  3      [ ]         SEQPACKET  CONNECTED     37033    @00004
unix  3      [ ]         SEQPACKET  CONNECTED     25482    @00005
unix  3      [ ]         SEQPACKET  CONNECTED     34440    @00006
unix  2      [ ]         DGRAM                    21828    @00001
unix  3      [ ]         SEQPACKET  CONNECTED     25484    @00007
unix  3      [ ]         SEQPACKET  CONNECTED     42511    @00011
unix  3      [ ]         SEQPACKET  CONNECTED     42509    @00010
unix  3      [ ]         SEQPACKET  CONNECTED     35476    @00008
unix  3      [ ]         SEQPACKET  CONNECTED     35477    @00009
unix  3      [ ]         STREAM     CONNECTED     122311   
unix  3      [ ]         STREAM     CONNECTED     112465   /run/user/1000/gvfsd/socket-zBE7PNgx
unix  3      [ ]         STREAM     CONNECTED     111741   
unix  3      [ ]         STREAM     CONNECTED     59286    
unix  3      [ ]         STREAM     CONNECTED     34463    
unix  3      [ ]         STREAM     CONNECTED     34416    
unix  3      [ ]         STREAM     CONNECTED     21109    
unix  3      [ ]         STREAM     CONNECTED     33092    
unix  3      [ ]         STREAM     CONNECTED     15206    
unix  3      [ ]         STREAM     CONNECTED     126341   
unix  3      [ ]         STREAM     CONNECTED     108388   
unix  3      [ ]         STREAM     CONNECTED     108065   
unix  3      [ ]         STREAM     CONNECTED     80446    
unix  3      [ ]         STREAM     CONNECTED     37590    
unix  3      [ ]         STREAM     CONNECTED     50557    
unix  3      [ ]         STREAM     CONNECTED     50595    
unix  3      [ ]         STREAM     CONNECTED     46810    
unix  3      [ ]         STREAM     CONNECTED     44932    
unix  3      [ ]         SEQPACKET  CONNECTED     39251    
unix  3      [ ]         STREAM     CONNECTED     35297    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     26314    
unix  3      [ ]         STREAM     CONNECTED     143390   
unix  3      [ ]         STREAM     CONNECTED     43706    
unix  3      [ ]         STREAM     CONNECTED     38751    
unix  3      [ ]         STREAM     CONNECTED     22116    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     84699    
unix  3      [ ]         STREAM     CONNECTED     34684    
unix  3      [ ]         SEQPACKET  CONNECTED     42506    
unix  3      [ ]         STREAM     CONNECTED     40455    
unix  3      [ ]         STREAM     CONNECTED     34489    
unix  3      [ ]         STREAM     CONNECTED     37040    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     21145    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     35862    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     28001    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     115308   
unix  3      [ ]         STREAM     CONNECTED     117822   
unix  3      [ ]         STREAM     CONNECTED     43219    
unix  3      [ ]         STREAM     CONNECTED     31526    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     28163    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     34660    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     43509    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     26565    
unix  3      [ ]         STREAM     CONNECTED     121235   
unix  3      [ ]         STREAM     CONNECTED     121234   
unix  3      [ ]         STREAM     CONNECTED     83994    
unix  3      [ ]         STREAM     CONNECTED     34657    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     45088    
unix  3      [ ]         STREAM     CONNECTED     14132    
unix  3      [ ]         STREAM     CONNECTED     37927    
unix  3      [ ]         STREAM     CONNECTED     33030    
unix  3      [ ]         STREAM     CONNECTED     16221    
unix  3      [ ]         STREAM     CONNECTED     11945    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25995    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     116416   
unix  3      [ ]         STREAM     CONNECTED     112384   
unix  3      [ ]         STREAM     CONNECTED     93181    
unix  3      [ ]         SEQPACKET  CONNECTED     50444    
unix  3      [ ]         STREAM     CONNECTED     21185    
unix  3      [ ]         STREAM     CONNECTED     14324    /run/user/1000/at-spi2-ML4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     34397    
unix  3      [ ]         STREAM     CONNECTED     120421   
unix  3      [ ]         STREAM     CONNECTED     46814    
unix  3      [ ]         STREAM     CONNECTED     26426    
unix  3      [ ]         STREAM     CONNECTED     115171   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     38870    
unix  3      [ ]         STREAM     CONNECTED     31527    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     84714    
unix  3      [ ]         SEQPACKET  CONNECTED     36634    
unix  3      [ ]         STREAM     CONNECTED     34353    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     25310    
unix  3      [ ]         STREAM     CONNECTED     21100    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     28157    
unix  3      [ ]         STREAM     CONNECTED     28145    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     12198    
unix  3      [ ]         STREAM     CONNECTED     22096    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     16207    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     128837   
unix  3      [ ]         STREAM     CONNECTED     93681    
unix  3      [ ]         STREAM     CONNECTED     89439    
unix  3      [ ]         STREAM     CONNECTED     67329    
unix  3      [ ]         STREAM     CONNECTED     55761    
unix  3      [ ]         STREAM     CONNECTED     34745    
unix  3      [ ]         STREAM     CONNECTED     26475    
unix  3      [ ]         SEQPACKET  CONNECTED     110991   
unix  3      [ ]         STREAM     CONNECTED     49593    
unix  3      [ ]         STREAM     CONNECTED     53555    
unix  3      [ ]         STREAM     CONNECTED     49310    
unix  3      [ ]         STREAM     CONNECTED     36167    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     32497    /run/user/1000/bus
unix  2      [ ]         DGRAM      CONNECTED     36558    
unix  3      [ ]         STREAM     CONNECTED     26585    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     40971    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     35463    
unix  3      [ ]         STREAM     CONNECTED     13026    
unix  3      [ ]         STREAM     CONNECTED     126342   
unix  3      [ ]         STREAM     CONNECTED     97725    
unix  3      [ ]         STREAM     CONNECTED     56888    
unix  3      [ ]         STREAM     CONNECTED     122365   
unix  2      [ ]         STREAM     CONNECTED     112379   
unix  3      [ ]         STREAM     CONNECTED     92199    
unix  3      [ ]         STREAM     CONNECTED     34431    
unix  3      [ ]         STREAM     CONNECTED     38175    /run/user/1000/at-spi2-373IH1/socket
unix  3      [ ]         STREAM     CONNECTED     21150    
unix  3      [ ]         STREAM     CONNECTED     136808   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     111332   @/tmp/.X11-unix/X0
unix  3      [ ]         SEQPACKET  CONNECTED     43578    
unix  3      [ ]         STREAM     CONNECTED     14047    
unix  3      [ ]         STREAM     CONNECTED     52256    
unix  3      [ ]         STREAM     CONNECTED     37097    
unix  3      [ ]         STREAM     CONNECTED     37096    
unix  3      [ ]         STREAM     CONNECTED     26320    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     35295    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     25987    
unix  3      [ ]         STREAM     CONNECTED     115311   
unix  3      [ ]         STREAM     CONNECTED     117377   
unix  3      [ ]         STREAM     CONNECTED     55012    
unix  3      [ ]         STREAM     CONNECTED     51410    
unix  3      [ ]         SEQPACKET  CONNECTED     43314    
unix  3      [ ]         STREAM     CONNECTED     22159    
unix  3      [ ]         STREAM     CONNECTED     36121    
unix  3      [ ]         STREAM     CONNECTED     128116   
unix  3      [ ]         STREAM     CONNECTED     108226   /run/user/1000/vscode-ipc-3e97e5fb-a743-4397-99fe-fe2be3be87bb.sock
unix  3      [ ]         STREAM     CONNECTED     117415   
unix  3      [ ]         STREAM     CONNECTED     45983    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     61595    
unix  3      [ ]         STREAM     CONNECTED     36550    
unix  3      [ ]         STREAM     CONNECTED     34528    
unix  3      [ ]         STREAM     CONNECTED     34488    
unix  3      [ ]         STREAM     CONNECTED     36170    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     26317    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     51406    
unix  3      [ ]         STREAM     CONNECTED     37485    
unix  3      [ ]         STREAM     CONNECTED     34658    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     45511    
unix  3      [ ]         STREAM     CONNECTED     35298    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     35587    
unix  3      [ ]         STREAM     CONNECTED     37226    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     30702    
unix  3      [ ]         STREAM     CONNECTED     26607    
unix  3      [ ]         STREAM     CONNECTED     120152   
unix  3      [ ]         STREAM     CONNECTED     32451    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     98887    
unix  3      [ ]         STREAM     CONNECTED     112383   
unix  3      [ ]         STREAM     CONNECTED     69459    
unix  3      [ ]         STREAM     CONNECTED     63523    /run/user/1000/gvfsd/socket-DSWyeFlm
unix  3      [ ]         STREAM     CONNECTED     34515    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31494    /run/user/1000/at-spi2-JM4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     34370    
unix  3      [ ]         STREAM     CONNECTED     26318    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     119545   
unix  3      [ ]         STREAM     CONNECTED     113491   
unix  3      [ ]         STREAM     CONNECTED     46942    
unix  3      [ ]         STREAM     CONNECTED     38831    
unix  3      [ ]         STREAM     CONNECTED     13975    
unix  3      [ ]         STREAM     CONNECTED     26006    
unix  3      [ ]         STREAM     CONNECTED     119044   
unix  3      [ ]         STREAM     CONNECTED     89518    
unix  3      [ ]         STREAM     CONNECTED     89436    
unix  3      [ ]         STREAM     CONNECTED     59497    
unix  3      [ ]         STREAM     CONNECTED     34713    
unix  3      [ ]         STREAM     CONNECTED     34661    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     117419   
unix  3      [ ]         STREAM     CONNECTED     105098   
unix  3      [ ]         STREAM     CONNECTED     94391    
unix  3      [ ]         STREAM     CONNECTED     54358    
unix  3      [ ]         STREAM     CONNECTED     49051    
unix  3      [ ]         STREAM     CONNECTED     36795    
unix  3      [ ]         STREAM     CONNECTED     36561    
unix  3      [ ]         STREAM     CONNECTED     40006    
unix  3      [ ]         STREAM     CONNECTED     28159    
unix  3      [ ]         STREAM     CONNECTED     12200    
unix  3      [ ]         STREAM     CONNECTED     13278    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     18098    
unix  2      [ ]         DGRAM      CONNECTED     24858    
unix  3      [ ]         STREAM     CONNECTED     30035    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     49287    
unix  3      [ ]         STREAM     CONNECTED     35501    
unix  2      [ ]         DGRAM      CONNECTED     41801    
unix  3      [ ]         SEQPACKET  CONNECTED     41781    
unix  3      [ ]         STREAM     CONNECTED     31513    
unix  3      [ ]         STREAM     CONNECTED     36154    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     49600    
unix  3      [ ]         STREAM     CONNECTED     49494    
unix  3      [ ]         STREAM     CONNECTED     34678    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     35410    
unix  3      [ ]         STREAM     CONNECTED     119510   
unix  3      [ ]         STREAM     CONNECTED     52568    
unix  3      [ ]         STREAM     CONNECTED     52257    
unix  3      [ ]         STREAM     CONNECTED     37230    
unix  3      [ ]         STREAM     CONNECTED     37087    
unix  2      [ ]         DGRAM      CONNECTED     25999    
unix  2      [ ]         DGRAM      CONNECTED     16513    
unix  3      [ ]         STREAM     CONNECTED     109170   
unix  3      [ ]         STREAM     CONNECTED     114000   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     49278    /run/user/1000/bus
unix  2      [ ]         DGRAM      CONNECTED     13762    
unix  3      [ ]         STREAM     CONNECTED     111331   
unix  3      [ ]         STREAM     CONNECTED     111114   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     93134    
unix  3      [ ]         STREAM     CONNECTED     21184    
unix  3      [ ]         STREAM     CONNECTED     39064    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     34432    
unix  3      [ ]         STREAM     CONNECTED     35868    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     80114    
unix  3      [ ]         STREAM     CONNECTED     51008    
unix  3      [ ]         STREAM     CONNECTED     37571    
unix  3      [ ]         STREAM     CONNECTED     50213    
unix  3      [ ]         STREAM     CONNECTED     48968    
unix  3      [ ]         STREAM     CONNECTED     48951    
unix  3      [ ]         STREAM     CONNECTED     53469    
unix  3      [ ]         STREAM     CONNECTED     26538    
unix  3      [ ]         STREAM     CONNECTED     139560   
unix  3      [ ]         STREAM     CONNECTED     120980   
unix  3      [ ]         STREAM     CONNECTED     110999   
unix  3      [ ]         STREAM     CONNECTED     31608    
unix  3      [ ]         STREAM     CONNECTED     38796    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     22099    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26288    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     31297    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     13833    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     119847   
unix  3      [ ]         STREAM     CONNECTED     84700    
unix  3      [ ]         STREAM     CONNECTED     61522    
unix  3      [ ]         STREAM     CONNECTED     39732    
unix  3      [ ]         STREAM     CONNECTED     39716    
unix  3      [ ]         STREAM     CONNECTED     35681    
unix  3      [ ]         STREAM     CONNECTED     34513    
unix  3      [ ]         STREAM     CONNECTED     36223    
unix  3      [ ]         STREAM     CONNECTED     26322    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     115312   
unix  3      [ ]         STREAM     CONNECTED     116225   /run/user/1000/at-spi2-RSWMH1/socket
unix  3      [ ]         STREAM     CONNECTED     43248    
unix  3      [ ]         STREAM     CONNECTED     43247    
unix  3      [ ]         STREAM     CONNECTED     26315    
unix  3      [ ]         STREAM     CONNECTED     113554   
unix  3      [ ]         STREAM     CONNECTED     113397   
unix  3      [ ]         STREAM     CONNECTED     45077    
unix  2      [ ]         DGRAM      CONNECTED     34008    
unix  3      [ ]         STREAM     CONNECTED     140419   
unix  3      [ ]         STREAM     CONNECTED     116373   
unix  3      [ ]         STREAM     CONNECTED     93180    
unix  3      [ ]         STREAM     CONNECTED     115910   
unix  3      [ ]         STREAM     CONNECTED     78285    
unix  3      [ ]         STREAM     CONNECTED     73312    
unix  3      [ ]         SEQPACKET  CONNECTED     31613    
unix  3      [ ]         STREAM     CONNECTED     34407    
unix  3      [ ]         STREAM     CONNECTED     35317    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     34232    
unix  3      [ ]         STREAM     CONNECTED     13307    /run/user/1000/bus
unix  2      [ ]         DGRAM      CONNECTED     39571    
unix  3      [ ]         STREAM     CONNECTED     49614    
unix  3      [ ]         STREAM     CONNECTED     53564    
unix  3      [ ]         STREAM     CONNECTED     36122    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     41810    
unix  3      [ ]         STREAM     CONNECTED     40974    /run/dbus/system_bus_socket
unix  3      [ ]         SEQPACKET  CONNECTED     25485    
unix  3      [ ]         STREAM     CONNECTED     12220    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     31337    
unix  3      [ ]         STREAM     CONNECTED     104978   
unix  3      [ ]         STREAM     CONNECTED     55173    
unix  3      [ ]         STREAM     CONNECTED     49461    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     54282    
unix  3      [ ]         STREAM     CONNECTED     39717    
unix  3      [ ]         STREAM     CONNECTED     40453    
unix  3      [ ]         STREAM     CONNECTED     25322    
unix  3      [ ]         STREAM     CONNECTED     36163    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     25313    
unix  3      [ ]         STREAM     CONNECTED     28106    
unix  3      [ ]         STREAM     CONNECTED     13828    /run/dbus/system_bus_socket
unix  2      [ ]         DGRAM                    118258   
unix  3      [ ]         STREAM     CONNECTED     117413   
unix  3      [ ]         STREAM     CONNECTED     104808   
unix  3      [ ]         STREAM     CONNECTED     93679    
unix  3      [ ]         STREAM     CONNECTED     67328    
unix  3      [ ]         STREAM     CONNECTED     13308    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     125375   
unix  3      [ ]         STREAM     CONNECTED     113992   
unix  3      [ ]         STREAM     CONNECTED     104807   
unix  3      [ ]         STREAM     CONNECTED     43709    
unix  3      [ ]         STREAM     CONNECTED     22907    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     117752   /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     46890    
unix  3      [ ]         STREAM     CONNECTED     52254    
unix  3      [ ]         STREAM     CONNECTED     48312    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     44857    
unix  3      [ ]         STREAM     CONNECTED     39193    
unix  3      [ ]         STREAM     CONNECTED     37086    
unix  3      [ ]         STREAM     CONNECTED     35296    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     26312    
unix  3      [ ]         STREAM     CONNECTED     30085    
unix  3      [ ]         STREAM     CONNECTED     104186   
unix  2      [ ]         DGRAM      CONNECTED     115929   
unix  3      [ ]         STREAM     CONNECTED     103931   
unix  3      [ ]         STREAM     CONNECTED     56993    
unix  3      [ ]         STREAM     CONNECTED     37583    
unix  3      [ ]         STREAM     CONNECTED     140439   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     59030    
unix  3      [ ]         STREAM     CONNECTED     38170    /run/user/1000/at-spi2-LP4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     21097    
unix  3      [ ]         STREAM     CONNECTED     110998   
unix  3      [ ]         STREAM     CONNECTED     45648    
unix  3      [ ]         STREAM     CONNECTED     38003    
unix  3      [ ]         STREAM     CONNECTED     32502    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     33091    
unix  3      [ ]         STREAM     CONNECTED     12194    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     22094    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     53592    
unix  3      [ ]         STREAM     CONNECTED     48825    
unix  3      [ ]         STREAM     CONNECTED     35588    
unix  3      [ ]         STREAM     CONNECTED     30650    
unix  3      [ ]         STREAM     CONNECTED     26557    
unix  3      [ ]         STREAM     CONNECTED     115315   
unix  3      [ ]         STREAM     CONNECTED     51455    
unix  3      [ ]         STREAM     CONNECTED     31525    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     35403    
unix  3      [ ]         STREAM     CONNECTED     12213    @/tmp/.X11-unix/X0
unix  2      [ ]         DGRAM      CONNECTED     21829    
unix  3      [ ]         STREAM     CONNECTED     105099   
unix  3      [ ]         STREAM     CONNECTED     60944    
unix  3      [ ]         STREAM     CONNECTED     39735    
unix  3      [ ]         STREAM     CONNECTED     42629    
unix  3      [ ]         STREAM     CONNECTED     43237    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     34492    
unix  3      [ ]         STREAM     CONNECTED     44129    /run/user/1000/at-spi2-2UDOH1/socket
unix  3      [ ]         STREAM     CONNECTED     39964    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     36172    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     14051    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     114003   
unix  3      [ ]         SEQPACKET  CONNECTED     113352   
unix  3      [ ]         STREAM     CONNECTED     46919    
unix  3      [ ]         STREAM     CONNECTED     39252    
unix  3      [ ]         STREAM     CONNECTED     33424    
unix  3      [ ]         DGRAM      CONNECTED     13978    
unix  3      [ ]         STREAM     CONNECTED     30034    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     120422   
unix  3      [ ]         STREAM     CONNECTED     99268    
unix  3      [ ]         STREAM     CONNECTED     93182    
unix  3      [ ]         STREAM     CONNECTED     115913   
unix  3      [ ]         STREAM     CONNECTED     73309    
unix  3      [ ]         STREAM     CONNECTED     61640    /run/user/1000/gvfsd/socket-auy4d9Vu
unix  3      [ ]         STREAM     CONNECTED     50443    
unix  3      [ ]         STREAM     CONNECTED     21478    
unix  3      [ ]         STREAM     CONNECTED     12236    /run/user/1000/at-spi2-OJ4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     34362    
unix  3      [ ]         STREAM     CONNECTED     50593    
unix  3      [ ]         STREAM     CONNECTED     37114    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     42095    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     37076    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     36178    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     37911    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     49615    
unix  3      [ ]         STREAM     CONNECTED     54284    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     14010    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     117412   
unix  3      [ ]         STREAM     CONNECTED     93646    
unix  3      [ ]         STREAM     CONNECTED     56210    
unix  3      [ ]         STREAM     CONNECTED     34738    
unix  3      [ ]         STREAM     CONNECTED     51411    
unix  3      [ ]         STREAM     CONNECTED     34715    
unix  3      [ ]         STREAM     CONNECTED     36314    
unix  3      [ ]         STREAM     CONNECTED     30563    
unix  3      [ ]         STREAM     CONNECTED     131535   
unix  3      [ ]         STREAM     CONNECTED     131534   
unix  3      [ ]         STREAM     CONNECTED     117616   /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     104933   
unix  3      [ ]         STREAM     CONNECTED     34699    @/tmp/.X11-unix/X0
unix  3      [ ]         SEQPACKET  CONNECTED     36640    
unix  3      [ ]         STREAM     CONNECTED     12246    
unix  3      [ ]         STREAM     CONNECTED     31334    
unix  3      [ ]         STREAM     CONNECTED     36128    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     34225    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     28113    
unix  3      [ ]         STREAM     CONNECTED     33020    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     25153    
unix  3      [ ]         STREAM     CONNECTED     138530   
unix  3      [ ]         STREAM     CONNECTED     57944    
unix  3      [ ]         STREAM     CONNECTED     53058    /run/user/1000/gvfsd/socket-sL2sbxwK
unix  3      [ ]         STREAM     CONNECTED     39603    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12257    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     36280    
unix  3      [ ]         STREAM     CONNECTED     34376    /run/user/1000/bus
unix  2      [ ]         DGRAM                    32525    
unix  3      [ ]         STREAM     CONNECTED     32845    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     119056   
unix  3      [ ]         STREAM     CONNECTED     83077    
unix  3      [ ]         STREAM     CONNECTED     51412    
unix  3      [ ]         STREAM     CONNECTED     54291    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     46090    /run/user/1000/at-spi2-JLFBH1/socket
unix  3      [ ]         STREAM     CONNECTED     22095    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     49595    
unix  3      [ ]         STREAM     CONNECTED     53552    
unix  3      [ ]         STREAM     CONNECTED     34679    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     26604    
unix  3      [ ]         STREAM     CONNECTED     30648    
unix  3      [ ]         STREAM     CONNECTED     45631    
unix  3      [ ]         STREAM     CONNECTED     31602    
unix  3      [ ]         STREAM     CONNECTED     33027    
unix  3      [ ]         STREAM     CONNECTED     21049    
unix  3      [ ]         STREAM     CONNECTED     143529   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     133146   
unix  3      [ ]         STREAM     CONNECTED     59285    
unix  3      [ ]         STREAM     CONNECTED     59065    
unix  3      [ ]         STREAM     CONNECTED     68988    
unix  3      [ ]         STREAM     CONNECTED     42107    
unix  3      [ ]         STREAM     CONNECTED     21457    
unix  3      [ ]         STREAM     CONNECTED     34417    
unix  3      [ ]         STREAM     CONNECTED     34423    /run/user/1000/at-spi2-HN4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     34186    
unix  3      [ ]         STREAM     CONNECTED     108389   
unix  3      [ ]         STREAM     CONNECTED     65576    /run/user/1000/gvfsd/socket-o1eQopvg
unix  3      [ ]         STREAM     CONNECTED     46816    
unix  3      [ ]         STREAM     CONNECTED     37079    
unix  3      [ ]         STREAM     CONNECTED     33703    /run/user/1000/at-spi2-55HPH1/socket
unix  3      [ ]         STREAM     CONNECTED     35458    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     26021    
unix  2      [ ]         DGRAM      CONNECTED     30058    
unix  3      [ ]         STREAM     CONNECTED     26002    
unix  3      [ ]         STREAM     CONNECTED     43714    
unix  3      [ ]         STREAM     CONNECTED     13827    
unix  3      [ ]         STREAM     CONNECTED     13829    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     62841    /run/user/1000/gvfsd/socket-hjIvANBI
unix  3      [ ]         STREAM     CONNECTED     42644    
unix  3      [ ]         STREAM     CONNECTED     40451    
unix  3      [ ]         SEQPACKET  CONNECTED     37034    
unix  3      [ ]         STREAM     CONNECTED     36173    
unix  3      [ ]         STREAM     CONNECTED     36166    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     28170    
unix  3      [ ]         STREAM     CONNECTED     12216    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     12211    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     14008    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     19938    
unix  3      [ ]         STREAM     CONNECTED     31034    
unix  3      [ ]         STREAM     CONNECTED     118620   
unix  3      [ ]         STREAM     CONNECTED     104922   
unix  2      [ ]         DGRAM                    75792    
unix  3      [ ]         STREAM     CONNECTED     34728    
unix  3      [ ]         STREAM     CONNECTED     34685    
unix  3      [ ]         STREAM     CONNECTED     31561    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     49616    
unix  3      [ ]         STREAM     CONNECTED     35291    
unix  3      [ ]         STREAM     CONNECTED     35246    
unix  3      [ ]         STREAM     CONNECTED     39812    
unix  3      [ ]         STREAM     CONNECTED     54287    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     31603    
unix  3      [ ]         STREAM     CONNECTED     38836    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     35478    
unix  3      [ ]         SEQPACKET  CONNECTED     35433    
unix  3      [ ]         STREAM     CONNECTED     123294   
unix  3      [ ]         STREAM     CONNECTED     116374   
unix  3      [ ]         STREAM     CONNECTED     112414   
unix  3      [ ]         STREAM     CONNECTED     115944   
unix  3      [ ]         STREAM     CONNECTED     115911   
unix  3      [ ]         STREAM     CONNECTED     111740   
unix  3      [ ]         STREAM     CONNECTED     21178    /run/user/1000/at-spi2-2Z1IH1/socket
unix  3      [ ]         STREAM     CONNECTED     120536   
unix  3      [ ]         STREAM     CONNECTED     80447    
unix  3      [ ]         STREAM     CONNECTED     44145    
unix  3      [ ]         STREAM     CONNECTED     30069    
unix  3      [ ]         STREAM     CONNECTED     113495   /run/user/1000/discord-ipc-0
unix  3      [ ]         STREAM     CONNECTED     114147   
unix  3      [ ]         STREAM     CONNECTED     113133   
unix  3      [ ]         STREAM     CONNECTED     47544    
unix  3      [ ]         STREAM     CONNECTED     37232    
unix  3      [ ]         STREAM     CONNECTED     42100    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     34355    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     115309   
unix  3      [ ]         STREAM     CONNECTED     117411   
unix  3      [ ]         STREAM     CONNECTED     117766   
unix  3      [ ]         STREAM     CONNECTED     43913    
unix  3      [ ]         STREAM     CONNECTED     34749    
unix  3      [ ]         STREAM     CONNECTED     45803    
unix  3      [ ]         STREAM     CONNECTED     51454    
unix  3      [ ]         STREAM     CONNECTED     28155    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     30509    
unix  3      [ ]         STREAM     CONNECTED     117937   /run/user/1000/gvfsd/socket-fsMlgjgu
unix  3      [ ]         STREAM     CONNECTED     60946    
unix  3      [ ]         STREAM     CONNECTED     54290    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     34675    
unix  3      [ ]         STREAM     CONNECTED     36553    
unix  3      [ ]         STREAM     CONNECTED     38837    /run/dbus/system_bus_socket
unix  3      [ ]         SEQPACKET  CONNECTED     25483    
unix  3      [ ]         STREAM     CONNECTED     32520    
unix  3      [ ]         STREAM     CONNECTED     33095    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     121299   
unix  3      [ ]         SEQPACKET  CONNECTED     111001   
unix  3      [ ]         STREAM     CONNECTED     110987   
unix  3      [ ]         STREAM     CONNECTED     51407    
unix  3      [ ]         STREAM     CONNECTED     45630    
unix  3      [ ]         STREAM     CONNECTED     37465    
unix  3      [ ]         SEQPACKET  CONNECTED     31544    
unix  3      [ ]         STREAM     CONNECTED     14272    
unix  3      [ ]         STREAM     CONNECTED     20852    
unix  3      [ ]         STREAM     CONNECTED     50589    
unix  3      [ ]         STREAM     CONNECTED     53565    
unix  3      [ ]         STREAM     CONNECTED     53550    
unix  3      [ ]         STREAM     CONNECTED     49297    
unix  3      [ ]         STREAM     CONNECTED     37089    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     26477    
unix  3      [ ]         STREAM     CONNECTED     103932   
unix  3      [ ]         STREAM     CONNECTED     61598    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     114361   
unix  3      [ ]         STREAM     CONNECTED     59044    
unix  3      [ ]         STREAM     CONNECTED     52677    
unix  3      [ ]         STREAM     CONNECTED     21456    
unix  3      [ ]         STREAM     CONNECTED     34405    
unix  3      [ ]         STREAM     CONNECTED     33445    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     34116    
unix  3      [ ]         STREAM     CONNECTED     109000   
unix  3      [ ]         STREAM     CONNECTED     43710    
unix  3      [ ]         DGRAM      CONNECTED     13979    
unix  3      [ ]         DGRAM      CONNECTED     13767    
unix  3      [ ]         STREAM     CONNECTED     113362   
unix  3      [ ]         STREAM     CONNECTED     46918    
unix  2      [ ]         DGRAM      CONNECTED     39572    
unix  3      [ ]         STREAM     CONNECTED     39253    
unix  3      [ ]         STREAM     CONNECTED     44136    
unix  3      [ ]         STREAM     CONNECTED     34217    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     21845    /var/run/docker/containerd/containerd.sock
unix  3      [ ]         STREAM     CONNECTED     113359   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     89519    
unix  3      [ ]         STREAM     CONNECTED     48309    
unix  3      [ ]         STREAM     CONNECTED     34221    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     128799   
unix  3      [ ]         STREAM     CONNECTED     112462   
unix  3      [ ]         STREAM     CONNECTED     94390    
unix  3      [ ]         STREAM     CONNECTED     57910    
unix  3      [ ]         STREAM     CONNECTED     54283    
unix  3      [ ]         STREAM     CONNECTED     42645    
unix  3      [ ]         STREAM     CONNECTED     40344    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     36126    
unix  3      [ ]         STREAM     CONNECTED     25279    
unix  3      [ ]         STREAM     CONNECTED     13310    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31321    
unix  3      [ ]         STREAM     CONNECTED     31318    
unix  3      [ ]         STREAM     CONNECTED     11963    
unix  3      [ ]         STREAM     CONNECTED     35504    
unix  3      [ ]         STREAM     CONNECTED     31607    
unix  3      [ ]         STREAM     CONNECTED     41797    
unix  3      [ ]         STREAM     CONNECTED     35479    
unix  3      [ ]         STREAM     CONNECTED     37920    
unix  3      [ ]         STREAM     CONNECTED     33004    
unix  3      [ ]         STREAM     CONNECTED     121016   
unix  3      [ ]         STREAM     CONNECTED     22194    /run/user/1000/at-spi2-7Y1IH1/socket
unix  3      [ ]         STREAM     CONNECTED     35409    
unix  3      [ ]         STREAM     CONNECTED     116220   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     37118    
unix  3      [ ]         STREAM     CONNECTED     34412    
unix  3      [ ]         STREAM     CONNECTED     135150   
unix  3      [ ]         STREAM     CONNECTED     132535   
unix  3      [ ]         STREAM     CONNECTED     115933   
unix  2      [ ]         DGRAM      CONNECTED     115930   
unix  3      [ ]         STREAM     CONNECTED     56886    
unix  3      [ ]         STREAM     CONNECTED     64543    
unix  3      [ ]         STREAM     CONNECTED     50480    
unix  3      [ ]         STREAM     CONNECTED     50218    
unix  3      [ ]         STREAM     CONNECTED     21112    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     62994    
unix  3      [ ]         STREAM     CONNECTED     38871    
unix  3      [ ]         STREAM     CONNECTED     38333    
unix  3      [ ]         STREAM     CONNECTED     33094    
unix  3      [ ]         STREAM     CONNECTED     50874    
unix  3      [ ]         STREAM     CONNECTED     44964    
unix  3      [ ]         STREAM     CONNECTED     53591    
unix  3      [ ]         STREAM     CONNECTED     49601    
unix  3      [ ]         STREAM     CONNECTED     53544    
unix  3      [ ]         STREAM     CONNECTED     51334    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     40449    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     26524    
unix  3      [ ]         STREAM     CONNECTED     45527    
unix  3      [ ]         STREAM     CONNECTED     37095    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     40433    
unix  3      [ ]         STREAM     CONNECTED     14266    
unix  3      [ ]         STREAM     CONNECTED     26292    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     20861    
unix  3      [ ]         STREAM     CONNECTED     60912    
unix  3      [ ]         STREAM     CONNECTED     51405    
unix  3      [ ]         STREAM     CONNECTED     42631    
unix  3      [ ]         STREAM     CONNECTED     37477    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     42089    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     36277    
unix  3      [ ]         STREAM     CONNECTED     36200    
unix  3      [ ]         STREAM     CONNECTED     38975    
unix  3      [ ]         STREAM     CONNECTED     25314    
unix  3      [ ]         STREAM     CONNECTED     32503    
unix  3      [ ]         STREAM     CONNECTED     117825   
unix  3      [ ]         STREAM     CONNECTED     104921   
unix  3      [ ]         STREAM     CONNECTED     83076    
unix  3      [ ]         STREAM     CONNECTED     34733    
unix  3      [ ]         STREAM     CONNECTED     30618    
unix  3      [ ]         STREAM     CONNECTED     32499    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     119341   
unix  3      [ ]         STREAM     CONNECTED     118845   
unix  2      [ ]         STREAM     CONNECTED     117916   
unix  3      [ ]         STREAM     CONNECTED     39710    
unix  3      [ ]         STREAM     CONNECTED     39575    
unix  3      [ ]         STREAM     CONNECTED     41858    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     37072    
unix  3      [ ]         STREAM     CONNECTED     37914    /run/user/1000/bus
unix  2      [ ]         DGRAM      CONNECTED     25774    
unix  3      [ ]         STREAM     CONNECTED     43716    
unix  3      [ ]         STREAM     CONNECTED     13799    
unix  3      [ ]         DGRAM      CONNECTED     13769    
unix  3      [ ]         STREAM     CONNECTED     122364   
unix  3      [ ]         STREAM     CONNECTED     120602   
unix  3      [ ]         STREAM     CONNECTED     113996   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     96357    
unix  3      [ ]         STREAM     CONNECTED     92201    
unix  3      [ ]         STREAM     CONNECTED     73310    
unix  3      [ ]         STREAM     CONNECTED     42106    
unix  3      [ ]         STREAM     CONNECTED     34460    
unix  3      [ ]         STREAM     CONNECTED     34403    
unix  3      [ ]         STREAM     CONNECTED     21098    
unix  3      [ ]         STREAM     CONNECTED     108039   
unix  3      [ ]         STREAM     CONNECTED     56881    
unix  3      [ ]         STREAM     CONNECTED     49613    
unix  3      [ ]         STREAM     CONNECTED     45089    
unix  3      [ ]         STREAM     CONNECTED     48949    
unix  3      [ ]         STREAM     CONNECTED     41799    
unix  3      [ ]         STREAM     CONNECTED     45078    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     35480    
unix  3      [ ]         STREAM     CONNECTED     31574    
unix  3      [ ]         STREAM     CONNECTED     38165    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     22115    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM                    13025    
unix  3      [ ]         STREAM     CONNECTED     128801   
unix  3      [ ]         STREAM     CONNECTED     99391    
unix  3      [ ]         STREAM     CONNECTED     43910    
unix  3      [ ]         STREAM     CONNECTED     54366    
unix  3      [ ]         STREAM     CONNECTED     54316    
unix  3      [ ]         STREAM     CONNECTED     39720    
unix  3      [ ]         SEQPACKET  CONNECTED     36635    
unix  3      [ ]         SEQPACKET  CONNECTED     42507    
unix  3      [ ]         STREAM     CONNECTED     40750    
unix  3      [ ]         STREAM     CONNECTED     12270    
unix  3      [ ]         STREAM     CONNECTED     38206    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     25320    
unix  3      [ ]         STREAM     CONNECTED     14009    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31037    
unix  3      [ ]         STREAM     CONNECTED     20888    
unix  3      [ ]         STREAM     CONNECTED     19918    
unix  2      [ ]         DGRAM      CONNECTED     27760    
unix  3      [ ]         STREAM     CONNECTED     89437    
unix  3      [ ]         STREAM     CONNECTED     49617    
unix  3      [ ]         STREAM     CONNECTED     34707    
unix  2      [ ]         DGRAM      CONNECTED     21774    
unix  3      [ ]         STREAM     CONNECTED     116173   /run/user/1000/gvfsd/socket-eh3Q1iVO
unix  3      [ ]         STREAM     CONNECTED     43707    
unix  3      [ ]         STREAM     CONNECTED     52252    
unix  3      [ ]         STREAM     CONNECTED     15211    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     123908   
unix  3      [ ]         STREAM     CONNECTED     114004   
unix  3      [ ]         SEQPACKET  CONNECTED     113358   
unix  3      [ ]         STREAM     CONNECTED     108791   
unix  3      [ ]         STREAM     CONNECTED     47545    
unix  3      [ ]         STREAM     CONNECTED     37463    
unix  3      [ ]         STREAM     CONNECTED     45087    
unix  3      [ ]         STREAM     CONNECTED     30592    /run/user/1000/at-spi2-GK4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     115922   
unix  3      [ ]         STREAM     CONNECTED     90887    
unix  3      [ ]         STREAM     CONNECTED     78284    
unix  3      [ ]         STREAM     CONNECTED     50561    
unix  3      [ ]         STREAM     CONNECTED     34408    
unix  3      [ ]         STREAM     CONNECTED     111399   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     121297   
unix  3      [ ]         SEQPACKET  CONNECTED     110996   
unix  3      [ ]         STREAM     CONNECTED     98843    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     45512    
unix  2      [ ]         DGRAM      CONNECTED     31582    
unix  3      [ ]         STREAM     CONNECTED     40408    
unix  3      [ ]         STREAM     CONNECTED     34357    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     33023    
unix  3      [ ]         STREAM     CONNECTED     18057    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     20856    
unix  3      [ ]         STREAM     CONNECTED     53566    
unix  3      [ ]         STREAM     CONNECTED     53557    
unix  3      [ ]         STREAM     CONNECTED     34681    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     48821    
unix  3      [ ]         SEQPACKET  CONNECTED     41782    
unix  3      [ ]         STREAM     CONNECTED     37094    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     117376   
unix  3      [ ]         STREAM     CONNECTED     66030    
unix  3      [ ]         STREAM     CONNECTED     45842    
unix  3      [ ]         STREAM     CONNECTED     51458    
unix  3      [ ]         STREAM     CONNECTED     21099    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     37921    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     128215   
unix  3      [ ]         STREAM     CONNECTED     128117   
unix  3      [ ]         STREAM     CONNECTED     117416   
unix  3      [ ]         STREAM     CONNECTED     119840   
unix  3      [ ]         STREAM     CONNECTED     57943    
unix  3      [ ]         STREAM     CONNECTED     50588    
unix  3      [ ]         STREAM     CONNECTED     42407    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     36290    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     38015    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     28149    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     34223    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     109171   
unix  2      [ ]         DGRAM      CONNECTED     14013    
unix  3      [ ]         STREAM     CONNECTED     49967    
unix  3      [ ]         STREAM     CONNECTED     46943    
unix  3      [ ]         STREAM     CONNECTED     34683    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     52259    
unix  3      [ ]         STREAM     CONNECTED     41861    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     26316    
unix  3      [ ]         STREAM     CONNECTED     140418   
unix  3      [ ]         STREAM     CONNECTED     118785   
unix  3      [ ]         STREAM     CONNECTED     73311    
unix  3      [ ]         STREAM     CONNECTED     59067    
unix  3      [ ]         STREAM     CONNECTED     34468    /run/user/1000/at-spi2-1S4PH1/socket
unix  3      [ ]         STREAM     CONNECTED     34434    
unix  3      [ ]         STREAM     CONNECTED     34371    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     21113    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     31310    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     35579    
unix  3      [ ]         STREAM     CONNECTED     41798    
unix  3      [ ]         STREAM     CONNECTED     34507    
unix  3      [ ]         STREAM     CONNECTED     31557    
unix  3      [ ]         STREAM     CONNECTED     37910    
unix  3      [ ]         STREAM     CONNECTED     13277    
unix  3      [ ]         STREAM     CONNECTED     22875    
unix  3      [ ]         STREAM     CONNECTED     34687    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     34659    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     53418    
unix  3      [ ]         STREAM     CONNECTED     118576   
unix  3      [ ]         STREAM     CONNECTED     93678    
unix  3      [ ]         STREAM     CONNECTED     34714    
unix  3      [ ]         STREAM     CONNECTED     22151    
unix  3      [ ]         STREAM     CONNECTED     22097    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     117420   
unix  3      [ ]         STREAM     CONNECTED     55011    
unix  3      [ ]         STREAM     CONNECTED     54675    
unix  3      [ ]         STREAM     CONNECTED     54289    
unix  3      [ ]         STREAM     CONNECTED     40893    
unix  3      [ ]         STREAM     CONNECTED     42630    
unix  3      [ ]         STREAM     CONNECTED     28486    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     28144    
unix  3      [ ]         STREAM     CONNECTED     28115    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     31042    
unix  3      [ ]         STREAM     CONNECTED     24859    
unix  3      [ ]         STREAM     CONNECTED     18016    
unix  2      [ ]         DGRAM      CONNECTED     19480    
unix  3      [ ]         STREAM     CONNECTED     118855   /tmp/CoreFxPipe_vscode.7f9b0054043eb45d273f7f890416cb47
unix  3      [ ]         STREAM     CONNECTED     109001   
unix  3      [ ]         SEQPACKET  CONNECTED     113353   
unix  3      [ ]         STREAM     CONNECTED     38750    
unix  3      [ ]         STREAM     CONNECTED     25374    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     36164    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     33098    
unix  3      [ ]         STREAM     CONNECTED     30631    /run/user/1000/at-spi2-LLMSH1/socket
unix  3      [ ]         STREAM     CONNECTED     16504    
unix  3      [ ]         STREAM     CONNECTED     34414    
unix  3      [ ]         STREAM     CONNECTED     134103   
unix  3      [ ]         STREAM     CONNECTED     122106   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     116180   
unix  3      [ ]         STREAM     CONNECTED     104805   
unix  3      [ ]         STREAM     CONNECTED     97724    
unix  3      [ ]         STREAM     CONNECTED     56887    
unix  3      [ ]         STREAM     CONNECTED     55773    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     14321    /run/user/1000/at-spi2-QO4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     132534   
unix  3      [ ]         STREAM     CONNECTED     116223   
unix  3      [ ]         STREAM     CONNECTED     115925   
unix  3      [ ]         SEQPACKET  CONNECTED     50445    
unix  3      [ ]         STREAM     CONNECTED     21129    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     21089    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     120151   
unix  3      [ ]         STREAM     CONNECTED     69457    
unix  3      [ ]         STREAM     CONNECTED     21138    
unix  3      [ ]         STREAM     CONNECTED     39714    
unix  3      [ ]         STREAM     CONNECTED     46808    
unix  3      [ ]         STREAM     CONNECTED     118816   
unix  3      [ ]         STREAM     CONNECTED     49968    
unix  3      [ ]         STREAM     CONNECTED     33422    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     28178    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     20906    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     49142    
unix  3      [ ]         STREAM     CONNECTED     51414    
unix  3      [ ]         STREAM     CONNECTED     49050    
unix  3      [ ]         STREAM     CONNECTED     48976    
unix  3      [ ]         STREAM     CONNECTED     54286    
unix  3      [ ]         SEQPACKET  CONNECTED     36793    
unix  3      [ ]         STREAM     CONNECTED     49288    
unix  2      [ ]         DGRAM      CONNECTED     36306    
unix  3      [ ]         STREAM     CONNECTED     40456    
unix  3      [ ]         STREAM     CONNECTED     36169    
unix  3      [ ]         STREAM     CONNECTED     26427    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     31043    
unix  3      [ ]         STREAM     CONNECTED     119544   
unix  3      [ ]         STREAM     CONNECTED     34708    
unix  3      [ ]         STREAM     CONNECTED     38951    
unix  3      [ ]         STREAM     CONNECTED     30539    
unix  3      [ ]         STREAM     CONNECTED     117410   
unix  3      [ ]         STREAM     CONNECTED     49493    
unix  3      [ ]         STREAM     CONNECTED     49460    
unix  3      [ ]         STREAM     CONNECTED     36222    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     42390    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     41809    
unix  3      [ ]         STREAM     CONNECTED     31575    
unix  3      [ ]         STREAM     CONNECTED     42087    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     35412    
unix  3      [ ]         STREAM     CONNECTED     13836    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     116288   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     113995   
unix  3      [ ]         STREAM     CONNECTED     59064    
unix  3      [ ]         STREAM     CONNECTED     50566    
unix  3      [ ]         STREAM     CONNECTED     25376    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31514    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     39031    /run/user/1000/at-spi2-083IH1/socket
unix  3      [ ]         STREAM     CONNECTED     20902    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     116179   
unix  3      [ ]         STREAM     CONNECTED     112388   /run/user/1000/gvfsd/socket-4CCdRtV3
unix  3      [ ]         STREAM     CONNECTED     112342   
unix  3      [ ]         STREAM     CONNECTED     56992    
unix  3      [ ]         STREAM     CONNECTED     56712    
unix  3      [ ]         STREAM     CONNECTED     119340   
unix  3      [ ]         STREAM     CONNECTED     50600    
unix  3      [ ]         STREAM     CONNECTED     39711    
unix  3      [ ]         STREAM     CONNECTED     44963    
unix  3      [ ]         STREAM     CONNECTED     37319    
unix  3      [ ]         STREAM     CONNECTED     37314    
unix  3      [ ]         STREAM     CONNECTED     28174    
unix  3      [ ]         STREAM     CONNECTED     14130    /run/user/1000/bus
unix  3      [ ]         DGRAM      CONNECTED     16518    
unix  3      [ ]         STREAM     CONNECTED     125376   
unix  3      [ ]         STREAM     CONNECTED     125293   
unix  3      [ ]         STREAM     CONNECTED     43465    
unix  3      [ ]         STREAM     CONNECTED     45086    
unix  3      [ ]         STREAM     CONNECTED     14017    
unix  3      [ ]         STREAM     CONNECTED     135689   
unix  3      [ ]         STREAM     CONNECTED     128214   
unix  3      [ ]         STREAM     CONNECTED     119848   
unix  3      [ ]         STREAM     CONNECTED     54681    
unix  3      [ ]         SEQPACKET  CONNECTED     42512    
unix  3      [ ]         STREAM     CONNECTED     42502    
unix  3      [ ]         STREAM     CONNECTED     37454    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     34512    
unix  3      [ ]         STREAM     CONNECTED     26563    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     30573    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     32522    
unix  3      [ ]         STREAM     CONNECTED     36153    
unix  3      [ ]         STREAM     CONNECTED     98841    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     83992    /run/user/1000/pulse/native
unix  3      [ ]         SEQPACKET  CONNECTED     43313    
unix  3      [ ]         STREAM     CONNECTED     22155    
unix  3      [ ]         STREAM     CONNECTED     12199    
unix  3      [ ]         STREAM     CONNECTED     53558    
unix  3      [ ]         STREAM     CONNECTED     48826    
unix  3      [ ]         STREAM     CONNECTED     34673    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     25372    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     30086    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     111121   
unix  3      [ ]         STREAM     CONNECTED     119851   
unix  3      [ ]         STREAM     CONNECTED     37369    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     12229    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     21088    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     33001    
unix  3      [ ]         STREAM     CONNECTED     20870    
unix  3      [ ]         STREAM     CONNECTED     114423   @/tmp/.ICE-unix/2038
unix  3      [ ]         STREAM     CONNECTED     92200    
unix  3      [ ]         STREAM     CONNECTED     135067   
unix  3      [ ]         STREAM     CONNECTED     113999   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     64541    
unix  3      [ ]         STREAM     CONNECTED     50567    
unix  3      [ ]         STREAM     CONNECTED     21130    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     34227    
unix  3      [ ]         STREAM     CONNECTED     34002    
unix  3      [ ]         STREAM     CONNECTED     117459   
unix  3      [ ]         STREAM     CONNECTED     117324   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     62976    
unix  3      [ ]         STREAM     CONNECTED     47549    
unix  3      [ ]         STREAM     CONNECTED     45085    
unix  3      [ ]         STREAM     CONNECTED     26551    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     35867    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     46889    
unix  3      [ ]         STREAM     CONNECTED     26597    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     128217   
unix  3      [ ]         STREAM     CONNECTED     119045   
unix  3      [ ]         STREAM     CONNECTED     34744    
unix  2      [ ]         DGRAM      CONNECTED     30360    
unix  3      [ ]         STREAM     CONNECTED     128800   
unix  3      [ ]         STREAM     CONNECTED     99392    
unix  3      [ ]         STREAM     CONNECTED     55010    
unix  3      [ ]         STREAM     CONNECTED     51338    /run/user/1000/bus
unix  3      [ ]         SEQPACKET  CONNECTED     36632    
unix  3      [ ]         STREAM     CONNECTED     36549    
unix  3      [ ]         STREAM     CONNECTED     26487    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     28158    
unix  3      [ ]         STREAM     CONNECTED     36952    
unix  3      [ ]         STREAM     CONNECTED     32498    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31332    
unix  3      [ ]         STREAM     CONNECTED     30119    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     110989   
unix  3      [ ]         STREAM     CONNECTED     53452    
unix  3      [ ]         STREAM     CONNECTED     37217    @/tmp/.X11-unix/X0
unix  2      [ ]         DGRAM      CONNECTED     41800    
unix  3      [ ]         STREAM     CONNECTED     31558    
unix  3      [ ]         STREAM     CONNECTED     21144    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     38091    
unix  3      [ ]         STREAM     CONNECTED     32496    
unix  3      [ ]         STREAM     CONNECTED     49592    
unix  3      [ ]         STREAM     CONNECTED     49308    
unix  3      [ ]         STREAM     CONNECTED     43230    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     14310    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     104314   
unix  3      [ ]         STREAM     CONNECTED     108040   
unix  3      [ ]         STREAM     CONNECTED     104913   
unix  3      [ ]         STREAM     CONNECTED     80113    
unix  3      [ ]         STREAM     CONNECTED     140543   
unix  3      [ ]         STREAM     CONNECTED     113998   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     58964    
unix  3      [ ]         STREAM     CONNECTED     50580    
unix  2      [ ]         DGRAM      CONNECTED     21455    
unix  3      [ ]         STREAM     CONNECTED     26526    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     34411    
unix  3      [ ]         DGRAM      CONNECTED     34058    
unix  2      [ ]         DGRAM                    108836   
unix  3      [ ]         STREAM     CONNECTED     43713    
unix  3      [ ]         STREAM     CONNECTED     55170    
unix  3      [ ]         STREAM     CONNECTED     50599    
unix  3      [ ]         STREAM     CONNECTED     30703    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     46121    
unix  3      [ ]         STREAM     CONNECTED     44146    
unix  3      [ ]         STREAM     CONNECTED     30639    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     39066    
unix  3      [ ]         STREAM     CONNECTED     28175    
unix  3      [ ]         STREAM     CONNECTED     26313    
unix  3      [ ]         STREAM     CONNECTED     115101   
unix  3      [ ]         STREAM     CONNECTED     117824   
unix  3      [ ]         STREAM     CONNECTED     59496    
unix  3      [ ]         STREAM     CONNECTED     22152    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         DGRAM      CONNECTED     21833    
unix  3      [ ]         STREAM     CONNECTED     119838   
unix  3      [ ]         STREAM     CONNECTED     104932   
unix  3      [ ]         STREAM     CONNECTED     60913    
unix  3      [ ]         STREAM     CONNECTED     54357    
unix  3      [ ]         STREAM     CONNECTED     34690    
unix  3      [ ]         STREAM     CONNECTED     36316    
unix  3      [ ]         STREAM     CONNECTED     34490    
unix  3      [ ]         STREAM     CONNECTED     32511    
unix  3      [ ]         STREAM     CONNECTED     35871    
unix  3      [ ]         STREAM     CONNECTED     13830    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     135704   @/tmp/.ICE-unix/2038
unix  3      [ ]         STREAM     CONNECTED     110986   
unix  3      [ ]         STREAM     CONNECTED     47334    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     21111    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     26319    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     33015    
unix  3      [ ]         STREAM     CONNECTED     32467    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     20868    
unix  3      [ ]         STREAM     CONNECTED     48828    
unix  3      [ ]         STREAM     CONNECTED     50421    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     49181    
unix  3      [ ]         STREAM     CONNECTED     46817    
unix  3      [ ]         STREAM     CONNECTED     21418    @/tmp/.ICE-unix/2038
unix  3      [ ]         SEQPACKET  CONNECTED     113356   
unix  3      [ ]         STREAM     CONNECTED     62977    
unix  2      [ ]         DGRAM      CONNECTED     49293    
unix  3      [ ]         STREAM     CONNECTED     22305    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     37918    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     14049    
unix  3      [ ]         STREAM     CONNECTED     98842    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     50562    
unix  3      [ ]         STREAM     CONNECTED     34401    
unix  3      [ ]         STREAM     CONNECTED     31483    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     15260    
unix  3      [ ]         STREAM     CONNECTED     120199   
unix  3      [ ]         STREAM     CONNECTED     21108    
unix  3      [ ]         STREAM     CONNECTED     49285    
unix  3      [ ]         STREAM     CONNECTED     53419    
unix  3      [ ]         SEQPACKET  CONNECTED     110997   
unix  3      [ ]         STREAM     CONNECTED     26584    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     35430    
unix  3      [ ]         STREAM     CONNECTED     14329    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31488    
unix  3      [ ]         STREAM     CONNECTED     14265    
unix  3      [ ]         STREAM     CONNECTED     13265    
unix  3      [ ]         STREAM     CONNECTED     128836   /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     138539   
unix  3      [ ]         STREAM     CONNECTED     117787   
unix  3      [ ]         STREAM     CONNECTED     54680    
unix  2      [ ]         DGRAM      CONNECTED     36557    
unix  3      [ ]         STREAM     CONNECTED     40454    
unix  3      [ ]         STREAM     CONNECTED     33427    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     36978    
unix  3      [ ]         STREAM     CONNECTED     21090    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     32501    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31322    
unix  3      [ ]         STREAM     CONNECTED     11928    
unix  3      [ ]         STREAM     CONNECTED     24851    
unix  2      [ ]         STREAM     CONNECTED     117918   
unix  3      [ ]         STREAM     CONNECTED     93680    
unix  3      [ ]         STREAM     CONNECTED     53556    
unix  2      [ ]         DGRAM      CONNECTED     38963    
unix  3      [ ]         STREAM     CONNECTED     30562    
unix  3      [ ]         STREAM     CONNECTED     55171    
unix  3      [ ]         STREAM     CONNECTED     46813    
unix  3      [ ]         STREAM     CONNECTED     34486    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     39147    
unix  3      [ ]         STREAM     CONNECTED     22157    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     28179    
unix  3      [ ]         STREAM     CONNECTED     34229    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31902    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     125294   
unix  3      [ ]         STREAM     CONNECTED     109166   
unix  3      [ ]         SEQPACKET  CONNECTED     43584    
unix  3      [ ]         STREAM     CONNECTED     43559    
unix  3      [ ]         STREAM     CONNECTED     28153    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     13826    
unix  3      [ ]         STREAM     CONNECTED     59043    
unix  3      [ ]         STREAM     CONNECTED     48820    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     34461    
unix  3      [ ]         STREAM     CONNECTED     25370    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     38180    /run/user/1000/at-spi2-T43IH1/socket
unix  3      [ ]         STREAM     CONNECTED     116171   
unix  3      [ ]         STREAM     CONNECTED     104918   
unix  3      [ ]         STREAM     CONNECTED     37589    
unix  3      [ ]         STREAM     CONNECTED     53545    
unix  3      [ ]         STREAM     CONNECTED     48317    
unix  3      [ ]         STREAM     CONNECTED     37091    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     35411    
unix  3      [ ]         STREAM     CONNECTED     33448    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     35292    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     115383   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     119850   
unix  3      [ ]         STREAM     CONNECTED     45629    
unix  3      [ ]         STREAM     CONNECTED     21171    /run/user/1000/at-spi2-SM4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     21065    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     14014    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     33019    
unix  3      [ ]         STREAM     CONNECTED     31313    
unix  3      [ ]         STREAM     CONNECTED     30037    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     135688   
unix  3      [ ]         STREAM     CONNECTED     104943   
unix  3      [ ]         STREAM     CONNECTED     119849   
unix  3      [ ]         STREAM     CONNECTED     104923   
unix  3      [ ]         STREAM     CONNECTED     84713    
unix  3      [ ]         STREAM     CONNECTED     42691    
unix  3      [ ]         STREAM     CONNECTED     52578    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     37466    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     34529    
unix  2      [ ]         DGRAM      CONNECTED     36305    
unix  3      [ ]         STREAM     CONNECTED     32521    
unix  3      [ ]         STREAM     CONNECTED     19931    
unix  3      [ ]         STREAM     CONNECTED     115384   
unix  3      [ ]         STREAM     CONNECTED     115100   
unix  3      [ ]         STREAM     CONNECTED     117788   
unix  3      [ ]         STREAM     CONNECTED     43912    
unix  3      [ ]         STREAM     CONNECTED     12221    
unix  3      [ ]         STREAM     CONNECTED     22153    
unix  3      [ ]         STREAM     CONNECTED     133147   
unix  3      [ ]         STREAM     CONNECTED     113398   
unix  3      [ ]         STREAM     CONNECTED     113132   
unix  3      [ ]         STREAM     CONNECTED     35468    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     13860    
unix  3      [ ]         STREAM     CONNECTED     39713    
unix  3      [ ]         STREAM     CONNECTED     46120    
unix  3      [ ]         STREAM     CONNECTED     120601   
unix  3      [ ]         STREAM     CONNECTED     93183    
unix  3      [ ]         STREAM     CONNECTED     26425    
unix  3      [ ]         STREAM     CONNECTED     123267   /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     120262   /run/user/1000/at-spi2-DO3JH1/socket
unix  3      [ ]         STREAM     CONNECTED     115923   
unix  3      [ ]         STREAM     CONNECTED     50556    
unix  3      [ ]         STREAM     CONNECTED     34404    
unix  3      [ ]         DGRAM      CONNECTED     34059    
unix  3      [ ]         STREAM     CONNECTED     53470    
unix  3      [ ]         STREAM     CONNECTED     35505    
unix  3      [ ]         STREAM     CONNECTED     41795    
unix  3      [ ]         STREAM     CONNECTED     41794    
unix  3      [ ]         STREAM     CONNECTED     31564    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     36269    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     13276    
unix  3      [ ]         STREAM     CONNECTED     51409    
unix  2      [ ]         DGRAM      CONNECTED     49294    
unix  3      [ ]         STREAM     CONNECTED     36320    /run/user/1000/at-spi2-HSS8G1/socket
unix  3      [ ]         STREAM     CONNECTED     35406    
unix  3      [ ]         STREAM     CONNECTED     118621   
unix  3      [ ]         STREAM     CONNECTED     119055   
unix  3      [ ]         STREAM     CONNECTED     89435    
unix  3      [ ]         STREAM     CONNECTED     48078    
unix  3      [ ]         STREAM     CONNECTED     49105    
unix  3      [ ]         STREAM     CONNECTED     49104    
unix  3      [ ]         STREAM     CONNECTED     34682    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     42406    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     40450    
unix  3      [ ]         STREAM     CONNECTED     37047    
unix  3      [ ]         STREAM     CONNECTED     36161    
unix  3      [ ]         STREAM     CONNECTED     12215    
unix  3      [ ]         STREAM     CONNECTED     25280    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31331    
unix  2      [ ]         DGRAM      CONNECTED     24897    
unix  3      [ ]         DGRAM      CONNECTED     27722    
unix  3      [ ]         STREAM     CONNECTED     112413   
unix  3      [ ]         STREAM     CONNECTED     33426    
unix  2      [ ]         STREAM     CONNECTED     114007   
unix  3      [ ]         STREAM     CONNECTED     46933    
unix  3      [ ]         STREAM     CONNECTED     50594    
unix  3      [ ]         STREAM     CONNECTED     41818    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     39254    
unix  3      [ ]         STREAM     CONNECTED     34487    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     28488    
unix  3      [ ]         STREAM     CONNECTED     34230    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     108387   
unix  3      [ ]         STREAM     CONNECTED     108386   
unix  3      [ ]         STREAM     CONNECTED     56889    
unix  3      [ ]         STREAM     CONNECTED     37582    
unix  3      [ ]         STREAM     CONNECTED     59029    
unix  3      [ ]         STREAM     CONNECTED     50579    
unix  3      [ ]         STREAM     CONNECTED     42109    
unix  3      [ ]         STREAM     CONNECTED     34418    /run/user/1000/at-spi2-OH4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     39034    /run/user/1000/at-spi2-NF4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     120981   
unix  3      [ ]         STREAM     CONNECTED     45526    
unix  3      [ ]         STREAM     CONNECTED     37464    
unix  3      [ ]         STREAM     CONNECTED     35475    
unix  3      [ ]         STREAM     CONNECTED     40437    
unix  3      [ ]         STREAM     CONNECTED     21093    
unix  3      [ ]         STREAM     CONNECTED     33022    
unix  3      [ ]         STREAM     CONNECTED     35865    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     48969    
unix  3      [ ]         STREAM     CONNECTED     48955    
unix  2      [ ]         DGRAM                    26556    
unix  3      [ ]         STREAM     CONNECTED     35413    /run/user/1000/at-spi2-UM4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     136811   /run/user/1000/at-spi2-HUSJH1/socket
unix  3      [ ]         STREAM     CONNECTED     115313   
unix  3      [ ]         STREAM     CONNECTED     115076   
unix  3      [ ]         STREAM     CONNECTED     65575    
unix  3      [ ]         STREAM     CONNECTED     22262    
unix  3      [ ]         STREAM     CONNECTED     36124    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     22149    
unix  3      [ ]         STREAM     CONNECTED     84715    
unix  3      [ ]         STREAM     CONNECTED     60673    
unix  3      [ ]         STREAM     CONNECTED     39733    
unix  3      [ ]         SEQPACKET  CONNECTED     42510    
unix  3      [ ]         STREAM     CONNECTED     34484    
unix  3      [ ]         STREAM     CONNECTED     37031    
unix  3      [ ]         STREAM     CONNECTED     36267    
unix  2      [ ]         STREAM     CONNECTED     38019    
unix  3      [ ]         STREAM     CONNECTED     36127    
unix  3      [ ]         STREAM     CONNECTED     32133    
unix  3      [ ]         STREAM     CONNECTED     138100   
unix  3      [ ]         STREAM     CONNECTED     128802   
unix  3      [ ]         STREAM     CONNECTED     114424   /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     84712    
unix  3      [ ]         STREAM     CONNECTED     45804    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     34689    
unix  3      [ ]         SEQPACKET  CONNECTED     36641    
unix  3      [ ]         STREAM     CONNECTED     37029    
unix  3      [ ]         STREAM     CONNECTED     25321    
unix  3      [ ]         STREAM     CONNECTED     34365    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     36131    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     36953    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     28160    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     36052    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     35861    
unix  3      [ ]         STREAM     CONNECTED     28002    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     119058   
unix  3      [ ]         STREAM     CONNECTED     60672    /run/user/1000/gvfsd/socket-xIteqTFX
unix  3      [ ]         STREAM     CONNECTED     34729    
unix  3      [ ]         STREAM     CONNECTED     49612    
unix  3      [ ]         STREAM     CONNECTED     53420    
unix  3      [ ]         STREAM     CONNECTED     30540    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     42628    
unix  3      [ ]         STREAM     CONNECTED     45446    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     31589    
unix  3      [ ]         STREAM     CONNECTED     37093    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     40969    
unix  3      [ ]         STREAM     CONNECTED     26428    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     37923    
unix  3      [ ]         STREAM     CONNECTED     21094    
unix  3      [ ]         STREAM     CONNECTED     140542   /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     132109   
unix  3      [ ]         STREAM     CONNECTED     112416   
unix  3      [ ]         STREAM     CONNECTED     104185   
unix  3      [ ]         STREAM     CONNECTED     104806   
unix  3      [ ]         STREAM     CONNECTED     104804   
unix  3      [ ]         STREAM     CONNECTED     90886    
unix  3      [ ]         STREAM     CONNECTED     34409    
unix  3      [ ]         STREAM     CONNECTED     34406    
unix  3      [ ]         STREAM     CONNECTED     104442   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     56890    
unix  3      [ ]         STREAM     CONNECTED     40438    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     113994   
unix  3      [ ]         STREAM     CONNECTED     47548    
unix  3      [ ]         STREAM     CONNECTED     43715    
unix  3      [ ]         STREAM     CONNECTED     33770    
unix  3      [ ]         STREAM     CONNECTED     33472    
unix  3      [ ]         STREAM     CONNECTED     117417   
unix  3      [ ]         STREAM     CONNECTED     104944   
unix  3      [ ]         STREAM     CONNECTED     119837   
unix  3      [ ]         STREAM     CONNECTED     34703    
unix  3      [ ]         STREAM     CONNECTED     36272    
unix  3      [ ]         STREAM     CONNECTED     34372    @/tmp/.ICE-unix/2038
unix  3      [ ]         STREAM     CONNECTED     21110    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     28161    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     28041    
unix  3      [ ]         STREAM     CONNECTED     128804   
unix  3      [ ]         STREAM     CONNECTED     117414   
unix  3      [ ]         STREAM     CONNECTED     115075   
unix  3      [ ]         STREAM     CONNECTED     66031    
unix  3      [ ]         STREAM     CONNECTED     43234    
unix  3      [ ]         STREAM     CONNECTED     93645    
unix  3      [ ]         STREAM     CONNECTED     53567    
unix  3      [ ]         STREAM     CONNECTED     53549    
unix  3      [ ]         STREAM     CONNECTED     48952    
unix  3      [ ]         STREAM     CONNECTED     26606    
unix  3      [ ]         STREAM     CONNECTED     26523    
unix  3      [ ]         STREAM     CONNECTED     111120   
unix  3      [ ]         STREAM     CONNECTED     87273    
unix  3      [ ]         STREAM     CONNECTED     51404    
unix  3      [ ]         STREAM     CONNECTED     51333    /run/user/1000/bus
unix  2      [ ]         DGRAM                    14263    
unix  3      [ ]         STREAM     CONNECTED     25315    
unix  3      [ ]         STREAM     CONNECTED     14071    
unix  3      [ ]         STREAM     CONNECTED     18056    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     114360   
unix  3      [ ]         STREAM     CONNECTED     93133    
unix  3      [ ]         STREAM     CONNECTED     69460    
unix  3      [ ]         STREAM     CONNECTED     69458    
unix  3      [ ]         STREAM     CONNECTED     34410    
unix  3      [ ]         STREAM     CONNECTED     26321    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     14007    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     108064   
unix  3      [ ]         STREAM     CONNECTED     57272    
unix  3      [ ]         STREAM     CONNECTED     119343   
unix  3      [ ]         STREAM     CONNECTED     46811    
unix  3      [ ]         STREAM     CONNECTED     49174    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     37229    
unix  3      [ ]         STREAM     CONNECTED     39146    
unix  3      [ ]         STREAM     CONNECTED     34364    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     32844    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     96356    
unix  3      [ ]         STREAM     CONNECTED     43704    
unix  3      [ ]         DGRAM      CONNECTED     13768    
unix  3      [ ]         STREAM     CONNECTED     118575   
unix  3      [ ]         STREAM     CONNECTED     56209    
unix  3      [ ]         STREAM     CONNECTED     43899    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     138529   
unix  3      [ ]         STREAM     CONNECTED     60945    
unix  3      [ ]         STREAM     CONNECTED     55172    
unix  3      [ ]         STREAM     CONNECTED     43911    
unix  3      [ ]         STREAM     CONNECTED     54317    
unix  3      [ ]         STREAM     CONNECTED     39719    
unix  3      [ ]         STREAM     CONNECTED     34506    
unix  3      [ ]         STREAM     CONNECTED     25377    
unix  3      [ ]         STREAM     CONNECTED     12223    
unix  3      [ ]         STREAM     CONNECTED     36951    
unix  3      [ ]         STREAM     CONNECTED     13304    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     36051    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     24848    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     121298   
unix  3      [ ]         STREAM     CONNECTED     45649    
unix  3      [ ]         STREAM     CONNECTED     35578    
unix  3      [ ]         STREAM     CONNECTED     38839    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     37092    @/tmp/.X11-unix/X0
unix  3      [ ]         SEQPACKET  CONNECTED     31584    
unix  3      [ ]         STREAM     CONNECTED     38164    
unix  3      [ ]         STREAM     CONNECTED     115314   
unix  3      [ ]         STREAM     CONNECTED     48970    
unix  3      [ ]         STREAM     CONNECTED     42114    /run/dbus/system_bus_socket
unix  2      [ ]         DGRAM      CONNECTED     35398    
unix  3      [ ]         STREAM     CONNECTED     120014   
unix  3      [ ]         STREAM     CONNECTED     104920   
unix  3      [ ]         STREAM     CONNECTED     123293   
unix  3      [ ]         STREAM     CONNECTED     112415   
unix  3      [ ]         STREAM     CONNECTED     114002   @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     114001   /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     34534    /run/user/1000/gvfsd/socket-bhpwKvER
unix  3      [ ]         STREAM     CONNECTED     31499    /run/user/1000/at-spi2-PR4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     34363    
unix  3      [ ]         STREAM     CONNECTED     123907   
unix  3      [ ]         STREAM     CONNECTED     113490   
unix  3      [ ]         STREAM     CONNECTED     119853   
unix  3      [ ]         STREAM     CONNECTED     52251    
unix  3      [ ]         STREAM     CONNECTED     43238    /var/run/mullvad-vpn
unix  3      [ ]         STREAM     CONNECTED     45074    
unix  3      [ ]         STREAM     CONNECTED     30039    
unix  3      [ ]         STREAM     CONNECTED     108792   
unix  3      [ ]         STREAM     CONNECTED     37214    
unix  3      [ ]         STREAM     CONNECTED     112467   
unix  3      [ ]         STREAM     CONNECTED     60681    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     46914    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     43240    /run/user/1000/at-spi2-1L4NH1/socket
unix  3      [ ]         STREAM     CONNECTED     119057   
unix  3      [ ]         STREAM     CONNECTED     60943    
unix  3      [ ]         STREAM     CONNECTED     42503    
unix  3      [ ]         STREAM     CONNECTED     34509    
unix  3      [ ]         STREAM     CONNECTED     35404    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     38997    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     38955    
unix  3      [ ]         STREAM     CONNECTED     32495    
unix  3      [ ]         STREAM     CONNECTED     27993    
unix  3      [ ]         SEQPACKET  CONNECTED     111002   
unix  3      [ ]         SEQPACKET  CONNECTED     110990   
unix  3      [ ]         STREAM     CONNECTED     36642    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     37231    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     14262    
unix  3      [ ]         STREAM     CONNECTED     22156    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     35294    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     33052    
unix  3      [ ]         STREAM     CONNECTED     53551    
unix  3      [ ]         STREAM     CONNECTED     36633    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     34677    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     40970    /run/user/1000/bus
unix  2      [ ]         DGRAM      CONNECTED     26537    
unix  3      [ ]         SEQPACKET  CONNECTED     31543    
unix  3      [ ]         STREAM     CONNECTED     30365    
unix  3      [ ]         STREAM     CONNECTED     99092    
unix  3      [ ]         STREAM     CONNECTED     104919   
unix  3      [ ]         STREAM     CONNECTED     30591    /run/user/1000/at-spi2-UO4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     138540   
unix  3      [ ]         STREAM     CONNECTED     114388   
unix  3      [ ]         SEQPACKET  CONNECTED     34441    
unix  3      [ ]         STREAM     CONNECTED     35299    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     21095    
unix  3      [ ]         STREAM     CONNECTED     13279    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     34062    
unix  3      [ ]         STREAM     CONNECTED     113553   
unix  3      [ ]         STREAM     CONNECTED     14048    
unix  3      [ ]         DGRAM      CONNECTED     13766    
unix  3      [ ]         STREAM     CONNECTED     119509   
unix  3      [ ]         STREAM     CONNECTED     118198   
unix  3      [ ]         STREAM     CONNECTED     46932    
unix  3      [ ]         STREAM     CONNECTED     49289    
unix  3      [ ]         STREAM     CONNECTED     39558    /run/user/1000/gvfsd/socket-MeOW9fel
unix  3      [ ]         STREAM     CONNECTED     37240    
unix  3      [ ]         STREAM     CONNECTED     39129    
unix  3      [ ]         STREAM     CONNECTED     21847    /var/run/docker/containerd/containerd.sock
unix  3      [ ]         STREAM     CONNECTED     48948    
unix  3      [ ]         STREAM     CONNECTED     35305    
unix  3      [ ]         STREAM     CONNECTED     35290    
unix  3      [ ]         STREAM     CONNECTED     21057    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     45632    
unix  3      [ ]         STREAM     CONNECTED     41829    
unix  3      [ ]         STREAM     CONNECTED     38203    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     30564    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     35293    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     57911    
unix  3      [ ]         STREAM     CONNECTED     55013    
unix  3      [ ]         STREAM     CONNECTED     42693    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     39811    
unix  3      [ ]         STREAM     CONNECTED     40894    
unix  3      [ ]         SEQPACKET  CONNECTED     36794    
unix  3      [ ]         STREAM     CONNECTED     34475    
unix  3      [ ]         STREAM     CONNECTED     21143    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     33097    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     14050    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     31320    
unix  3      [ ]         STREAM     CONNECTED     31319    
unix  3      [ ]         STREAM     CONNECTED     13962    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     28027    /var/run/docker/containerd/containerd.sock
unix  3      [ ]         STREAM     CONNECTED     11946    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM      CONNECTED     24856    
unix  3      [ ]         STREAM     CONNECTED     89438    
unix  3      [ ]         STREAM     CONNECTED     34734    
unix  3      [ ]         STREAM     CONNECTED     37291    
unix  3      [ ]         STREAM     CONNECTED     117940   /run/user/1000/gvfsd/socket-5So4lE57
unix  3      [ ]         STREAM     CONNECTED     113993   
unix  3      [ ]         STREAM     CONNECTED     43703    
unix  3      [ ]         STREAM     CONNECTED     35460    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     33099    
unix  3      [ ]         STREAM     CONNECTED     115912   
unix  3      [ ]         STREAM     CONNECTED     50479    
unix  3      [ ]         STREAM     CONNECTED     41867    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     39026    /run/user/1000/at-spi2-DT4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     34369    
unix  3      [ ]         STREAM     CONNECTED     57271    
unix  3      [ ]         STREAM     CONNECTED     54943    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     52258    
unix  3      [ ]         STREAM     CONNECTED     53554    
unix  3      [ ]         STREAM     CONNECTED     53553    
unix  3      [ ]         STREAM     CONNECTED     48824    
unix  3      [ ]         STREAM     CONNECTED     26603    
unix  3      [ ]         STREAM     CONNECTED     26481    
unix  3      [ ]         STREAM     CONNECTED     21465    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     21087    
unix  3      [ ]         STREAM     CONNECTED     39813    
unix  3      [ ]         STREAM     CONNECTED     42690    
unix  3      [ ]         STREAM     CONNECTED     34712    
unix  3      [ ]         STREAM     CONNECTED     34674    
unix  3      [ ]         STREAM     CONNECTED     36548    
unix  3      [ ]         STREAM     CONNECTED     36541    
unix  3      [ ]         STREAM     CONNECTED     26581    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     38967    
unix  2      [ ]         DGRAM      CONNECTED     38964    
unix  3      [ ]         STREAM     CONNECTED     34219    @/tmp/.X11-unix/X0
unix  2      [ ]         DGRAM      CONNECTED     27821    
unix  3      [ ]         STREAM     CONNECTED     115310   
unix  3      [ ]         STREAM     CONNECTED     83075    
unix  3      [ ]         STREAM     CONNECTED     49143    
unix  3      [ ]         STREAM     CONNECTED     49596    
unix  3      [ ]         STREAM     CONNECTED     51413    
unix  3      [ ]         STREAM     CONNECTED     118846   
unix  3      [ ]         STREAM     CONNECTED     34553    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     37100    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     39149    
unix  3      [ ]         STREAM     CONNECTED     26001    
unix  3      [ ]         DGRAM      CONNECTED     16517    
unix  3      [ ]         STREAM     CONNECTED     98886    
unix  3      [ ]         STREAM     CONNECTED     62995    
unix  3      [ ]         STREAM     CONNECTED     43466    
unix  3      [ ]         STREAM     CONNECTED     34402    
unix  3      [ ]         STREAM     CONNECTED     13865    
unix  2      [ ]         DGRAM      CONNECTED     13835    
unix  3      [ ]         STREAM     CONNECTED     59066    
unix  3      [ ]         STREAM     CONNECTED     68989    
unix  3      [ ]         STREAM     CONNECTED     42103    
unix  3      [ ]         STREAM     CONNECTED     34415    
unix  3      [ ]         STREAM     CONNECTED     25308    /run/user/1000/pulse/native
unix  3      [ ]         STREAM     CONNECTED     34124    
unix  2      [ ]         DGRAM      CONNECTED     34034    
unix  3      [ ]         STREAM     CONNECTED     120535   
unix  3      [ ]         STREAM     CONNECTED     104315   
unix  3      [ ]         STREAM     CONNECTED     56891    
unix  3      [ ]         STREAM     CONNECTED     119852   
unix  3      [ ]         STREAM     CONNECTED     37570    
unix  3      [ ]         STREAM     CONNECTED     41817    
unix  3      [ ]         SEQPACKET  CONNECTED     31583    
unix  3      [ ]         STREAM     CONNECTED     26536    /run/systemd/journal/stdout
unix  3      [ ]         SEQPACKET  CONNECTED     35434    
unix  3      [ ]         STREAM     CONNECTED     30036    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     48308    
unix  3      [ ]         STREAM     CONNECTED     30586    /run/user/1000/at-spi2-621IH1/socket
unix  3      [ ]         STREAM     CONNECTED     12225    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     22150    
unix  3      [ ]         STREAM     CONNECTED     89440    
unix  3      [ ]         STREAM     CONNECTED     61523    
unix  3      [ ]         STREAM     CONNECTED     34739    
unix  3      [ ]         STREAM     CONNECTED     81885    /run/user/1000/pipewire-0
unix  3      [ ]         STREAM     CONNECTED     54367    
unix  3      [ ]         STREAM     CONNECTED     48977    
unix  3      [ ]         STREAM     CONNECTED     34698    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     45449    /run/user/1000/at-spi2-76P8G1/socket
unix  3      [ ]         STREAM     CONNECTED     34510    
unix  3      [ ]         STREAM     CONNECTED     12230    
unix  3      [ ]         STREAM     CONNECTED     37999    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     28147    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     12210    
unix  3      [ ]         STREAM     CONNECTED     13832    /run/dbus/system_bus_socket
unix  2      [ ]         DGRAM      CONNECTED     31011    
unix  3      [ ]         DGRAM      CONNECTED     27721    
unix  3      [ ]         STREAM     CONNECTED     50596    
unix  3      [ ]         STREAM     CONNECTED     52255    
unix  3      [ ]         SEQPACKET  CONNECTED     43579    
unix  3      [ ]         STREAM     CONNECTED     46105    /run/user/1000/at-spi2-WXTEH1/socket
unix  3      [ ]         STREAM     CONNECTED     38202    
unix  3      [ ]         STREAM     CONNECTED     109167   
unix  3      [ ]         STREAM     CONNECTED     37117    
unix  3      [ ]         STREAM     CONNECTED     120537   
unix  3      [ ]         STREAM     CONNECTED     104914   
unix  3      [ ]         STREAM     CONNECTED     134102   
unix  3      [ ]         STREAM     CONNECTED     132108   
unix  3      [ ]         STREAM     CONNECTED     115924   
unix  3      [ ]         STREAM     CONNECTED     112341   
unix  3      [ ]         STREAM     CONNECTED     104803   
unix  3      [ ]         SEQPACKET  CONNECTED     31614    
unix  3      [ ]         STREAM     CONNECTED     22261    /tmp/dbus-27yrq1DDe6
unix  3      [ ]         STREAM     CONNECTED     31489    /run/user/1000/at-spi2-KL4IH1/socket
unix  3      [ ]         STREAM     CONNECTED     121296   
unix  3      [ ]         STREAM     CONNECTED     87274    
unix  3      [ ]         STREAM     CONNECTED     37486    
unix  3      [ ]         STREAM     CONNECTED     49309    
unix  3      [ ]         STREAM     CONNECTED     26583    @/tmp/.X11-unix/X0
unix  3      [ ]         STREAM     CONNECTED     40007    /run/user/1000/at-spi2-CA4KH1/socket
unix  3      [ ]         STREAM     CONNECTED     14258    
unix  3      [ ]         STREAM     CONNECTED     34750    
unix  3      [ ]         STREAM     CONNECTED     48971    
unix  3      [ ]         STREAM     CONNECTED     53451    
unix  3      [ ]         STREAM     CONNECTED     26566    
unix  3      [ ]         STREAM     CONNECTED     31572    
unix  3      [ ]         STREAM     CONNECTED     128803   
unix  3      [ ]         STREAM     CONNECTED     117765   
unix  3      [ ]         SEQPACKET  CONNECTED     36631    
unix  3      [ ]         STREAM     CONNECTED     25259    
unix  3      [ ]         DGRAM      CONNECTED     21832    
unix  3      [ ]         STREAM     CONNECTED     128216   
unix  3      [ ]         STREAM     CONNECTED     119841   
unix  3      [ ]         STREAM     CONNECTED     45841    
unix  3      [ ]         STREAM     CONNECTED     36547    
unix  3      [ ]         STREAM     CONNECTED     42505    
unix  3      [ ]         STREAM     CONNECTED     34649    
unix  3      [ ]         STREAM     CONNECTED     33713    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     32532    
unix  3      [ ]         STREAM     CONNECTED     36129    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     109390   
unix  3      [ ]         STREAM     CONNECTED     109225   /run/user/1000/gvfsd/socket-mCnbmnBq
unix  3      [ ]         SEQPACKET  CONNECTED     43582    
unix  3      [ ]         STREAM     CONNECTED     14018    
unix  3      [ ]         STREAM     CONNECTED     119342   
unix  3      [ ]         STREAM     CONNECTED     52569    
unix  3      [ ]         STREAM     CONNECTED     46807    
unix  3      [ ]         STREAM     CONNECTED     37213    
unix  3      [ ]         SEQPACKET  CONNECTED     39250    
unix  3      [ ]         STREAM     CONNECTED     35431    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     26019    
unix  3      [ ]         STREAM     CONNECTED     13831    /run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     27774    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     120013   
unix  3      [ ]         STREAM     CONNECTED     56880    
unix  3      [ ]         STREAM     CONNECTED     34228    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     122312   
unix  3      [ ]         STREAM     CONNECTED     114387   
unix  3      [ ]         STREAM     CONNECTED     93184    
unix  3      [ ]         STREAM     CONNECTED     87337    /run/user/1000/bus
unix  3      [ ]         STREAM     CONNECTED     52676    
unix  3      [ ]         STREAM     CONNECTED     42104    
unix  3      [ ]         STREAM     CONNECTED     42083    
unix  3      [ ]         STREAM     CONNECTED     34413    
unix  3      [ ]         STREAM     CONNECTED     30006    /run/systemd/journal/stdout
```

## Other Commands

### ssh
![](assets/ssh.png)

### neofetch
On my host system
![](assets/neofetch1.png)

On a remote system (from the SSH example)
![](assets/neofetch2.png)

### htop
![](assets/htop.png)

### dig
![](assets/dig.png)

### host
![](assets/host.png)

### whois
```
[mreiff@starship ~]$ whois stevens.edu
This Registry database contains ONLY .EDU domains.
The data in the EDUCAUSE Whois database is provided
by EDUCAUSE for information purposes in order to
assist in the process of obtaining information about
or related to .edu domain registration records.

The EDUCAUSE Whois database is authoritative for the
.EDU domain.

A Web interface for the .EDU EDUCAUSE Whois Server is
available at: http://whois.educause.edu

By submitting a Whois query, you agree that this information
will not be used to allow, enable, or otherwise support
the transmission of unsolicited commercial advertising or
solicitations via e-mail.  The use of electronic processes to
harvest information from this server is generally prohibited
except as reasonably necessary to register or modify .edu
domain names.

-------------------------------------------------------------

Domain Name: STEVENS.EDU

Registrant:
	Stevens Institute of Technology
	Castle Point on Hudson
	Information Technology
	Hoboken, NJ 07030
	USA

Administrative Contact:
	Domain Name Administration
	Stevens Institute of Technology
	Information Technology
	Castle Point on the Hudson
	Hoboken, NJ 07030
	USA
	+1.2012165457
	webmaster@stevens.edu

Technical Contact:
	Domain Name Administration
	Stevens Institute of Technology
	Information Technology
	Castle Point on the Hudson
	Hoboken, NJ 07030
	USA
	+1.2012165457
	webmaster@stevens.edu

Name Servers:
	BETTY.NS.CLOUDFLARE.COM
	HASSLO.NS.CLOUDFLARE.COM

Domain record activated:    25-Jun-1998
Domain record last updated: 28-Dec-2021
Domain expires:             31-Jul-2022
```

### traceroute
![](assets/traceroute.png)

### lsblk
![](assets/lsblk.png)

### date
![](assets/date.png)

### whoami
![](assets/whoami.png)
