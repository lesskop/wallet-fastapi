from fastapi import FastAPI

from .api import router

tags_metadata = [
    {
        'name': 'users',
        'description': 'Registration and authorization'
    },
    {
        'name': 'operations',
        'description': 'Work with operations'
    },
]

app = FastAPI(
    title='Wallet',
    description='Personal expenses and income accounting service',
    openapi_tags=tags_metadata
)
app.include_router(router)
