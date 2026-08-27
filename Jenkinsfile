pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip3 install --break-system-packages pytest'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python3 -m pytest tests/'
            }
        }
    }
}
