#!/bin/bash
docker build . -t langnet-bridge --file Dockerfile
docker-compose up -d