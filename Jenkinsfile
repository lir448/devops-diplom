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
  stage('Docker build') {
    def customImage = docker.build("lir448/covid-stats:${env.BUILD_ID}", "-f ${dockerfile} ./dockerfiles") 
    customImage.push()
  }
}
