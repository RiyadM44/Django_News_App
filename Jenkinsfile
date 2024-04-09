pipeline {
    agent any
    stages {
        stage('SSH to First Instance') {
            steps {
                sshagent(['fb8cd24f-5493-495b-a966-c2a39b0e3d91']) {
                    sh 'ssh ubuntu@18.196.62.224'
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

        stage('Run Docker Container On First Intance') {
            steps {
                // Pull the latest version of the Docker image
                sh 'docker pull riyadm44/djangonewsimage:latest'

                // Run the Docker container with the specified options
                sh 'docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage'
            }
        }
    }
}
