if("$BRANCH_NAME".contains("main")){
    properties([
    parameters([
    string(name: 'SomethingElse', defaultValue: 'Option', description: 'Cloud Type')
    ])
])
} else {
    println "If not set something different"
}
    

pipeline {
    agent any
    stages{
        stage("Hello"){
            steps{
                echo "Building Something"
            }
        }
    }
}
