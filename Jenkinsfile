stage('Build containers') {
    node {
        deleteDir()
        checkout scm

        docker.build('behave-test-build-env',
                     '-f Dockerfile.test .')
    }
}

stage('Run tests') {
    node {
        deleteDir()
        checkout scm

        docker.image('behave-test-build-env')
              .inside {
            try {
                sh """
                    behave --junit
                """
            } finally {
                junit 'reports/*.xml'
            }
        }
    }
}
