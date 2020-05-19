node{
  def app
  
  stage('Clone') {
    checkout scm
  }
  
  stage('prmier test') {
      sh 'docker ps'
    }
  
  stage('Build image') {
    app = docker.build("e71fc5c0fcb1")
  }
  
  stage('Test nhady') {
    docker.image('e71fc5c0fcb1').withRun('-p 80:80')
      
    }
    
    stage('Test image') {
      sh 'docker ps'
    }
  
    stage('curl') {
      sh 'curl localhost'
    }
  
}
