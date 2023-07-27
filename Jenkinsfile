pipeline{
    agent any
    
    stages{
        stage('SCM Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/samadhand/newflask.git'
            }
        }
        stage('docker image build'){
            steps{
                sh '/usr/bin/docker image build -t dhanavesamadhan/flaskimage .'
            }
        }
        stage('docker auth'){
            steps{
                sh 'echo dckr_pat_-h6-1B_Oh1E1kreihXH9Zez7o54 | /usr/bin/docker login -u dhanavesamadhan --password-stdin'
            }
        }
        stage('docker image push'){
            steps{
                sh '/usr/bin/docker image push dhanavesamadhan/flaskimage'
            }
        }
        stage('delivery confirmation'){
            steps{
                input 'Do you want to deploy  application'
            }
        }
        stage('docker remove service'){
            steps{
                sh '/usr/bin/docker service rm flaskservice'
            }
        }
        stage('docker create service'){
            steps{
                sh '/usr/bin/docker service create --name flaskservice --replicas 2 -p 8000:8000 dhanavesamadhan/flaskimage'
            }
        }

    }
}
