Model weight dowload from [Google Drive](https://drive.google.com/file/d/1u9uPkI3CSCk0O4_xL2pmY4QRajqLNS-m/view?usp=sharing)

# how to run
[build container]
sudo docker build -t fastapi_docker .      


[run container]
sudo docker run --name fastapi_docker_4 -p 7100:8000 fastapi_docker

[open web]
http:0.0.0.0:7100/docs
