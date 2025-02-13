# Automation Agent

This is an API-powered automation agent for DataWorks Solutions.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `uvicorn src.main:app --reload`
3. Use API endpoints:
   - `POST /run?task=<task description>` → Execute task
   - `GET /read?path=<file path>` → Read file content

## Docker

Build and run:

docker build -t automation-agent . docker run -p 8000:8000 -e AIPROXY_TOKEN=your_token automation-agent