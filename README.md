# Production-grade App Deployment Platform 
### (Mini Heroku on AWS)

A production-inspired deployment platform built on AWS — push code to GitHub and it automatically builds, containerizes, and deploys your app with auto-scaling and monitoring.

---

## Architecture

\`\`\`
git push → GitHub Actions
                ↓
         Docker Build
                ↓
         Push to ECR
                ↓
         ECS Fargate Deploy
                ↓
         ALB (Load Balancer)
                ↓
         Auto Scaling + CloudWatch
\`\`\`

---

## Tech Stack

| Layer | Technology |
|---|---|
| App | Python + FastAPI |
| Container | Docker |
| Registry | AWS ECR |
| Orchestration | AWS ECS Fargate |
| Load Balancer | AWS ALB |
| Infrastructure | Terraform |
| CI/CD | GitHub Actions |
| Monitoring | CloudWatch + SNS |

---

## Features (Progressive Build)

- [x] FastAPI app containerized with Docker
- [x] ECR repository created via Terraform
- [x] ECS cluster created via Terraform
- [x] Docker image pushed to ECR
- [ ] ECS Task Definition + Service
- [ ] ALB Load Balancer
- [ ] Auto Scaling policy
- [ ] GitHub Actions CI/CD pipeline
- [ ] CloudWatch monitoring + SNS alerts
- [ ] Blue-green deployment

---

## System Design Concepts Covered

- **Containerization** — Docker for consistent deployments
- **Infrastructure as Code** — Terraform for reproducible infra
- **Container Orchestration** — ECS Fargate, no server management
- **Load Balancing** — ALB for traffic distribution
- **Auto Scaling** — Scale based on CPU/memory
- **Zero-downtime Deploy** — Blue-green deployment strategy
- **Observability** — Metrics, logs, alerts

---

## Local Setup

\`\`\`bash
# Clone repo
git clone https://github.com/Ashwin52/aws-deployment-platform.git
cd aws-deployment-platform

# Build Docker image
docker build -t deployment-platform-app .

# Run locally
docker run -p 8000:8000 deployment-platform-app

# Test
curl http://localhost:8000/health
\`\`\`

---

## Infrastructure Setup

\`\`\`bash
# Initialize Terraform
cd terraform
terraform init

# Preview changes
terraform plan

# Apply
terraform apply
\`\`\`

---

## Author

**Ashwin** — ECE Student | Aspiring Cloud & DevOps Engineer

[![GitHub](https://img.shields.io/badge/GitHub-Ashwin52-black)](https://github.com/Ashwin52)
