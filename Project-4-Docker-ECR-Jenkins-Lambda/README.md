# Project 4: Automated Docker Image Deployment to Amazon ECR with Jenkins & Lambda

## 📌 Objective
Build a CI/CD pipeline in **Jenkins** that builds a Docker image, pushes it to
**Amazon ECR** on every code change, and triggers an **AWS Lambda** function
for post-deployment tasks (logging + notification).

## 🏗 Architecture
```
GitHub → Jenkins (build+push) → Amazon ECR → EventBridge/Direct Invoke → Lambda → DynamoDB + SNS
```

## 🛠 Tech Stack
`Docker` · `Amazon ECR` · `Jenkins` · `AWS Lambda` · `DynamoDB` · `SNS` · `EventBridge`

---

## 🚀 Step-by-Step Guide

### Step 1: Docker Setup
The sample app lives in [`app/`](app/) (a minimal Flask API) with a [`Dockerfile`](Dockerfile).
```bash
docker build -t docker-ecr-jenkins-lambda-demo .
docker run -p 5000:5000 docker-ecr-jenkins-lambda-demo
curl http://localhost:5000/health
```

**✅ Deliverable:** Screenshot/output of `docker run` and the successful `curl` response.
📸 `screenshots/step1-docker-run.png`

---

### Step 2: Create the ECR Repository & Manual Push (initial test)
```bash
aws ecr create-repository --repository-name docker-ecr-jenkins-lambda-demo

aws ecr get-login-password --region ap-south-1 | \
  docker login --username AWS --password-stdin <account-id>.dkr.ecr.ap-south-1.amazonaws.com

docker tag docker-ecr-jenkins-lambda-demo:latest \
  <account-id>.dkr.ecr.ap-south-1.amazonaws.com/docker-ecr-jenkins-lambda-demo:latest

docker push <account-id>.dkr.ecr.ap-south-1.amazonaws.com/docker-ecr-jenkins-lambda-demo:latest
```

**✅ Deliverable:** Screenshot of the image visible in the ECR console.
📸 `screenshots/step2-ecr-repo.png`

---

### Step 3: Jenkins Pipeline
[`Jenkinsfile`](Jenkinsfile) defines a 5-stage pipeline:
1. **Checkout** — pulls the latest code from GitHub
2. **Build Docker Image**
3. **Login to ECR** — using Jenkins' AWS credentials binding
4. **Tag & Push to ECR** — tags with `${BUILD_NUMBER}-${GIT_COMMIT}` and `latest`
5. **Trigger Lambda** — invokes the post-deploy Lambda directly

Configure in Jenkins:
- Add AWS credentials (`aws-jenkins-creds`) and the account ID (`aws-account-id`)
  under **Manage Jenkins → Credentials**.
- Create a **Pipeline** job pointing at this repo, using the `Jenkinsfile`.

**✅ Deliverable:** Screenshot of a successful Jenkins pipeline run (all stages green).
📸 `screenshots/step3-jenkins-pipeline.png`

---

### Step 4: Lambda Function Integration
[`lambda/lambda_function.py`](lambda/lambda_function.py) logs each push to a
**DynamoDB** table (`ecr-push-log`) and optionally sends an **SNS** notification.

Trigger it either way:
- **Direct invoke** from the last Jenkinsfile stage (already wired up), or
- **EventBridge rule** — see [`lambda/eventbridge-rule.json`](lambda/eventbridge-rule.json),
  which matches ECR `PUSH` events for this repository.

Deploy:
```bash
cd lambda
pip install -r requirements.txt -t .
zip -r function.zip .
aws lambda create-function \
  --function-name ecr-push-notifier \
  --runtime python3.12 \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip \
  --role arn:aws:iam::<account-id>:role/lambda-ecr-notifier-role \
  --environment "Variables={DYNAMODB_TABLE=ecr-push-log,SNS_TOPIC_ARN=<topic-arn>}"
```

**✅ Deliverable:** Screenshot of the DynamoDB table row + (optional) SNS email/Slack notification.
📸 `screenshots/step4-lambda-dynamodb.png`

---

### Step 5 (Optional Enhancements)
- Slack notification instead of/in addition to SNS.
- Trigger an ECS service update from Lambda after a successful push.

**✅ Deliverable (if completed):** Screenshot of the Slack message / ECS deployment.
📸 `screenshots/step5-optional.png`

---

## 📂 Repository Structure
```
Project-4-Docker-ECR-Jenkins-Lambda/
├── README.md
├── Dockerfile
├── .dockerignore
├── Jenkinsfile
├── app/
│   ├── app.py
│   └── requirements.txt
├── lambda/
│   ├── lambda_function.py
│   ├── requirements.txt
│   └── eventbridge-rule.json
└── screenshots/
```

## 🔐 Security Considerations
- AWS credentials are stored in Jenkins' credentials manager, never hard-coded
  in the `Jenkinsfile`.
- The Lambda execution role should follow least privilege: only
  `dynamodb:PutItem` on the specific table and `sns:Publish` on the specific topic.
- ECR repository can have image scanning on push enabled for vulnerability checks.

## ✅ Deliverables Checklist
- [ ] Jenkinsfile (this repo)
- [ ] Dockerfile and source code (this repo)
- [ ] Lambda function code (this repo)
- [ ] Code pushed to GitHub, link shared in documentation
- [ ] README with architecture, deployment steps, and component explanation (this file)
- [ ] Sample logs / screenshots of image push and Lambda execution
