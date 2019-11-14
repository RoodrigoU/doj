#!/bin/bash
sudo docker run --rm   --name pg-docker -e POSTGRES_USER=dojopy -e POSTGRES_PASSWORD=dojopy -d -p 5432:5432 -v $HOME/docker/volumes/postgres_dojopy:/var/lib/postgresql/data  postgres;
