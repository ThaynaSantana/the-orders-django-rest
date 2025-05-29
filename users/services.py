from .models import User


class UserService:
    def create_user(self, username: str, email: str):
        user = User.objects.create(username=username, email=email)
        return user
