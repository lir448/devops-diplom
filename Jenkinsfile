node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('Docker build') 
  docker.withRegistry('https://index.docker.io/v1/', 'c90b84cb-5146-459c-8756-b74250d6de7f') {
    def customImage = docker.build("lir448/covid-stats:v${env.BUILD_ID}") 
    customImage.push()
  }
}
