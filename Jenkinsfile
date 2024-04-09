pipeline {
    agent any
    stages {
        stage('Deploy on First Instance') {
            steps {
                script {
                    // Execute SSH command and wait for completion
                    sshagent(['ssh-agent']) {
                        def sshResult = sh(script: '''
                            ssh -o StrictHostKeyChecking=no ubuntu@3.78.242.227 '
                            docker stop ry || true &&
                            docker rm ry || true &&
                            docker pull riyadm44/djangonewsimage:latest &&
                            docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage'
                        ''', returnStatus: true)
                        if (sshResult != 0) {
                            error "SSH connection failed"
                        }
                    }
                }
            }
        }
        stage('Deploy on Second Instance') {
            steps {
                script {
                    // Execute SSH command and wait for completion
                    sshagent(['ssh-agent']) {
                        def sshResult = sh(script: '''
                            ssh -o StrictHostKeyChecking=no ubuntu@18.192.127.84 '
                            docker stop ry || true &&
                            docker rm ry || true &&
                            docker pull riyadm44/djangonewsimage:latest &&
                            docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage'
                        ''', returnStatus: true)
                        if (sshResult != 0) {
                            error "SSH connection failed"
                        }
                    }
                }
            }
        }
    }
}

