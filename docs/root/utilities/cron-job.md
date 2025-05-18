The **cron job utility** demonstrates how to use `fastapi-utils` to run recurring background tasks in a FastAPI application.

!!! dependencies
    ```bash
    pip install typing-inspect fastapi-utils
    ```

## ⏰ Cron Job Setup with Lifespan

```python title="server.py"
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from contextlib import asynccontextmanager

# 1-minute recurring task
@repeat_every(seconds=60)
async def cron_job():
    print("CronJob....")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Optional: Run once at startup
    await cron_job()
    yield

# Attach lifespan to FastAPI app
app = FastAPI(lifespan=lifespan)
```

## 🛠️ How It Works

* `@repeat_every(...)`: Decorator to schedule repeated execution.
* `lifespan`: Hook that initializes your cron job when the FastAPI app starts.
* Non-blocking execution allows background scheduling without interfering with request handling.

## ✅ When to Use

* Email reminders every hour
* Database cleanup tasks
* Scheduled API polling
* Metrics/report aggregation jobs