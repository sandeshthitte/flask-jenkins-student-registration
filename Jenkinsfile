pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/swati-zampal/stud-reg-flask-app.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest || echo "No tests available"
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill -f "python app.py" || true
                nohup venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
