from fastapi import FastAPI

from wallet.database import Base, engine
from wallet.api import router

tags_metadata = [
    {
        'name': 'users',
        'description': 'Registration and authorization'
    },
    {
        'name': 'operations',
        'description': 'Work with operations'
    },
    {
        'name': 'reports',
        'description': 'Exporting and importing reports'
    }
]

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Wallet',
    description='Personal expenses and income accounting service',
    openapi_tags=tags_metadata
)
app.include_router(router)
