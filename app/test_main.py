import pytest


@pytest.mark.parametrize(
    "payload",
    [
        {"title": ""},
        {"description": "no title"},
        {"title": "x" * 300},
        {},
    ],
)
async def test_create_task_invalid(client, payload):
    response = await client.post("/tasks", json=payload)
    assert response.status_code == 422