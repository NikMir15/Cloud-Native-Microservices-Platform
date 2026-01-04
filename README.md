# Cloud-Native Microservices Platform (Docker + Auth + API Gateway)

## Overview
This project is a cloud-native microservices platform built with a clean, scalable architecture.
It demonstrates real-world microservice patterns: independent services, container orchestration, secure JWT-based authentication, and a single API Gateway entry point.

The platform currently includes:
- **Auth Service** (user registration + login, JWT token issuance)
- **Product Service** (product catalogue)
- **Order Service** (creates orders by calling Product Service, protected by JWT)
- **API Gateway (Nginx)** (single entry point for routing traffic)

---

## Tech Stack
- **Backend:** FastAPI (Python)
- **Auth:** JWT (python-jose)
- **API Gateway:** Nginx
- **Containerisation:** Docker, Docker Compose
- **Local Tooling:** VS Code, PowerShell

---

## Architecture
The system follows a microservices architecture where each service runs independently in its own container.
All external traffic goes through the **API Gateway**, which routes requests to internal services.

**High-level flow**
1. Client hits **Gateway** on port `8080`
2. Gateway forwards requests to the appropriate service container
3. **Order Service** calls **Product Service** internally over Docker network
4. **Order Service** validates JWT for protected endpoints

### Services
- **gateway** (Nginx): Routes `/auth/*`, `/products/*`, `/orders/*`
- **auth-service** (FastAPI): `/register`, `/login`, returns JWT token
- **product-service** (FastAPI): `/products`
- **order-service** (FastAPI): `/orders` (JWT protected), calls product-service

---

## Service Ports (Docker)
- Gateway: `8080 -> 80`
- Auth Service: `8001`
- Product Service: `8002`
- Order Service: `8003`

---

## How to Run (Docker)
### Prerequisites
- Docker Desktop installed and running

### Start the platform
From the project root:
```bash
docker compose up -d --build
