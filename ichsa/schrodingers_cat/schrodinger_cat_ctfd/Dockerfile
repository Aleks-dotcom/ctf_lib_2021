FROM gcc:10-buster as build

RUN mkdir -p /app
COPY schrodinger_cat.c /app

WORKDIR /app

RUN gcc -pthread schrodinger_cat.c -no-pie -lrt -o app.out

FROM python:3.7.8-slim as app

WORKDIR /app
COPY flag.txt /app/	
RUN chmod 0444 /app/flag.txt

COPY --from=build /app/app.out /app/app.out
COPY schrodinger_cat.py /app/schrodinger_cat.py

RUN apt-get update && apt-get install -y socat

# Set non root user
RUN useradd -c 'User' -m -d /home/user -s /bin/bash user
RUN chown -R user:user /home/user

USER user
ENV HOME /home/user

EXPOSE 8001
CMD ["socat", "TCP-LISTEN:8001,reuseaddr,fork", "EXEC:'python /app/schrodinger_cat.py'"]