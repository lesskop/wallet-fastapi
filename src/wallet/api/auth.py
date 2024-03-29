from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from wallet.models.auth import UserCreate, Token, User
from wallet.services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth',
)


@router.post('/sign-up', response_model=Token, tags=['users'])
def sign_up(user_data: UserCreate, service: AuthService = Depends()):
    return service.register_new_user(user_data)


@router.post('/sign-in', tags=['users'])
def sign_in(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends()
):
    return service.authenticate_user(form_data.username, form_data.password)


@router.get('/user', response_model=User, tags=['users'])
def get_user(
        user: User = Depends(get_current_user),
):
    return user
