def agent1 = "any"
node { 
    agent1 = new File( pwd() + '/agents').text.trim()
    println agent
}
    
pipeline {
    agent any
    stages {
        stage('Hello6') {
            steps {
                script {
                  echo "Hello Something $agent1"                 
                }
            }
        }
   }
}
