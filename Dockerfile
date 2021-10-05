FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    imagemagick parallel

WORKDIR /workdir
# RUN for d in */ ; do find . -name "*.depth.pgm" | parallel -I% --max-args 1 convert % %.png done
docker run -it -v '/opt/datasets/test/extracted/':'/workdir' imagemagick:latest
for d in */ ; do echo $d; find . -name "*.depth.pgm" | parallel -I% --max-args 1 convert % %.png; done

docker run -it -v '/opt/datasets/val/extracted/':'/workdir' imagemagick:latest
for d in */ ; do > echo $d; > find . -name "*.jpg" | parallel -I% --max-args 1 convert % %.png; > done