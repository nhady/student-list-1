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
  
  stage('Test image') {
    docker.image('e71fc5c0fcb1').withRun('-p 80:80')
      
    }
    
    stage('doker ps') {
      sh 'docker ps'
    }
  
    stage('curl') {
      sh 'curl localhost'
    }
  
}
