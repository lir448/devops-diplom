pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('1') {
            steps {
                echo '1'
                sh 'ls -la'
                sh 'pwd'
            }
        }
        stage('2') {
            steps {
                echo '2'
                sh 'mkdir -p test'
            }
        }
        stage('3') {
            steps {
                echo '3'
                sh 'ls -la'
                dir('test') {
                    sh 'pwd'
                    sh 'echo "Hello!" > test.txt'
                }
            }
        }
        stage('4') {
            steps {
                echo '4'
                sh 'ls -lah */*'
            }
        }
        stage('5') {
            steps {
                script {
                    echo '5'
                    def res = sh(script: "find ./ -name 'test.txt'", returnStdout: true)
                    sh "cat ${res}"
                }
            }
        }
    }
}

