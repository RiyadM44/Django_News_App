pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Dockering...'
                script {
                    // Change directory to your news_Application
                    dir('news_Application') {
                        // Run the command for Apache
                        sh 'python3 manage.py runserver 0.0.0.0:8000'
                    }
                }
            }
        }
    }
}
