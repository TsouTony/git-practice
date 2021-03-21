pipeline {
	agent any
	
	parameters {
		string(name: 'name1', defaultValue: 'dog', description: 'the name of 1')
		string(name: 'name2', defaultValue: 'cat', description: 'the name of 2')
	}
	stages {
		stage('Build') {
			steps {
				echo "Building v3, ID : ${env.BUILD_ID} on ${env.JENKINS_URL}"
			}
		}
		stage('Test') {
			steps {
				echo "Testing v3, via ${params.name1}"
			}
		}
		stage('Deploy') {
			steps {
				echo "Deploying v3, via ${params.name2}"
			}
		}
	}
	post {
		failure {
			mail to{a546518a@gmail}, subject: "git-practice pipeline failed :("
		}
	}
}