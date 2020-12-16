def version = "0.3-dev";

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
                sh "echo ${version}"
                
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
                sh "docker build --tag cdrault/tweet-search-project:${version} ."
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
                sh "docker run -d -p 5001:5000 --name tweet-search-container cdrault/tweet-search-project:${version}"
                sh "docker commit tweet-search-container cdrault/tweet-search-project:${version}"
                sh "docker stop tweet-search-container"
                sh "docker rm tweet-search-container"
                sh "docker push cdrault/tweet-search-project:${version}"
            }
        }
        stage('Launch app on server') {
            when{
                anyOf{
                    branch 'develop'
                }
            }
            steps {
                sh "docker stop tweet-search-project-dev"
                sh "docker rm tweet-search-project-dev"
                sh "docker run -d -p 5000:5000 --name tweet-search-project-dev cdrault/tweet-search-project:${version}"
            }
        }
    }
}
