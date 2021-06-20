1. 빈칸에 들어갈 코드는 무엇일까요?

```jsx
{% if blogs.has_previous%} #이전 페이지가 있을 경우
<a href="?page=1">처음</a>
<a href="?___________________">이전</a> 
{% endif %}
<span>{{blogs.number}}</span>
<span>of</span>
<span>{{blogs.paginator.num_pages}}</span>
________________ #다음페이지가 있을 경우
<a href="?page={{blogs.next_page_number}}">다음</a>
<a href="?page=__________________">마지막</a>
{% endif %>
```

- 정답

2. 다음과 코드를 이용하면 날짜 오름차순으로 글이 보이게 됩니다!

```jsx
blogs = Blog.objects.order_by('pub_date')
```

 그럼 내림차순으로 정렬하기 위해서는 빈칸에 어떤 코드가 들어가야 할까요?

```jsx
blogs = Blog.objects.order_by('_________')
```

- 정답

3. 다음 중 환경 변수에 관해 틀린 설명을 고르세요.

ㄱ. 시스템에 저장되어 있는 변수를 의미한다.

ㄴ. OS.environ.get("변수명",'기본값')으로 설정한다.

ㄷ. 환경에 차이를 둘 때 사용(테스트/프로덕션 구별 등)한다.

ㄹ. 유출 가능한 정보들을 다루기 위한 변수이다.

ㅁ. OS.environ에서 dict 형식으로 불러올 수 있다.

- 정답

4. 다음 코드를 실행하면 각각 어떤 결과가 나올까요?

```python
from django.core.paginator import Paginator
objects = ['멋쟁이', '사자처럼', '1학기', '마지막', '스터디', '아쉬워ㅠ']
p = Paginator(objects,3)
page1 = p.page(1)
page2 = p.page(2)
>> p.num_pages #1번문제
>> p.page_range #2번문제
>> page1.object_list #3번문제
>> page2.has_previous() #4번문제
```

- 정답

오늘 실습이 너무 빨리 끝난 느낌이 든다구요?! 아마 그것은 기분 탓..!

한 학기동안 강의에 과제에 스터디까지 하신다고 너무 고생 많으셨습니다ㅠㅠㅠ

남은 시간은 스터디조와 마지막인만큼 작별인사..?를 나눠주세요ㅎㅎ

꼭 5인이상 집합금지가 풀려서 스터디끼리라도 모일 수 있는 자리가 생겼으면 좋겠네요😢

아 이때까지 배운 장고 사실 왜 배웠는지 크게 와닿으시지 않을 것 같아 마지막으로 영상을 준비해봤습니다!

끝이라고 해놓고 뭘 자꾸 시키는 것 같아서 죄송하지만 이게 다 피가 되고 살이 되는 읍읍,,😵

이만 물러갑니당 총총

[https://youtu.be/PnhmeFakkXg](https://youtu.be/PnhmeFakkXg)

[무엇을 언제 써야할까? Node JS vs Django!](https://youtu.be/PnhmeFakkXg)
