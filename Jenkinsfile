pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh "docker build -t lir448/covid-stats:${env.BUILD_ID} ."
                }
            }
        }
    }
}

