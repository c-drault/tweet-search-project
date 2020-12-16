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
                echo "${BUILD_NUMBER}"
                
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
                    branch 'add-jenkinsfile'
                }
            }
            steps {
                sh '''#!/bin/bash
                    cd ..
                    docker build --tag cdrault/tweet-search-project:0.1 .
                '''
            }
        }
        stage('Push Docker Images') {
            when{
                anyOf{
                    branch 'release-*'
                    branch 'develop'
                    branch 'add-jenkinsfile'
                }
            }
            steps {
                sh '''#!/bin/bash
                    cd ..
                    docker run -d -p 5000:5000 --name tweet-search-container cdrault/tweet-search-project:0.1
                    docker commit tweet-search-container cdrault/tweet-search-project:0.1
                    docker push cdrault/tweet-search-project:0.1
                    docker stop tweet-search-container
                    docker rm tweet-search-container
                '''
            }
        }
        stage('Launch app on server') {
            when{
                anyOf{
                    branch 'develop'
                }
            }
            steps {
                sh '''#!/bin/bash
                    docker run -d -p 5000:5000 --name tweet-search-project-dev cdrault/tweet-search-project:0.1
                '''
            }
        }
    }
}
