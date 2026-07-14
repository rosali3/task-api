import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from main import app, tasks


@pytest_asyncio.fixture
async def client():
    tasks.clear()           # очищаем хранилище перед каждым тестом. Без этой строки тесты начнут видеть задачи друг друга и ломаться при изменении порядка
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url="http://test"
    )  as client:
        yield client