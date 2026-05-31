
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "mvicente123/dados:1.0"
    }

    stages {

        stage('1. Limpieza workspace') {
            steps {
                cleanWs()
            }
        }

        stage('2. Checkout código') {
        
            steps {
                git branch: 'main', url: 'https://github.com/mvicentv/Dados-_1.0.git'
            }
            
        }

        stage('3. Build Docker image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('4. Test ejecución contenedor') {
            steps {
                script {
                    sh """
                    docker run --name test_container ${DOCKER_IMAGE}
                    docker rm test_container
                    """
                }
            }
        }

        stage('5. Push a DockerHub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
        stage('Análisis estático SonarQube') {
            
            steps {
                withCredentials([string(credentialsId: 'SonarQube', variable: 'SONAR_TOKEN')]) {
                    sh '''
                    /opt/sonar-scanner \
                    -Dsonar.login=$SONAR_TOKEN \
                    -Dsonar.host.url=http://localhost:9000
                    '''
                    }
                }
                    
        }
    }
            

    post {
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}
