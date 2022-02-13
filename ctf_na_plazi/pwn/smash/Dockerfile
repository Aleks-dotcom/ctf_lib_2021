# sudo docker build -t system_health_check .
# sudo docker run -d -p 1024:1024 --rm -it system_health_check
#docker run --rm -v $PWD:/pwd --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d --name ctf -i ctf

FROM ubuntu:19.10

RUN apt-get update

RUN dpkg --add-architecture i386 && \
apt-get update && \
apt-get install -y gdb gcc strace  ltrace 

COPY ./hello /
COPY gdbinit /root/.gdbinit
ADD peda/ /root/peda/
COPY libc6-i386_2.23-0ubuntu11.2_amd64.so /usr/lib32/libc-2.30.so
ADD pwndbg/ /root/pwndbg/
COPY libc6-i386_2.23-0ubuntu11.2_amd64.deb /tmp/libc.deb


RUN chmod +x /hello
RUN dpkg -i /tmp/libc.deb
ENTRYPOINT ["/bin/bash"]

