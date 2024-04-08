pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Dockering...'
                sh 'cd ~/workspace/RY/Django_News_App/news_Application && python3 manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
