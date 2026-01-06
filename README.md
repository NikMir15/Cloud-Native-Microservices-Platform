# Cloud-Native Microservices Platform (AWS)

## Overview
This project demonstrates a **cloud-native microservices architecture** deployed on **AWS** using modern DevOps and infrastructure best practices.  
It focuses on **scalability, security, container orchestration, and production-grade networking** rather than only application code.

The platform is designed to be extended with multiple backend services behind a single API gateway and load balancer.

---

## Architecture
High-level flow:

Client
|
v
Application Load Balancer (ALB)
|
v
ECS Cluster (Fargate)
|
+--> API Gateway / Nginx
|
+--> Auth Service
|
+--> Other Microservices (future)


### Key Design Decisions
- **ALB** handles traffic distribution and HTTPS termination  
- **ECS Fargate** runs containers without managing servers  
- **Task definitions** separate infrastructure from application code  
- **Route 53** manages DNS for subdomains (keeps main portfolio safe)  
- **ACM** provides SSL certificates

---

## Tech Stack
- AWS ECS (Fargate)
- Application Load Balancer (ALB)
- Amazon ECR
- AWS Route 53
- AWS Certificate Manager (ACM)
- Docker
- Nginx (Gateway)
- Git & GitHub

---

## Repository Structure
cloud-native-microservices-platform/
│
├── gateway/
│ ├── Dockerfile.ecs
│ └── nginx.ecs.conf
│
├── ecs-trust.json
├── taskdef.json
├── .gitignore
└── README.md


---

## How It Works
1. Traffic enters through an **Application Load Balancer**
2. ALB forwards requests to ECS services
3. Nginx acts as a **gateway** to route requests to internal services
4. Services run as containers and can scale independently
5. DNS and SSL are handled at the infrastructure layer

---

## Key Features
- Containerized microservices deployment
- Load-balanced architecture using ALB
- HTTPS using ACM certificates
- DNS routing using Route 53
- Gateway routing (Nginx) for microservice endpoints
- Cloud-ready design for autoscaling & CI/CD

---

## Future Improvements
- ECS Service Auto Scaling policies
- CI/CD pipeline (GitHub Actions)
- Observability dashboards (CloudWatch)
- Auth hardening (JWT verification between services)
- Rate limiting / WAF integration

---

## Notes
This project is intentionally **infrastructure-focused** to demonstrate real-world cloud engineering skills.
