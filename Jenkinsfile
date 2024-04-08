pipeline {
    agent any
 
    stages {
        stage('Build') {
            steps {
                echo 'Dockering...'
                sh 'cd ~/Django_News_App/news_Application && python3 manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}
