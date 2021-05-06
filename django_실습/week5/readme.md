## 🔥 퀴즈로 내용을 익혀봅시다 ! 🔥

다같이 푸는 시간을 가진 후 다른 조원분께 정답을 말씀해달라고 부탁드리는 등 상호작용이 활발히 일어나면서 진행되면 좋겠습니다 !!!  +) 부분은 스터디 진행 시간을 고려하셔서 추가적으로 진행해주세요 ~

---

장고 프로젝트를 시작하려고 합니다. 빈 폴더를 만들었고, 음...  무엇부터 해줘야할까요?  순서대로 배열해주세요!  a) 장고 앱 만들기 b) 장고 프로젝트 시작하기 c)가상환경 설치 및 실행하기 d) 장고 설치하기

- 정답

    c - d - b - a 순서입니다 !  

    +) 각각 입력해줘야 할 커맨드는 어떻게 될까요 ?

working directory 안에서 mutsa.py라는 파일의 내용을 수정했습니다. 이 수정한 파일만을 staging area에 올리고 싶다면, 터미널에 어떤 커맨드를 써야할까요 ? 

- 정답

    ```bash
    git add mutsa.py
    ```

    "git add <파일/디렉토리 경로>" 는 해당 디렉토리의 변경 내용을 스테이징 영역으로 넘겨줍니다.

    이외에도,

    "git add . "는 '현재' 디렉토리 이하의 모든 변경 내용을 스테이징 영역으로,

    "git add -A "는 작업 디렉토리 상의 어디에 위치하든 모든 변경 내용을 스테이징 영역으로 넘겨주는 등 다양한 옵션들이 있습니다.

    +) 다른 자주 쓰이는 옵션에는 무엇이 있을까요?

 git 을 이용하여 작성한 프로젝트를 github에 올리려합니다. [ ]에 들어갈 커맨드를 작성해주세요 ! 

```bash
git [ ]  //git 명령어를 사용할 수 있는 상태로 만듦

git add .    //현재 디렉토리 이하의 모든 변경 내용을 status area에 올림

git commit [ ] "message" //status area에 존재하는 내용들을 변경 내용을 설명하는 "message"와 함께 로컬 저장소에 저장

git [ ] add origin "https://github.com~" //원격 저장소의 이름을 origin으로, 주소를 "https:~"로 추가해준다.

git [        ] //origin이라는 이름으로 등록된 원격 저장소에 master라는 브랜치를 반영한다.

```

- 정답

 장고 프로젝트를 위해 현재 여러분은 app까지 만들었습니다.  그 후, 

1. settings.py ⇒[   ]

2. templates ⇒ [   ]

3. views.py ⇒ [  ]

4. urls.py ⇒ [   ]

의 단계를 거치려 하는데, 각각 [ ]에 들어갈 설명은 무엇일까요 ?

a : views.py에서 처리된 데이터를 받아 사용자에게 화면을 보여줌
b : project에게 app의 존재 알리기
c : 요청에 맞는 함수를 views.py에서 찾아 요청 전달
d : 데이터를 처리하는 함수 작성

- 정답

urls.py의 코드 중

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello.views.home, name='home'),
]
이 있다면, path 뒤의  '  ' / hello.views.home/ name='home' 이 세가지가 각각 의미하는 바는 무엇일까요?

- 정답

---

**깃에 대해 더 알고싶습니다...
: 도움이 될(수도 있는) 참고 사이트 

웹사이트 

 [https://backlog.com/git-tutorial/kr/stepup/stepup1_1.html](https://backlog.com/git-tutorial/kr/stepup/stepup1_1.html)
 [https://learngitbranching.js.org/?locale=ko](https://learngitbranching.js.org/?locale=ko)

강의

[https://www.youtube.com/watch?v=FXDjmsiv8fI&t=468s](https://www.youtube.com/watch?v=FXDjmsiv8fI&t=468s)
