pipeline {
    agent any

    stages {
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
                // Run the Docker container with the specified options
                sh 'docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage'
            }
        }
    }
}
