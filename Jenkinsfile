
pipeline {
  agent any
  environment {
    HEADLESS = "1"
    CI = "true"
  }
  stages {
    stage('Setup Python') {
      steps {
        sh 'python3 -V || python -V'
      }
    }
    stage('Install') {
      steps {
        sh 'python3 -m venv .venv || python -m venv .venv'
        sh '. .venv/bin/activate && pip install -U pip && pip install -r requirements.txt'
      }
    }
    stage('Run Tests') {
      steps {
        sh '. .venv/bin/activate && pytest --html=report.html --self-contained-html -n auto'
      }
    }
    stage('Archive Report') {
      steps {
        archiveArtifacts artifacts: 'report.html', fingerprint: true
      }
    }
  }
  post {
    always {
      junit allowEmptyResults: true, testResults: '**/junit*.xml'
    }
  }
}
