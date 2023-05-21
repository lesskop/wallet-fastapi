from fastapi import HTTPException, status

validation_error = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={'WWW-authenticate': 'bearer'}
)

incorrect_credentials_error = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Incorrect username or password',
    headers={'WWW-authenticate': 'bearer'}
)
