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
                    /home/cdrault/.local/bin/pytest
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
