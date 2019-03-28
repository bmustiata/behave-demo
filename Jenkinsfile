properties([
    parameters([
        booleanParam(name: 'VERSION_5', defaultValue: true,
                description: 'Should the tests run on version 5'),
        booleanParam(name: 'VERSION_4', defaultValue: true,
                description: 'Should the tests run on version 4')
    ])
])


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
                def command = "behave --junit"

                if (VERSION_5) {
                    command += " -t v5"
                }

                if (VERSION_4) {
                    command += " -t v4"
                }

                sh command
            } finally {
                junit 'reports/*.xml'
            }
        }
    }
}
