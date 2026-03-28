resource "aws_instance" "k8s_server" {
  ami = "ami-0b6c6ebed2801a5cb"
  instance_type = var.instance_type
  key_name = var.key_name
  subnet_id = aws_subnet.public_subnet.id

  vpc_security_group_ids = [
    aws_security_group.devops_sg.id
  ]
  user_data = file("../scripts/install_minikube.sh")

  tags = {
    Name= "kubernetes-server"
  }
}
