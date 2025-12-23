# 🏦 Bank Retirement MLOps System

Production-ready **Machine Learning & MLOps system** demonstrating how
a data science solution is packaged, tested, released, and deployed using
**GitHub + CircleCI**, **Docker**, **Gemfury**, and **Railway**.

This repository represents a production workflow where:
- the ML model is packaged as a **versioned Python dependency**
- the inference API is deployed as a **containerized service**
- **CircleCI orchestrates** testing, publishing, and deployment steps

---

## 🎯 What This Project Is

This project is a **practical MLOps reference implementation**.

It focuses on:
- packaging ML logic as installable Python packages
- automated training, testing, and static checks via `tox`
- versioned model distribution via a private registry (**Gemfury**) through CI/CD
- containerized inference services (FastAPI + Docker)
- CI/CD-driven cloud deployment to **Railway**

The emphasis is on **engineering quality, reproducibility, and automation** —
not on exploratory experimentation or model benchmarking.

---

## 🧠 End-to-End Architecture
```
GitHub (commits / tags)
↓
CircleCI (orchestration: test → publish → deploy)
├── Model release track (tags) → Gemfury (versioned wheel)
└── API deployment track (main/demo) → Docker build → Railway deploy
```


Both Gemfury publishing and Railway deployment are performed **inside CircleCI**.
They are separated into two tracks to support different release triggers.

---

## 📦 Machine Learning Package

The ML model is implemented as a **production-grade Python package** and is
fully decoupled from the API and deployment layers.

### Key characteristics
- clear separation of:
  - feature engineering
  - training
  - prediction
  - validation
- configuration via YAML files
- explicit versioning
- automated training and testing via `tox`
- static checks (formatting, typing)
- build artifacts produced as `.whl` files
- published to **Gemfury via CircleCI**

### What happens in CI for the model package
- `tox` runs training + tests (`train_pipeline.py` is executed before pytest)
- `tox -e publish_model` publishes the built artifact to Gemfury
- publication uses CI environment configuration (e.g., `GEMFURY_PUSH_URL`)

---

## 🚀 Inference API

The inference layer is implemented using **FastAPI** and consumes the released ML package
as a standard dependency.

### Characteristics
- REST API for model inference
- request/response validation using Pydantic
- health check endpoints
- no training logic inside the API
- ML package installed via `pip` using Gemfury as an extra index
  (configured via CI/env, e.g., `PIP_EXTRA_INDEX_URL`)

---

## 🔁 CI/CD Pipeline (CircleCI)

This repository uses **CircleCI** as the execution engine for automation.

### CI/CD responsibilities
- run automated tests for both the API and the ML package
- run static checks (formatting, typing)
- build versioned Python wheels
- publish ML packages to **Gemfury** (within CI)
- build Docker images for the API (within CI)
- deploy containers to **Railway** (within CI)

### Pipeline triggers (two tracks)

#### 1) Model release track (tags)
- **Trigger:** Git tags
- **Steps (CircleCI):** test/train → publish to Gemfury

#### 2) API deployment track (branches)
- **Trigger:** pushes to `main` or `demo`
- **Steps (CircleCI):** test → Docker build → deploy to Railway (`railway up`)

This structure is common in production: model releases are controlled by tags,
while the serving layer can be deployed independently.

---

## 🐳 Docker & Deployment (Railway)

The inference service is fully containerized.

Deployment flow (executed by CircleCI):
1. run API tests
2. build Docker image
3. deploy to Railway via Railway CLI (`railway up`)
4. Railway handles runtime, scaling, and exposure

---

## 📁 Repository Structure
```
├── .circleci/ # CircleCI pipeline configuration
├── deploying_with_containers/
│ ├── bank_retirement_api/ # FastAPI inference service
│ ├── model_package/ # ML package source code
│ └── Dockerfile # Container build configuration
├── .gitignore
└── README.md
```

---

## ⚙️ How the System Works

1. Changes are pushed to GitHub (commits or tags)
2. CircleCI runs the corresponding pipeline:
   - tags → train/test/publish model package to Gemfury
   - main/demo → test/build/deploy API container to Railway
3. The API serves predictions using the packaged model dependency

Each step is automated, reproducible, and traceable.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- Docker
- GitHub
- CircleCI
- Gemfury (private Python package registry)
- Railway (cloud deployment)
- Tox

---

## 📌 Project Status

✅ CI/CD-enabled (CircleCI)  
✅ Model publishing to Gemfury (tags)  
✅ API deployment to Railway (main/demo)  
🔧 Planned extensions:
- AWS deployment scenario (Docker-only)
- AWS deployment scenario (full CI/CD)
- monitoring and metrics
- authentication and access control
