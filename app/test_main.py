from httpx import ASGITransport, AsyncClient

from main import app


async def test_health():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

async def test_create_task_ok():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            "/tasks",
            json={
                "title": "buy milk",
                "description": "2 liters",
            },
        )

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "buy milk"
    assert body["done"] is False
    assert isinstance(body["id"], int)


async def test_create_task_missing_title():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
                    "/tasks",
                    json={"description": "no title"}
    )
    assert response.status_code == 422


async def test_create_task_empty_title():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
                    "/tasks",
                    json={"title": ""}
    )
    assert response.status_code == 422