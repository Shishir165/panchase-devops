# 🌿 Panchase Eco Tourism — DevOps Capstone Project

> A full-stack DevOps project built around a real eco-tourism website for Panchase, Pokhara, Nepal.  
> Live at **[panchase.com](https://panchase.com)**

---

## 🏗️ Architecture Overview

```
                         ┌─────────────────────────────────┐
                         │         panchase.com             │
                         │   (Route53 + ACM SSL + CloudFront)│
                         └────────────┬────────────────────┘
                                      │
                         ┌────────────▼────────────────────┐
                         │        AWS S3 Bucket             │
                         │    (Static Website Hosting)      │
                         └────────────┬────────────────────┘
                                      │
              ┌───────────────────────┼────────────────────────┐
              │                       │                        │
  ┌───────────▼──────────┐ ┌─────────▼──────────┐ ┌──────────▼─────────┐
  │   GitHub Actions      │ │   API Gateway       │ │   Kubernetes       │
  │   CI/CD Pipeline      │ │   + Lambda + SES    │ │   (Minikube)       │
  └───────────────────────┘ └────────────────────┘ └────────────────────┘
```

---

## 🛠️ Tech Stack

| Category | Tool | Purpose |
|---|---|---|
| **IaC** | Terraform | Provision all AWS infrastructure |
| **Containerization** | Docker | Package website into container |
| **Orchestration** | Kubernetes (Minikube) | Run containers locally |
| **Package Manager** | Helm | Deploy K8s resources with one command |
| **CI/CD** | GitHub Actions | Auto-deploy on every git push |
| **Hosting** | AWS S3 + CloudFront | Static website hosting + CDN |
| **DNS** | AWS Route53 | Domain management |
| **SSL** | AWS ACM | HTTPS certificate |
| **Serverless** | AWS Lambda | Booking form backend |
| **API** | AWS API Gateway | REST API for Lambda |
| **Email** | AWS SES | Booking notification emails |
| **Monitoring** | Prometheus + Grafana | Cluster metrics & dashboards |
| **Analytics** | Google Analytics | Website visitor tracking |
| **Payments** | Stripe (test) + Wise | International payment integration |

---

## 📁 Project Structure

```
panchase-devops/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline
├── terraform/
│   ├── main.tf                 # S3, CloudFront, ACM, Route53
│   ├── variables.tf            # Input variables
│   ├── outputs.tf              # Output values
│   └── backend.tf              # Remote state config
├── kubernetes/
│   ├── deployment.yaml         # K8s Deployment (2 replicas)
│   ├── service.yaml            # NodePort Service
│   └── ingress.yaml            # Nginx Ingress (panchase.local)
├── charts/
│   └── panchase/               # Helm chart
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
├── lambda/
│   ├── booking.py              # Booking form handler → SES
│   ├── payment.py              # Stripe payment → checkout session
│   └── trust-policy.json       # IAM role policy
├── monitoring/                 # Prometheus + Grafana configs
├── website/
│   └── static/
│       ├── index.html          # Main website
│       └── Panchase-eco-tourism/ # Images & assets
└── Dockerfile                  # nginx:alpine container
```

---

## 🚀 CI/CD Pipeline

Every `git push` to `main` triggers:

```
git push
    ↓
GitHub Actions
    ↓
aws s3 sync website/static/ → s3://panchase.com
    ↓
CloudFront cache invalidation
    ↓
panchase.com updated ✅
```

---

## ☸️ Kubernetes Setup (Local)

```bash
# Start cluster
minikube start

# Load Docker image
minikube image load panchase-website:latest

# Deploy with Helm (one command!)
helm install panchase charts/panchase

# Access via ingress
kubectl port-forward -n ingress-nginx service/ingress-nginx-controller 8080:80
# → http://panchase.local:8080
```

---

## 📊 Monitoring Stack

```bash
# Install Prometheus + Grafana
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace

# Access Grafana
kubectl --namespace monitoring port-forward service/monitoring-grafana 3000:80
# → http://localhost:3000 (admin / see secret)
```

---

## 📧 Serverless Booking System

```
User fills booking form
    ↓
API Gateway (POST /booking)
    ↓
Lambda (booking.py)
    ↓
AWS SES → email notification
    ↓
ayudh165@gmail.com ✅
```

**API Endpoint:**
```
POST https://gc32u6iwmk.execute-api.us-east-1.amazonaws.com/prod/booking
```

**Payload:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+1234567890",
  "date": "2026-05-01",
  "guests": "2",
  "message": "Looking forward to the trek!"
}
```

---

## 💳 Payment Integration

```
User clicks Book button
    ↓
API Gateway (POST /payment)
    ↓
Lambda (payment.py)
    ↓
Stripe Checkout Session
    ↓
Stripe hosted payment page
    ↓
Redirect back to panchase.com ✅
```

> **Note:** Stripe is configured in test mode. Nepal is not yet supported by Stripe for merchant accounts — Wise payment links are used for live international payments.

---

## 🌍 Infrastructure (Terraform)

```bash
cd terraform

# Initialize
terraform init

# Preview changes
terraform plan

# Apply
terraform apply

# Resources created:
# ✅ S3 bucket (panchase.com)
# ✅ CloudFront distribution
# ✅ ACM SSL certificate
# ✅ Route53 hosted zone
```

---

## 🐳 Docker

```bash
# Build
docker build -t panchase-website:latest .

# Run locally
docker run -p 8080:80 panchase-website:latest

# Access → http://localhost:8080
```

---

## ⚙️ Environment Variables

| Variable | Service | Description |
|---|---|---|
| `STRIPE_SECRET_KEY` | Lambda | Stripe API secret key |
| `AWS_REGION` | Terraform | AWS region (us-east-1) |
| `DOMAIN_NAME` | Terraform | panchase.com |

---

## 📋 Prerequisites

- AWS CLI configured (`aws configure`)
- Terraform >= 1.0
- Docker
- kubectl
- Minikube
- Helm >= 3.0
- Node.js (for local dev)

---

## 🗺️ Roadmap

- [x] Terraform Infrastructure
- [x] Docker containerization
- [x] GitHub Actions CI/CD
- [x] Kubernetes local deployment
- [x] Helm chart
- [x] Prometheus + Grafana monitoring
- [x] Lambda booking system
- [x] API Gateway
- [x] AWS SES email notifications
- [x] Stripe payment integration
- [x] Google Analytics
- [ ] Khalti payment (Nepal locals)
- [ ] AWS EKS (production Kubernetes)
- [ ] Terraform remote state
- [ ] Custom domain for API Gateway

---

## 👨‍💻 Author

**Shishir Pariyar**  
GitHub: [@Shishir165](https://github.com/Shishir165)  
Project: [panchase.com](https://panchase.com)

---

## 📄 License

This project is for educational and portfolio purposes.  
Website content © Panchase Eco Tourism.