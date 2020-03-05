from django.db import models


class ProjectCode(models.Model):
    pcode = models.CharField(db_column='PCODE', primary_key=True, max_length=4)  #Field name made lowercase.
    pname = models.CharField(db_column='PNAME', max_length=100)  # Field name madelowercase.

    class Meta:
        managed = False
        db_table = 'project_code'


class TodoList(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made low ercase.
    pcode = models.CharField(max_length=4)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    is_complete = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    # 저장 버튼을 누르면 바로 저장을 하지 않고, todo_save 함수를 호출하면 그제서야 저장
    # 이렇게 하는 이유는 여러가지가 있지만, save하기 전에 default로 db 값을 넣어주도록 하기 위해서 이렇게 함
    # 예를 들어서 is_complete는 1이 아닌 0의 값을 가져야 하기 때문에 0으로 넣어주는 등의 작업!
    def todo_save(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'todo_list'


'''
데이터 베이스를 적용시키기 위해서 model이 적용되도록 함
makemigrations는 models.py에 적용된 내용을 파일로 생성(일종의 초안 작업)
migrate는 그 적용 사항을 실제 db에 적용 시켜줌

근데 나는 이미 db를 만들어놨으니 코드를 직접 짤 필요가 없음
이미 만들어진 db를 어떻게 models.py에 옮기느냐?? (django는 다 지원해줍니다)
python manage.py inspectdb

코드가 쭉 나오는데 이 내용을 복붙해서 models 파일에 넣어주면 됨.
그리고 makemigrations, migrate
'''