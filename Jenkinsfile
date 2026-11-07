pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo "Building Docker Image"

                bat "docker build -t mypythonflaskapp ."
            }
        }

        stage('Run') {
            steps {
                echo "Running application in Docker Container"

                bat "docker rm -f mycontainer || exit 0"

                bat "docker run -d -p 5000:5000 --name mycontainer mypythonflaskapp"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}