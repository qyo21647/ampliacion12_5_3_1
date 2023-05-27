pipeline{
  agent any
  triggers{
    pollSCM('* * * * *')
  }
  stages{
    stage('Checkout'){
      steps{
        checkout scm
      }
    }
    stage('Unit test'){
      steps{
        sh 'python3 -m unittest discover -s . -p "test_calculator.py"'
      }
    }
    stage('Code coverage'){
      steps{
        sh 'pip install coverage'
        sh 'coverage run --source=. -m unittest discover -s . "test_calculator.py"
        sh 'coverage report -m'
      }
    }
  }
}
