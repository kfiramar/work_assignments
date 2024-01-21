node('zip-job-docker') {
    docker.image('python:3.10').inside('--privileged') {
        // Set environment variables
        env.ARTIFACTORY_SERVER = 'http://34.165.44.255'
        env.ARTIFACTORY_REPO = "binary-storage/${env.VERSION}"
        env.ARTIFACTORY_USER = 'super-user'
        env.ARTIFACTORY_PASSWORD = 'Qw12856!'


        try {
            // Build stage
            stage('Build') {
                sh 'python zip_job.py'
            }


            // Publish stage
            stage('Publish') {
                if (currentBuild.resultIsBetterOrEqualTo('SUCCESS')) {
                    sh """
                        curl -u${env.ARTIFACTORY_USER}:${env.ARTIFACTORY_PASSWORD} \
                        -T path/to/zip/files/*.zip \
                        ${env.ARTIFACTORY_SERVER}/${env.ARTIFACTORY_REPO}/
                    """
                }
            }
        } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            throw e
        } finally {
            // Report stage
            stage('Report') {
                mail to: 'kfira2709@gmail.com',
                     subject: "Build ${env.BUILD_TAG} Status: ${currentBuild.currentResult}"
            }


            // Cleanup stage
            stage('Cleanup') {
                cleanWs()
            }
        }
    }
}
