pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Dockering...'
                sh 'python3 manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
