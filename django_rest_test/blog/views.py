from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from blog.models import Post
from blog.serializers import PostSerializer


# 응답에 여러가지 헤더가 포함되어져야 하는데, 이를 쉽고 간편하게 처리해주는 HttpResponse를 장고에서 제공해주고 있음
# 따라서 우리는 간단하게 return HttpResponse(데이터) 모양으로 쉽게 응답을 보낼 수 있음
def blog_page(request):
    post_list = Post.objects.all()

    return HttpResponse('Hello ' + post_list[0].title)


class blog_api(GenericAPIView, mixins.ListModelMixin): # GenericAPIView는 as_view() 라는 함수를 가지고 있는데, 이 함수는 기본적인 REST Framework 웹 페이지를 하나 출력
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


'''
REST Framework 를 사용하기 위해서는,
기본적으로 questset 이라는 멤버와 serializer_class 라는 멤버(또는 get_serializer_class() 라는 함수)를 제공해줘야 합니다.
이를 통해서 GenericAPIView는 기본적인 REST 기능을 수행할 수 있게 됩니다.

먼저 queryset은 어떠한 모델을 보여줄것인가? 를 정의 합니다.
Post 데이터들을 보여줄 테니, 전체 Post 데이터를 반환 하게 합니다.

그 뒤, serializer_class 는 PostSerializer 를 설정해 둡니다.

이제 GET 요청에 대한 처리를 구현할 차례 입니다.
기본적으로 REST Framework는 GET / POST / PATCH / DELETE 등의 요청에 대한 기본 처리를 제공해 줍니다.
GenericAPIView 에서 각각 get / post / delete 등의 이름으로 정의가 되어 있습니다.
직접 처리하는 것도 방법이지만, GenericAPIView는 다른 Mixin 클래스와의 조합으로 쉽고 빠르게 구현하는 방법들을 제공 합니다.
rest_framework.mixins 를 포함하고, ListModelMixins 라는 클래스를 다중 상속하여 해당 기능을 구현해 봅시다.

다중 상속을 통해, GenericAPIView의 기능과 ListModelMixin의 기능을 같이 가져왔습니다.
ListModelMixin은 GeneicAPIView에 queryset과 serializer_class를 기반으로 하여 데이터 List를 만들어주는 기능을 합니다.

먼저 get 을 정의해 봅시다.
기본적으로 REST Framework에서는 request, *args, **kwargs를 반드시 포함해서 처리하게 되어 있습니다.
기본적으로 온 요청에 대한 Parsing 작업을 하여 Request를 생성하고, 그 외에 여러 데이터는 *args와 **kwargs에 포함하여 오는 형태 입니다.

ListModelMixin 클래스를 상속 받으면 list 라는 함수가 상속받아집니다. get 메소드에서 이를 호출하는 것으로, 기본적으로 목록 조회 기능을 요청할 수 있습니다.
'''