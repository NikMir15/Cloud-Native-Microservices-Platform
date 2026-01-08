# Cloud-Native Microservices Platform

Cloud-native microservices platform using **FastAPI**, **JWT authentication**, **Docker Compose**, and an **Nginx API Gateway** — with an AWS-ready path using **ECS Fargate + ALB + Route 53 + ACM**.

## Overview
This project demonstrates how to design and run a microservices platform with:
- A single entry point (API Gateway)
- Independently deployable services
- Container-first local development (Docker Compose)
- Production-style AWS deployment architecture (ECS/ALB/HTTPS/DNS)

## Tech Stack
- Backend: FastAPI (Python), JWT Auth
- Gateway: Nginx (reverse proxy / routing)
- Containers: Docker, Docker Compose
- CI/CD: GitHub Actions (workflows in `.github/workflows`)
- AWS (deployment-ready): ECS Fargate, ALB, ECR, Route 53, ACM

## Architecture
High-level flow:

Client  
→ (Local) Nginx Gateway → Services (FastAPI)  
→ (AWS) ALB (HTTPS) → ECS (Fargate) → Nginx Gateway → Services

Key design decisions:
- Gateway handles routing to internal services
- Services are isolated and can scale independently
- Infra concerns (DNS/SSL/LB) are handled at the platform layer

## Repository Structure
- `frontend/` — UI
- `gateway/` — Nginx gateway config + Dockerfile
- `services/` — backend microservices (FastAPI)
- `docker-compose.yml` — local orchestration
- `ecs/`, `taskdef.json`, `ecs-trust.json` — ECS deployment assets
- `.github/workflows/` — CI/CD workflows

## How to Run Locally (Docker Compose)
### Prerequisites
- Docker + Docker Compose installed

### Run
```bash
git clone https://github.com/NikMir15/Cloud-Native-Microservices-Platform.git
cd Cloud-Native-Microservices-Platform
docker compose up --build
