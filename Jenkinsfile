pipeline {
    agent any
    stages {
        stage('Run Test') {
            when{
                not{
                    branch 'main'
                }
            }
            steps {
                echo 'Building...'
                
                sh '''#!/bin/bash
                    cd webapp/tests/
                    python3 -m nltk.downloader all
                    pytest-3
                '''
            }
        }
        stage('Build Docker images') {
            when{
                anyOf{
                    branch 'release-*'
                    branch 'develop'
                }
            }
            steps {
                echo 'Testing...'
            }
        }
        stage('Push Docker Images') {
            when{
                anyOf{
                    branch 'release-*'
                    branch 'develop'
                }
            }
            steps {
                echo 'Deploying...'
            }
        }
        stage('Launch app on server') {
            when{
                anyOf{
                    branch 'release-*'
                    branch 'develop'
                }
            }
            steps {
                echo 'Deploying...'
            }
        }
    }
}
