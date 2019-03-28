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

        sh """
            behave
        """
    }
}
