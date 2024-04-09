pipeline {
    agent any
    stages {
        stage('SSH to First Instance') {
            steps {
                script {
                    // SSH to the first instance using the provided key
                    sh 'ssh -i RHY.pem ubuntu@18.196.62.224'
                }
            }
        }

        stage('Stop and Remove Container From First Instance') {
            steps {
                script {
                    // Stop the container if it's running
                    sh 'docker stop ry || true'
                    
                    // Remove the container if it exists
                    sh 'docker rm ry || true'
                }
            }
        }

        stage('Run Docker Container On First Instance') {
            steps {
                // Pull the latest version of the Docker image
                sh 'docker pull riyadm44/djangonewsimage:latest'

                // Run the Docker container with the specified options
                sh 'docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage'
            }
        }
    }
}
