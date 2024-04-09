pipeline {
    agent any
    stages {
        stage('SSH to First Instance') {
            steps {
                sshagent(['ssh-agent']) {
                    sh 'ssh -tt -o StrictHostKeyChecking=no ubuntu@18.196.62.224'
                    sh 'mkdir hello'
                }
            }
        }
    }
}

    
