pipeline {
    agent any
    environment {
        DOCKER_USER = "abhishek661"
        DOCKER_CREDS = "dockerhub_cred"
    }
    stages {
        stage ("CheckOut Code") {
            steps {
                git branch: "main",
                    url: "https://github.com/Abhi7022-hash/Ecommerce.git"
            }
        }
        stage ("Build Images") {
            steps {
                sh '''
                docker build -t $DOCKER_USER/f2:front frontend-service
                docker build -t $DOCKER_USER/o1:order order-service
                docker build -t $DOCKER_USER/p2:product product-service
                docker build -t $DOCKER_USER/u1:user user-service
                '''

            }
        }
        stage ("Docker Login") {
            steps {
                 withCredentials([usernamePassword)(
                     credentialsid: "DOCKER_CREDS"
                     usernameVariable: "DOCKER_USERNAME"
                     passwordVariable: "DOCKER_PASSWORD"
                 )]) {
                     sh '''
                     docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                     '''
                 }
            }
        }
        stage ("Push Images to Dockerhub") {
            steps {
                sh '''
                docker push $DOCKER_USER/f2:front
                docker push $DOCKER_USER/o1:order
                docker push $DOCKER_USER/p2:product
                docker push $DOCKER_USER/u1:user
                '''
            }
       }
       stage ("Check Kubernetes Access") {
           steps {
               withCredentials([file(credentialsId: 'kubeconfig-cred', variable: 'KUBECONFIG')]) {
                   sh '''
                   export KUBECONFIG = $KUBECONFIG
                   kubectl get nodes
                   '''
               }
           }
       }
       stage("Deploy to Kubernetes") {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-cred', variable: 'KUBECONFIG')]) {
                    sh '''
                    export KUBECONFIG=$KUBECONFIG
                    kubectl apply -f k8s/deployments/
                    kubectl apply -f k8s/services
                    kubectl apply -f k8s/configmaps
                    kubectl apply -f k8s/secrets



                    '''
                }
            }
       } 



















 




        





























