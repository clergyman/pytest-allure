def rc
pipeline {
    agent any
    parameters {
        string(name: 'MY_ENV', defaultValue: '0.7', description: 'First threshold value (e.g., for use in JavaScript code)')
        string(name: 'MY_ENV2', defaultValue: '0.95', description: 'Second threshold value (e.g., for use in JavaScript code)')
    }
    tools {
        nodejs 'node22'
    }

    stages {
        stage('Checkout') {
            steps {
                // checkout specific branch
                git branch: 'main', url: 'https://github.com/clergyman/pytest-allure'
            }
        }
        stage('Setup') {
            parallel {
                stage('Node') {
                    steps {
                        sh '''
                          node --version
                          npm --version
                          npm install -g allure
                          npm init -y
                          npm install -D allure
                        '''
                    }
                }
                stage('Python') {
                    steps {
                        sh '''
                          set -e
                          TOOLS="$WORKSPACE/.tools"
                          PY="$TOOLS/python"
        
                          mkdir -p "$TOOLS"
                          if [ ! -x "$PY/bin/python3" ]; then
                            curl -L https://github.com/indygreg/python-build-standalone/releases/download/20240224/cpython-3.12.2+20240224-x86_64-unknown-linux-gnu-install_only.tar.gz \
                              | tar -xz -C "$TOOLS"
                            #mv "$TOOLS/python" "$PY"
                          fi
        
                          export PATH="$PY/bin:$PATH"
                          python3 -m ensurepip
                          python3 -m pip install --upgrade pip
                          python3 -m pip install -r requirements.txt
                          python3 -m pip install allure-pytest
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    rc = sh(
                        script: '''
                                  set -e
                                  export PATH="$WORKSPACE/.tools/python/bin:$PATH"
                                  export MY_ENV="${MY_ENV}"
                                  export MY_ENV2="${MY_ENV2}"
                                  npx allure run -- pytest --alluredir=build/allure-results
                                ''',
                        returnStatus: true
                    )
                    if (rc == 1) {
                        currentBuild.result = 'UNSTABLE'
                    } else if (rc > 1) {
                        error("Failed with exit code ${rc}")
                    }
                }
            }
        }
        stage('publish HTMl report') {
            steps {
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, icon: '', keepAll: true, reportDir: "$WORKSPACE/allure-report", reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: 'allure', useWrapperFileDirectly: false])
            }
        }
        
        stage('Trigger Downstream Pipeline') {
            when {
                expression { rc == 0 }
            }
            steps {
                build job: 'allure3-pytest-freestyle',
                      parameters: [
                          string(name: 'UPSTREAM_BUILD', value: "${env.BUILD_NUMBER}"),
                      ],
                      propagate: false,  // don't let downstream failure affect this build
                      wait: false
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}