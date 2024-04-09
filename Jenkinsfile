pipeline {
    agent any
    stages {
        stage('SSH to First Instance') {
            steps {
                sshagent(['ssh-agent']) {
                    echo "Attempting SSH connection"
                    sh 'ssh -tt -o StrictHostKeyChecking=no ubuntu@18.196.62.224'
                    echo "SSH command executed"
                    sh 'mkdir hello'
                    echo "mkdir command executed"
                }
            }
        }
    }
}
