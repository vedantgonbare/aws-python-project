# AWS Python Automation 🚀

Automate AWS infrastructure using Python (boto3). 
Provision, manage, and clean up EC2 & S3 resources — no console needed.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![AWS](https://img.shields.io/badge/AWS-boto3-orange?logo=amazon-aws)
![License](https://img.shields.io/badge/license-MIT-green)

---

## What This Does

| Script | Action |
|--------|--------|
| `create_ec2_instance.py` | Finds latest Amazon Linux 2 AMI → launches t2.micro EC2 |
| `create_s3_bucket.py` | Creates S3 bucket with unique name |
| `full_automation.py` | One command: EC2 + S3 + file upload + all config |
| `cleanup_aws_resources.py` | Terminates EC2 + empties + deletes S3 bucket |
| `terminate_all_instances.py` | Bulk terminate all running instances |

---

## Architecture

Your Machine (boto3)
│
├──▶ EC2 (ap-south-1) ──▶ Amazon Linux 2, t2.micro
│         └── Key Pair auth
│
└──▶ S3 Bucket
└── File upload / delete automation
---

## Prerequisites

```bash
pip install boto3
aws configure   # Add your Access Key + Secret Key
```

Required IAM permissions:
- `ec2:*`
- `s3:*`

---

## Quick Start

```bash
# Clone
git clone https://github.com/vedantgonbare/aws-python-project
cd aws-python-project

# Install deps
pip install -r requirements.txt

# Run full automation
python scripts/full_automation.py

# Cleanup everything (avoid AWS charges!)
python scripts/cleanup_aws_resources.py
```

---

## Project Structure
aws-python-project/
├── scripts/
│   ├── create_ec2_instance.py
│   ├── create_s3_bucket.py
│   ├── full_automation.py
│   ├── cleanup_aws_resources.py
│   └── terminate_all_instances.py
├── resources/
│   └── test.txt
├── .gitignore
├── requirements.txt
└── README.md
---

## Security Notes

- ⚠️ Never commit AWS credentials to Git
- `.pem` key files are in `.gitignore`
- Use IAM roles with minimum permissions
- Always run `cleanup_aws_resources.py` after testing (avoid billing!)

---

## Author

**Vedant Gonbare** — Python Backend Developer  
[GitHub](https://github.com/vedantgonbare) · [LinkedIn](inkedin.com/in/vedantgonbare/)