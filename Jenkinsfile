pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                script {
                  echo "Hello ${REF_YCR}"
                    echo "${scm.branches[0].name}"
                }
            }
        }
   }
}
