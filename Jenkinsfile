pipeline {
    agent any
    stages {
        stage('SSH to Instance') {
            steps {
                sshagent(['849d5fe9-ae71-4c4e-9167-74ba2bb3c39c']) {
                    sh 'ssh ubuntu@3.65.228.31'
                }
            }
        }

        stage('Stop and Remove Container') {
            steps {
                script {
                    // Stop the container if it's running
                    sh 'docker stop ry || true'
                    
                    // Remove the container if it exists
                    sh 'docker rm ry || true'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                // Pull the latest version of the Docker image
                sh 'docker pull riyadm44/djangonewsimage:latest'

                // Run the Docker container with the specified options
                sh 'docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage'
            }
        }
    }
}
