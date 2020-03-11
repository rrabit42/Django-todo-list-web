from django.db import models

'''
간단한 블로그 만들기

블로그는 다양한 포스팅(Post) 단위로 구분되며,
하나의 포스팅에는 제목 / 내용 / 작성시간 등으로 구분

즉, '제목' / '내용' / '작성시간' 이 이 데이터의 기본
'''


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=2048)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)

