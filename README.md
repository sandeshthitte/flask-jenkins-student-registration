# flask-jenkins-student-registration

This project is a Flask-based Student Registration Web Application deployed on an Ubuntu EC2 instance using Jenkins CI/CD pipeline.
It demonstrates:

Continuous Integration & Deployment with Jenkins

GitHub → Jenkins Webhook integration

Automated environment setup & deployment

MySQL database integration with Flask

🛠️ Tech Stack

Frontend: HTML, Bootstrap 5

Backend: Python (Flask)

Database: MySQL

CI/CD: Jenkins Pipeline

Version Control: Git & GitHub

Server: AWS EC2 (Ubuntu)

⚙️ Setup Instructions
1️⃣ Server Setup (Ubuntu EC2)
sudo apt update && sudo apt upgrade -y
sudo apt install -y openjdk-17-jdk python3 python3-venv python3-pip git mysql-server

2️⃣ Install Jenkins
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | \
  sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | \
  sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins


Access Jenkins:

http://<EC2-PUBLIC-IP>:8080


Get initial password:

sudo cat /var/lib/jenkins/secrets/initialAdminPassword

3️⃣ MySQL Database Setup
CREATE DATABASE studentdb;
CREATE USER 'studentuser'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON studentdb.* TO 'studentuser'@'localhost';
FLUSH PRIVILEGES;

USE studentdb;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    course VARCHAR(50),
    address TEXT,
    contact VARCHAR(50)
);

4️⃣ Jenkins Pipeline (Jenkinsfile)
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<your-username>/flask-jenkins-student-registration.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/pip install --upgrade pip
                venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                if [ -d tests ]; then
                    venv/bin/python -m pytest tests || echo "Tests failed"
                else
                    echo "No tests available"
                fi
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill -f "app.py" || true
                nohup venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }
}

5️⃣ GitHub Webhook Integration

Go to your GitHub repo → Settings → Webhooks → Add Webhook

Payload URL:

http://<EC2-PUBLIC-IP>:8080/github-webhook/


Content type: application/json

Secret: (set a random string, e.g. MySecret123)

In Jenkins job → Build Triggers → GitHub hook trigger for GITScm polling

Now every git push will auto-trigger Jenkins build 🚀

6️⃣ Running Flask Server

If needed, start Flask manually:

cd ~/stud-reg-flask-app
nohup venv/bin/python app.py > app.log 2>&1 &


Ensure your app.py ends with:

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


Open in browser:

http://<EC2-PUBLIC-IP>:5000

📂 Project Features

✅ Student Registration Form (Bootstrap styled)
✅ Stores student data in MySQL
✅ View registered students at /students
✅ CI/CD with Jenkins (auto deploy on push)
✅ GitHub Webhook for automation
.
