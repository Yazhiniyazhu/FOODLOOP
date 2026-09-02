pipeline {
    agent any

    stages {

        stage('Verify Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t monika123/foodloop:latest .'
            }
        }

    }
}
