# VetRehabAI

An AI-powered physical therapy monitoring platform for veterans.

## Overview

VetRehabAI helps clinicians track veteran patients' rehabilitation progress using
computer vision, pose estimation, and AI-driven analytics.

## Project Structure

```
VetRehabAI/
├── frontend/          # React/Next.js UI for patients and clinicians
├── backend/           # REST API server (FastAPI or Node.js)
├── ai/                # ML models — pose estimation, pain detection, progress analysis
├── database/          # Schemas, migrations, seed data
├── shared/            # Shared types and constants across services
├── infrastructure/    # Docker, CI/CD, Nginx configs
└── docs/              # API reference, architecture diagrams, guides
```

## Getting Started

```bash
cp .env.example .env
docker-compose up
```

## Modules

| Module | Description |
|--------|-------------|
| Pose Estimation | Real-time joint angle tracking during exercises |
| Progress Analysis | Longitudinal recovery trend modeling |
| Pain Detection | Facial / motion cue analysis for pain indicators |
| Clinician Dashboard | Session review, alerts, patient management |
| Patient Portal | Exercise guidance, progress visualization |
