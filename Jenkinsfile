stage('Run tests') {
    node {
        deleteDir()
        checkout scm

        sh """
            behave
        """
    }
}
