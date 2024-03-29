import uvicorn

from wallet.settings import settings

uvicorn.run(
    'wallet.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)
