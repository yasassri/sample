node { 
    String agent = new File('agents').text
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
