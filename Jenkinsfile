pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shoval/wog'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run') {
            steps {
                echo 'Running the Dockerized application...'
                sh '''
                docker run -d --name test_container -p 8777:5000 \
                -v $(WORKSPACE)/scores.txt:/Scores.txt \
                $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running Selenium tests...'
                    bat 'python3 Tests/e2e.py'
                }
            }
        }

       stage('Finalize') {
    steps {
        script {
            steps {
                echo 'Finalizing: Cleaning up and pushing to DockerHub...'
                sh '''
                docker stop test_container || true
                docker rm test_container || true
                docker login -u your_dockerhub_username -p your_dockerhub_password
                docker push $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }
    }
}

    }

    post {
        always {
            echo 'Cleaning up...'
            sh '''
            docker stop test_container || true
            docker rm test_container || true
            docker rmi $DOCKER_IMAGE:$DOCKER_TAG || true
            '''
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}