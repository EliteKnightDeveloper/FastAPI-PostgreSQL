from fastapi import APIRouter

from apis.v1 import controller_user, controller_blog, controller_login

api_router = APIRouter()
api_router.include_router(controller_user.router, prefix="", tags=["users"])
api_router.include_router(controller_blog.router, prefix="", tags=["blogs"])
api_router.include_router(controller_login.router, prefix="", tags=["login"])
