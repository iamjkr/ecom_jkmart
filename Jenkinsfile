pipeline {
    agent { label 'dj-agent'}
    
    stages {
        stage('Code'){
            steps{
               git 'https://github.com/iamjkr/ecom_jkmart.git'
            
            }
            
        }
        stage('Buid'){
             steps{
                 sh 'docker build . -t iamjkr/webe:latest'
            }
            
        }
        stage('Push'){
            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerHub',usernameVariable: 'docker_username', passwordVariable: 'docker_password')])
                {
                    sh 'docker login -u $docker_username -p $docker_password'
                    sh 'docker push iamjkr/webe:latest'
                }
            }
        }
  
  
        stage('Test'){
            steps{
                echo "Testing code"
            }
            
        }
        stage('Deploy'){
            steps{
                sh 'docker-compose down && docker-compose up -d --no-deps'
            }
            
        }
    }
}
