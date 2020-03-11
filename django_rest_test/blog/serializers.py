from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'reg_date')


'''
Serializer는 REST 로 데이터를 주고 받을 때, 모델을 어떻게 주고 받을 것인가를 정의하기 위한 클래스 입니다.
저희는 데이터 모델 그 자체를 주고 받을 것 이니, 기본적으로 모델 전체를 자동으로 변환해주는 ModelSerializer 에 힘을 빌릴겁니다.

rest_framework.serializers 에 포함되어 있는 ModelSerializer 는 Meta 클래스를 요구합니다.
클래스 안에 Meta 클래스를 정의하는 것으로, ModelSerializer가 자신이 필요한 정보들을 파악하여 자동으로 Serialize 를 수행하게 될 것입니다.
ModelSerializer는 다양한 메타 데이터를 포함할 수 있지만, model 데이터만을 넘겨줘도 저희가 쓰기에는 충분 합니다.
'''