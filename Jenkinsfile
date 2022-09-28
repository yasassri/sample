def agent1 = "any"
node { 
    agent1 = new File( pwd() + '/agents').text.trim()
    println agent1
}
    
pipeline {
    agent agent1
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
