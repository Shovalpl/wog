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
                sh """
                    /usr/local/bin/docker system prune -f
                    /usr/local/bin/docker pull python:3.12-slim
                    /usr/local/bin/docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .
                """
            }
        }

        stage('Run') {
            steps {
                echo 'Running the Dockerized application...'
                sh '''
                /usr/local/bin/docker run -d --name test_container -p 8777:5000 \
                -v $(WORKSPACE)/scores.txt:/Scores.txt \
                $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running Selenium tests...'
                    sh 'python3 Tests/e2e.py'
                }
            }
        }

       stage('Finalize') {
    steps {
        script {
            steps {
                echo 'Finalizing: Cleaning up and pushing to DockerHub...'
                sh '''
                /usr/local/bin/docker stop test_container || true
                /usr/local/bin/docker rm test_container || true
                /usr/local/bin/docker login -u shovalpl -p auckppk1!
                /usr/local/bin/docker push $DOCKER_IMAGE:$DOCKER_TAG
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
            /usr/local/bin/docker stop test_container || true
            /usr/local/bin/docker rm test_container || true
            /usr/local/bin/docker rmi $DOCKER_IMAGE:$DOCKER_TAG || true
            '''
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}