node {
	def app
  
	stage('clone') {
		checkout scm
	}
	stage('Build image') {
		app = docker.build("e71fc5c0fcb1") 
	}
	stage('Test image') {
		docker.image('e71fc5c0fcb1'.withRun('-p 80/80') {c -> sh 'docker ps' sh 'curl localhost' }
   }
}
