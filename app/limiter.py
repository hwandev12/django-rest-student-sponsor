from django_limits.limiter import Limiter
from django.contrib.auth import get_user_model
from .models import Sponsor
from django.db.models import Q

User = get_user_model()

class MyLimiter(Limiter):
    rules = {
        User: [
            {
                'limit': 3,
                'message': 'Only 20 active users are allowed',
                'filterset': Q(is_active=True)
            },
            {
                'limit': 10,
                'message': 'Only 10 staff memebers are allowed',
                'filterset': Q(is_staff=True)
            }
        ]
    }