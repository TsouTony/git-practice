pipeline {
	agent any
	
	stages {
		stage('Build') {
			steps {
				echo "Building v3, ID : ${env.BUILD_ID} on ${env.JENKINS_URL}"
			}
		}
		stage('Test') {
			steps {
				echo 'Testing v3'
			}
		}
		stage('Deploy') {
			steps {
				echo 'Deploying v3'
			}
		}
	}
}