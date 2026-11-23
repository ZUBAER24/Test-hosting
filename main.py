import os
import time
from datetime import datetime, timezone
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

START_TIME = time.time()

app = FastAPI(
    title="ERROR X HOSTING",
    description="High-Performance Python Cloud Hosting Engine on Render",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_uptime() -> str:
    elapsed = int(time.time() - START_TIME)
    days, rem = divmod(elapsed, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"


@app.get("/", response_class=HTMLResponse)
async def home():
    env = os.getenv("ENV", "production").upper()
    uptime = get_uptime()
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ERROR X HOSTING — Python Cloud Node</title>
        <style>
            :root {{
                --bg: #090b10;
                --card: #111520;
                --accent: #ff2a5f;
                --accent-glow: rgba(255, 42, 95, 0.35);
                --text: #f3f4f6;
                --muted: #9ca3af;
                --green: #10b981;
            }}
            * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }}
            body {{
                background: radial-gradient(circle at top, #181c2e 0%, var(--bg) 70%);
                color: var(--text);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }}
            .container {{
                max-width: 680px;
                width: 100%;
                background: var(--card);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 16px;
                padding: 40px;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 30px var(--accent-glow);
                text-align: center;
            }}
            .badge {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: rgba(16, 185, 129, 0.12);
                color: var(--green);
                border: 1px solid rgba(16, 185, 129, 0.3);
                padding: 6px 14px;
                border-radius: 999px;
                font-size: 0.85rem;
                font-weight: 600;
                margin-bottom: 20px;
            }}
            .dot {{
                width: 8px;
                height: 8px;
                background: var(--green);
                border-radius: 50%;
                box-shadow: 0 0 8px var(--green);
            }}
            h1 {{
                font-size: 2.4rem;
                font-weight: 800;
                letter-spacing: 2px;
                margin-bottom: 10px;
                background: linear-gradient(90deg, #ffffff, var(--accent));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            p.subtitle {{
                color: var(--muted);
                font-size: 1.05rem;
                margin-bottom: 30px;
            }}
            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
                gap: 16px;
                margin-bottom: 30px;
            }}
            .stat {{
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.06);
                border-radius: 12px;
                padding: 16px;
            }}
            .stat-label {{
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 1px;
                color: var(--muted);
                margin-bottom: 6px;
            }}
            .stat-value {{
                font-size: 1.1rem;
                font-weight: 700;
                color: #fff;
            }}
            .endpoints {{
                text-align: left;
                background: #0b0e16;
                border-radius: 10px;
                padding: 18px;
                border: 1px solid rgba(255, 255, 255, 0.05);
                font-family: monospace;
                font-size: 0.9rem;
            }}
            .endpoints div {{ margin: 6px 0; color: #d1d5db; }}
            .method {{ color: var(--accent); font-weight: bold; }}
            a {{ color: #60a5fa; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="badge"><span class="dot"></span> SYSTEM ONLINE & OPERATIONAL</div>
            <h1>ERROR X HOSTING</h1>
            <p class="subtitle">High-Speed Python Cloud Deployment Powered by Render</p>
            <div class="grid">
                <div class="stat">
                    <div class="stat-label">Environment</div>
                    <div class="stat-value">{env}</div>
                </div>
                <div class="stat">
                    <div class="stat-label">Server Uptime</div>
                    <div class="stat-value">{uptime}</div>
                </div>
                <div class="stat">
                    <div class="stat-label">Engine</div>
                    <div class="stat-value">FastAPI + Uvicorn</div>
                </div>
            </div>
            <div class="endpoints">
                <div><span class="method">GET</span> <a href="/api/status">/api/status</a> — JSON Server Telemetry</div>
                <div><span class="method">GET</span> <a href="/health">/health</a> — Render Zero-Downtime Health Check</div>
                <div><span class="method">GET</span> <a href="/docs">/docs</a> — Interactive Swagger API Docs</div>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/api/status")
async def api_status(request: Request):
    return JSONResponse(
        {
            "hosting": "ERROR X HOSTING",
            "status": "online",
            "environment": os.getenv("ENV", "production"),
            "uptime": get_uptime(),
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "client_ip": request.client.host if request.client else "unknown",
        }
    )


@app.get("/health")
async def health_check():
    return {"hosting": "ERROR X HOSTING", "status": "healthy"}
