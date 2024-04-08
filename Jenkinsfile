pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Dockering...'
                sh 'sudo docker run -p 80:80 -d --name apache httpd'
            }
        }
    }
}
