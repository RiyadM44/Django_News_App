pipeline {
    agent any
    stages {
        stage('Deploy on First Instance') {
            steps {
                script {
                    // Execute SSH command and wait for completion
                    sshagent(['ssh-agent']) {
                        def sshResult = sh(script: 'ssh -o StrictHostKeyChecking=no ubuntu@18.196.62.224', returnStatus: true)
                        if (sshResult != 0) {
                            error "SSH connection failed"
                        }
                        // Stop the container if it's running
                        sh 'docker stop ry || true'
                        
                        // Remove the container if it exists
                        sh 'docker rm ry || true'
                        
                        // Pull the latest version of the Docker image
                        sh 'docker pull riyadm44/djangonewsimage:latest'

                        // Run the Docker container with the specified options
                        sh 'docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage'
                    }
                      
                }
            }
        }
    }
}
