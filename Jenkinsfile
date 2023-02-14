pipeline {
  agent {
    docker {
      image 'python:3.9-slim-buster'
      args '-p 8000:8000'
    }
  }
  stages {
    stage('Build') {
      steps {
       
      }
    }
    stage('Test') {
      steps {
        sh 'python manage.py test'
      }
    }
    stage('Deploy') {
      steps {
     
      }
    }
  }
}
