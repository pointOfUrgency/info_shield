from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy

SECRET = "SECRET"

cookie_transport = CookieTransport()

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)