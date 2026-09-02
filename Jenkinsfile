pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting FoodLoop code from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t foodloop .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker rm -f foodloop-container || true'
                sh 'docker run -d -p 8501:8501 --name foodloop-container foodloop'
            }
        }
    }
}
