pipeline {
    agent any
    environment {
        IMAGE = "naveena818/food-app"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/naveenaece2000/food-delivery-ops.git'
            }
        }
        stage('Build Image') {
            steps {
                sh "docker build -t $IMAGE:latest ."
            }
        }
        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push $IMAGE:latest"
                }
            }
        }
        stage('Deploy K8s') {
            steps {
                // Assuming Jenkins runs on a machine that already has kubectl configured
                sh 'kubectl apply -f k8s/deployment.yaml' 
            }
        }
    }
}