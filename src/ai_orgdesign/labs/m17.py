"""Bounded asynchronous work plus local lease ownership and expiration."""

import asyncio
import tempfile
from pathlib import Path

from ai_orgdesign.business import CaseStore


async def bounded_work(items, limit=2):
    if type(limit) is not int or limit < 1:
        raise ValueError("Positive integer concurrency required")
    semaphore = asyncio.Semaphore(limit)
    active = 0
    peak = 0

    async def work(item):
        nonlocal active, peak
        async with semaphore:
            active += 1
            peak = max(peak, active)
            try:
                await asyncio.sleep(0.001)
                return {"id": item, "status": "prepared"}
            finally:
                active -= 1

    results = await asyncio.gather(*(work(item) for item in items))
    return {"results": results, "peak": peak, "limit": limit}


def demo():
    with tempfile.TemporaryDirectory() as folder:
        store = CaseStore(Path(folder) / "jobs.db")
        store.enqueue("job-1")
        first = store.claim("job-1", "worker-a", now=0, seconds=10)
        before_expiry = store.claim("job-1", "worker-b", now=5)
        reclaimed = store.claim("job-1", "worker-b", now=11)
        store.finish("job-1", "worker-b", now=12)
        return {
            "first": first,
            "second_before_expiry": before_expiry,
            "reclaimed": reclaimed,
            "arrival_per_hour": 30,
            "review_capacity_per_hour": 20,
            "backlog_growth_per_hour": 10,
        }
