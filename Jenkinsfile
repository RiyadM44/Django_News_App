pipeline {
    agent any
    stages {
        stage('SSH to First Instance') {
            steps {
                script {
                    sshagent(['ssh-agent']) {
                        sh 'ssh -o StrictHostKeyChecking=no ubuntu@18.196.62.224 "mkdir ~/saiid"'
                    }
                }
            }
        }
    }
}


        // stage('Stop and Remove Container From First Instance') {
        //     steps {
        //         script {
        //             // Stop the container if it's running
        //             sh 'docker stop ry || true'
                    
        //             // Remove the container if it exists
        //             sh 'docker rm ry || true'
        //         }
        //     }
        // }

        // stage('Run Docker Container On First Instance') {
        //     steps {
        //         // Pull the latest version of the Docker image
        //         sh 'docker pull riyadm44/djangonewsimage:latest'

        //         // Run the Docker container with the specified options
        //         sh 'docker run -d -p 8000:8000 --name ry riyadm44/djangonewsimage'
        //     }
        // }
//     }
// }
