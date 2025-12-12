pipeline {
    agent any

    environment {
        // Set environment variables here or in Jenkins Global Config
        HEADLESS = "true"
        USE_MOCK_DB = "true" // Set to false if connecting to real DB in CI
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install -r requirements.txt
                    playwright install chromium
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Running tests and generating Allure results
                    sh 'pytest --alluredir=allure-results'
                }
            }
        }
    }

    post {
        always {
            // Generate Allure Report
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

            // Archive build artifacts if needed (e.g., screenshots, videos)
            archiveArtifacts artifacts: 'test-results/**, allure-results/**', allowEmptyArchive: true
        }
    }
}
