pipeline {
    agent any // This means Jenkins can run the pipeline on any available agent (including the master)

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                // Git checkout is handled automatically by the SCM configuration of the job
                // unless you configure it explicitly here for multiple repositories.
            }
        }

        stage('Build') {
            steps {
                echo 'Building (installing dependencies)...'
                // For a simple Python app, this might just be a placeholder.
                // If you had a requirements.txt, it would be: sh 'pip install -r requirements.txt'
                sh 'echo "No specific build steps for this simple Python app, but dependencies would go here."'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 src/test_app.py' // Execute the Python unit tests
            }
        }

        stage('Quality Check (Simulated)') {
            steps {
                echo 'Performing basic quality checks...'
                sh 'echo "Simulating a static code analysis or linting check..."'
                // In a real project, you might run tools like 'pylint src/app.py' here
            }
        }

        stage('Deploy (Simulated CI/CD)') {
            steps {
                echo 'Deploying application...'
                // In a real CI/CD, this would deploy to a staging/production environment.
                // This could involve pushing Docker images, deploying to Kubernetes, SSHing files, etc.
                sh 'echo "Simulating deployment to a development environment..."'
                sh 'echo "Application deployed successfully (simulated)." > deployment_log.txt'
            }
        }
    }

    post { // Actions to take after the pipeline completes
        always { // Always run, regardless of build status
            echo 'Pipeline finished.'
            // Clean up workspace after build to save disk space
            deleteDir()
        }
        success { // Only run if pipeline succeeds
            echo 'Pipeline succeeded! 🎉'
        }
        failure { // Only run if pipeline fails
            echo 'Pipeline failed! 😢'
            // You could add email notifications or Slack messages here
        }
    }
}
