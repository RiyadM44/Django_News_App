pipeline {
    agent any
    stages {
        stage('Deploy on First Instance') {
            steps {
                script {
                    // Execute SSH command and wait for completion
                    sshagent(['ssh-agent']) {
                        def sshResult = sh(script: '''
                            ssh -o StrictHostKeyChecking=no ubuntu@18.185.48.217 '
                                docker stop ry || true &&
                                docker rm ry || true &&
                                docker rmi riyadm44/djangonewsimage || true &&
                                docker pull riyadm44/djangonewsimage:latest &&
                                docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage &&
                                cd Django_News_App/ &&
                                git pull origin main &&
                                cd news_Application/ &&
                                python3 manage.py makemigrations &&
                                python3 manage.py migrate'
                            ''', returnStatus: true)
                        if (sshResult != 0) {
                            error "SSH connection failed"
                        }
                    }
                }
            }
        } 
        stage('Deploy on Second Instance') {
            steps {
                script {
                    // Execute SSH command and wait for completion
                    sshagent(['ssh-agent']) {
                        def sshResult = sh(script: '''
                            ssh -o StrictHostKeyChecking=no ubuntu@3.67.186.141 '
                                docker stop ry || true &&
                                docker rm ry || true &&
                                docker rmi riyadm44/djangonewsimage || true &&
                                docker pull riyadm44/djangonewsimage:latest &&
                                docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage &&
                                cd Django_News_App/ &&
                                git pull origin main ' 
                            ''', returnStatus: true)
                        if (sshResult != 0) {
                            error "SSH connection failed"
                        }
                    }
                }
            }
        }        
    }
}
