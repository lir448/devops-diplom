node {
  environment {
        MYSQL_USER     = credentials('62036b91-363c-493c-b13e-cd3efd829368')
        MYSQL_PASSWORD = credentials('ca729364-5c21-418d-a82c-246941d3fa07')
        MYSQL_HOST     = terraform-20211017181751165500000008.cvvgdyrr5hra.us-east-1.rds.amazonaws.com
        MYSQL_DB       = dbtest
  }
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
  stage('Deploy to test environment on AWS EKS') {
    sh "kubectl apply -n test -f deploy-app.yaml"
  }  
}
