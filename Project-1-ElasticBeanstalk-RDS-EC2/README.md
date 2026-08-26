# Project 1: AWS Elastic Beanstalk with RDS, Accessed from EC2

## 📌 Objective
Deploy an application environment using **AWS Elastic Beanstalk**, provision an
integrated **Amazon RDS** database, and securely access that RDS instance from
a separate **EC2** instance in the same VPC.

## 🛠 Tech Stack
`AWS Elastic Beanstalk` · `Amazon RDS (MySQL)` · `Amazon EC2` · `VPC / Security Groups`

---

## 🚀 Step-by-Step Guide

### Step 1: Create the Elastic Beanstalk Environment
1. Go to **AWS Console → Elastic Beanstalk → Create Application**.
2. Choose platform **Python** and upload/deploy the app in [`sample-app/`](sample-app/).
   - `application.py` — sample Flask app (Beanstalk's default WSGI entry point).
   - `requirements.txt` — Python dependencies.
   - `.ebextensions/01_packages.config` — Beanstalk config file.
3. Under **Configure more options → Database**, select:
   - Engine: `mysql`
   - Instance class: `db.t3.micro` (free-tier friendly)
   - Make sure it deploys **inside the same VPC** as the environment.
4. Launch the environment and wait for the health status to turn **Green**.

**✅ Deliverable:** Screenshot of the Beanstalk environment dashboard showing "Health: Ok".
📸 `screenshots/step1-eb-environment.png`

---

### Step 2: Verify the RDS Instance Created by Beanstalk
1. Go to **RDS Console → Databases** and locate the DB instance Beanstalk created
   (name usually starts with `aweb...` or `ebdb`).
2. Note the **Endpoint** and **Port** — you'll need these in Step 4.
3. Under Beanstalk: **Configuration → Database** also shows these same values as
   environment variables (`RDS_HOSTNAME`, `RDS_PORT`, `RDS_DB_NAME`, `RDS_USERNAME`).

**✅ Deliverable:** Screenshot of the RDS instance detail page.
📸 `screenshots/step2-rds-created.png`

---

### Step 3: Configure Security Groups
1. Open the **RDS security group** (auto-created by Beanstalk).
2. Add an inbound rule:
   - Type: `MySQL/Aurora` (port 3306)
   - Source: the **security group of your standalone EC2 instance** (Step 4)
     — not `0.0.0.0/0`, to keep the DB private.
3. Keep the existing rule that allows the Beanstalk environment itself to connect.

**✅ Deliverable:** Screenshot of the RDS security group inbound rules.
📸 `screenshots/step3-security-group.png`

---

### Step 4: Launch a Separate EC2 Instance & Connect to RDS
1. Launch a new EC2 instance (Amazon Linux 2023) in the **same VPC** as Beanstalk.
2. SSH into it:
   ```bash
   ssh -i your-key.pem ec2-user@<EC2_PUBLIC_IP>
   ```
3. Run [`scripts/connect_rds_from_ec2.sh`](scripts/connect_rds_from_ec2.sh) to install
   the MySQL client and connect using the RDS endpoint from Step 2.
4. Run [`scripts/test_read_write.sql`](scripts/test_read_write.sql) to confirm read/write
   access works end-to-end.

**✅ Deliverable:** Terminal screenshot showing a successful `mysql>` connection and
query output.
📸 `screenshots/step4-ec2-to-rds.png`

---

### Step 5 (Optional Enhancements)
- Store RDS credentials in **AWS Secrets Manager** instead of plain environment variables.
- Add a CloudWatch alarm on `DatabaseConnections` or `CPUUtilization`.

**✅ Deliverable (if completed):** Screenshot of Secrets Manager secret / CloudWatch alarm.
📸 `screenshots/step5-optional-enhancements.png`

---

## 📂 Repository Structure
```
Project-1-ElasticBeanstalk-RDS-EC2/
├── README.md
├── sample-app/
│   ├── application.py
│   ├── requirements.txt
│   └── .ebextensions/01_packages.config
├── scripts/
│   ├── connect_rds_from_ec2.sh
│   └── test_read_write.sql
└── screenshots/
```

## 🔐 Security Considerations
- RDS is **never** exposed publicly — only reachable from the Beanstalk environment
  and the specific EC2 instance's security group.
- Credentials are pulled from Beanstalk environment variables rather than hard-coded.
- Recommend rotating DB credentials via Secrets Manager for production use.

## ✅ Deliverables Checklist
- [ ] Deployed Elastic Beanstalk environment with application
- [ ] Screenshot of RDS database created via Beanstalk
- [ ] Commands used to access RDS from EC2 (see `scripts/`)
- [ ] (Optional) Test script for database operations
- [ ] Architecture diagram, setup guide, security notes, screenshots (this README)
