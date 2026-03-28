#!/bin/bash


# Update the Packages
sudo apt update -y

# This commad will install the docker
sudo apt install -y docker.io curl apt-transport-https

# This command will start and enable the docker
sudo systemctl start docker
sudo systemctl enable docker

#This command is used to give permission forthe docker
sudo usermod -aG docker ubuntu

#This command will apply new group immideatly
newgrp docker

#This command will install teh kubectl
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"

chmod +x kubectl

sudo mv kubectl /usr/local/bin/

#This command is used to install the minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

sudo install minikube-linux-amd64 /usr/local/bin/minikube

#This command will start Minikube with Docker driver
sudo -u ubuntu minikube start --driver=docker --memory=700mb --cpus=1
