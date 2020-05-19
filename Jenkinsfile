node{
  def app
  
  stage('Clone') {
    checkout scm
  }
  
  stage('Build image') {
    app = docker.build("e71fc5c0fcb1")
  }
  
  stage('Test image') {
    docker.image('e71fc5c0fcb1').withRun('-p 80:80'){c -> 
      sh 'curl -u toto: python -X GET http://192.168.48.158:5000/pozos/api/v1.0/get_student_ages'
    }
  }
  
}
