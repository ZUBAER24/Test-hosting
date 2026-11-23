# ERROR X HOSTING — Render Python Deployment

A production-ready Python web hosting template branded for **ERROR X HOSTING**, pre-configured for zero-downtime deployment on **Render**.

## Included Files
- `main.py` — FastAPI + Uvicorn application with a live dashboard (`/`), JSON status API (`/api/status`), and health check (`/health`).
- `render.yaml` — Render Infrastructure-as-Code Blueprint for automatic setup.
- `requirements.txt` — Production server dependencies (`fastapi`, `uvicorn`, `gunicorn`).
- `.env.example` — Sample environment variables for local testing.
- `.gitignore` — Clean Git ignore rules.

## Quick Deploy to Render
1. Extract this ZIP and push the files to a new **GitHub** or **GitLab** repository.
2. Go to [Render Dashboard](https://dashboard.render.com/) -> click **New +** -> **Blueprint**.
3. Connect your repository and click **Apply**.
4. Render will automatically build and launch **ERROR X HOSTING**.

## Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
