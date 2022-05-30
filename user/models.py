#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractUser: 장고의 기본 모델을 임포트
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):  # 이것을 장고의 기본모델로 사용하겠다는 의미(settings.py에 정의해주어야함)
    class Meta:
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
