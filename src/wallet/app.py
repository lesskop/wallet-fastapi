from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .api import router

app = FastAPI()
app.include_router(router)


@app.get('/')
def root():
    return RedirectResponse(url='/docs')
