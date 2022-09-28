node { 
    String agent = new File( pwd() + '/agents').text
    println agent
}
    
pipeline {
    agent any
    stages {
        stage('Hello6') {
            steps {
                script {
                  echo "Hello Something $agent"                 
                }
            }
        }
   }
}
