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
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python manage.py test'
      }
    }
    stage('Deploy') {
      steps {
        sh 'python manage.py runserver 0.0.0.0:8000'
      }
    }
  }
}
