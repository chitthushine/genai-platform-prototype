# GenAI Platform Prototype

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![React Version](https://img.shields.io/badge/react-18%2B-blue)](https://reactjs.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A full-stack platform prototype for deploying and managing Generative AI models, featuring:

- 🚀 FastAPI backend with model serving
- ⚛️ React frontend with intuitive UI
- 🐳 Dockerized environment
- 🔒 API key authentication
- 📊 Prometheus monitoring

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)

## Features
- **Model Serving**
  - GPT-2 text generation (just a prototype)
  - BART summarization  (just a prototype)
- **Monitoring**
  - Prometheus endpoint
- **Security**
  - API key authentication
  - CORS protection
- **Developer Experience**
  - Hot-reloading for React & FastAPI
  - Pre-commit hooks with Black/Flake8

## Tech Stack
**Backend**
- Python 3.9
- FastAPI
- Pip (dependency management)

**Frontend**
- React 22
- React Router 6
- Axios (HTTP client)

**Infrastructure**
- Docker
- Docker Compose
- Prometheus/Grafana

## Installation

### Prerequisites
- Docker 23+

```bash
# Clone repository
git clone https://github.com/chitthushine/genai-platform-prototype.git
cd genai-platform-prototype

# 1. Docker setup
cd genai-platform-prototype
docker-compose build
docker-compoe up -d
