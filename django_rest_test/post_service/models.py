from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    # 게시물의 고유한 인덱스는 models.Model에 기본으로 포함되는 pk를 이용
    title = models.CharField(max_length=1024)
    body = models.CharField(max_length=4096)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Django의 기본 User
    regdate = models.DateTimeField(auto_created=True, auto_now_add=True)

