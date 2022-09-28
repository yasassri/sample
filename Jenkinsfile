
// node { 
//     agent1 = new File( pwd() + '/agents').text.trim()
//     println agent1
// }
    
pipeline {
    agent {label getAgentFromFile()}
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

def getAgentFromFile(){
    def agent1 = "default"
    agent1 = new File( pwd() + '/agents').text.trim()
    println agent1
    return agent1
}
