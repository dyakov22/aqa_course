// add functions to pipeline

pipeline {

    agent {
        label 'test_label'
    }

    options {
        timeout(time: 1, unit: 'HOURS')
//         retry(2)
    }

    parameters {
        string(name: 'run_command', defaultValue: 'python3 -m pytest -k test_simple_alert', description: 'Command to run pytest suite')
        choice(name: 'Test choice', choices: ['1', '2', '3'], description: 'Test choice parameter')
    }

//     triggers {
//         cron('* * * * *')
//     }

    environment {
//         PLATFORM = 'CHROME'
//         BROWSER_VERSION = 112
        ENV_FILE = credentials('config_file') // -> path to config file
    }


    stages {
//
//         stage('Checkout') {
//             steps {
//                 git credentialsId: 'git_hub_credentials_with_password', url: 'https://github.com/dyakov22/aqa_course.git'
//             }
//         }
// if jenkins pipeline stores in another place than test project repo

        stage('Create venv') {

            steps {
                script {
                    sh '''
                    python3 -m venv ${WORKSPACE}/venv
                    chmod 777 ${WORKSPACE}/venv/bin/activate  # DO NOT DO IN THIS WAY
                    source ${WORKSPACE}/venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }

            }
        }

        stage('Run test suite') {

            steps {
                script {
                    sh '''
                    source ${WORKSPACE}/venv/bin/activate

                    ${run_command}
                    '''

                }

            }
            post {
                always {
                    allure includeProperties:
                     false,
                     jdk: '',
                     results: [[path: '/allure-results']]
                }
            }

        }
    }
    post {
        always {
            script {
                cleanWs()
                sh 'echo WORKSPACE was deleted'
            }
        }
    }
}