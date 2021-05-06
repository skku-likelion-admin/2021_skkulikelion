# Django_Week5 #
## 🔥 퀴즈로 내용을 익혀봅시다 ! 🔥

다같이 푸는 시간을 가진 후 다른 조원분께 정답을 말씀해달라고 부탁드리는 등 상호작용이 활발히 일어나면서 진행되면 좋겠습니다 !!!  +) 부분은 스터디 진행 시간을 고려하셔서 추가적으로 진행해주세요 ~

---

### 1. 장고 프로젝트를 시작하려고 합니다. 빈 폴더를 만들었고, 무엇부터 해줘야할까요?  순서대로 배열해주세요!  
### a) 장고 앱 만들기 b) 장고 프로젝트 시작하기 c)가상환경 설치 및 실행하기 d) 장고 설치하기 ###

- 정답

    c - d - b - a 순서입니다 !  

    +) 각각 입력해줘야 할 커맨드는 어떻게 될까요 ?
    

### 2.working directory 안에서 mutsa.py라는 파일의 내용을 수정했습니다. 이 수정한 파일만을 staging area에 올리고 싶다면, 터미널에 어떤 커맨드를 써야할까요 ? ###

- 정답

    ```bash
    git add mutsa.py
    ```

    "git add <파일/디렉토리 경로>" 는 해당 디렉토리의 변경 내용을 스테이징 영역으로 넘겨줍니다.

    이외에도,

    "git add . "는 '현재' 디렉토리 이하의 모든 변경 내용을 스테이징 영역으로,

    "git add -A "는 작업 디렉토리 상의 어디에 위치하든 모든 변경 내용을 스테이징 영역으로 넘겨주는 등 다양한 옵션들이 있습니다.

    +) 다른 자주 쓰이는 옵션에는 무엇이 있을까요?
    

### 3. git 을 이용하여 작성한 프로젝트를 github에 올리려합니다. [ ]에 들어갈 커맨드를 작성해주세요 ! ###

```bash
git [ ]  //git 명령어를 사용할 수 있는 상태로 만듦

git add .    //현재 디렉토리 이하의 모든 변경 내용을 status area에 올림

git commit [ ] "message" //status area에 존재하는 내용들을 변경 내용을 설명하는 "message"와 함께 로컬 저장소에 저장

git [ ] add origin "https://github.com~" //원격 저장소의 이름을 origin으로, 주소를 "https:~"로 추가해준다.

git [        ] //origin이라는 이름으로 등록된 원격 저장소에 master라는 브랜치를 반영한다.

```

- 정답

    init, -m, remote, push origin master

    마지막 "git push origin master" 에서, push 의 옵션으로 -u를 붙이게 되면(git push -u ~)

    최초 실행시에만 원격 저장소와 브랜치의 이름을 적으면 되고 이후에는 "git push"만 입력해도 내용이 반영됩니다.

    +)master 말고 다른 브랜치를 사용하려면 어떻게 해야할까요?
    

### 4. 장고 프로젝트를 위해 현재 여러분은 app까지 만들었습니다.  그 후, 

1. settings.py ⇒[   ]

2. templates ⇒ [   ]

3. views.py ⇒ [  ]

4. urls.py ⇒ [   ]

### 의 단계를 거치려 하는데, 각각 [ ]에 들어갈 설명은 무엇일까요 ? ###

a : views.py에서 처리된 데이터를 받아 사용자에게 화면을 보여줌
b : project에게 app의 존재 알리기
c : 요청에 맞는 함수를 views.py에서 찾아 요청 전달
d : 데이터를 처리하는 함수 작성

- 정답

    1 -  b  , 2  - a , 3 - d, 4 - c   ( 장고 프로젝트의 진행 순서는 당연 유동적이나, 저 순서로 기억하시면 편할듯 합니다 ! )

    + ) 각 단계에서 꼭 입력해야했던 코드들은 무엇이 있을까요 ? (ex : [setting.py](http://setting.py) 에서 app 등록하는 과정 등) 
   

### 5. urls.py의 코드 중

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello.views.home, name='home'),
]
### 이 있다면, path 뒤의  '  ' / hello.views.home/ name='home' 이 세가지가 각각 의미하는 바는 무엇일까요? ###

- 정답

    path는 3가지 인수를 받습니다. 제일 먼저 route인데, 도메인 뒤에 붙는 url 부분이라고 보시면됩니다. 

    - route 이해하기

        확인을 위해 브라우저 주소창에 [http://127.0.0.1:8000/](http://127.0.0.1:8000/admin) 뒤에 admin을 적어봅시다.

        ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2270e064-69c1-40db-8419-04e1164ff0eb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2270e064-69c1-40db-8419-04e1164ff0eb/Untitled.png)

        뭐지 이페이지는!?!?

         나중에 배울 페이지입니다. 지금은 아 url을 통해 저렇게 이동하는구나 정도만 익혀둡시다.

        home 과 연결되는 path는 ' '로 아무것도 적지 않았습니다. 이렇게 적으면 아무것도 적지 않았은 경우, 작동합니다.

    두번째 veiws.home은 연결하고 싶은 views안에 정의된 함수입니다. hello폴더 안의 views파일 안에 home이라고 정의된 함수를 실행시키겠다라는 말입니다.

    마지막 **name='home'**은 이 path의 이름을 home이라 정하겠다고 약속하는 내용으로, 이렇게 약속을 하면 django프로젝트 어디에서든 home이라고 불러서 호출해 낼 수 있습니다.

    가능한 함수이름과 path의 name을 일치시켜주는게 정신건강에 이롭습니다.

---

**깃에 대해 더 알고싶습니다...
: 도움이 될(수도 있는) 참고 사이트 

웹사이트 

 [https://backlog.com/git-tutorial/kr/stepup/stepup1_1.html](https://backlog.com/git-tutorial/kr/stepup/stepup1_1.html)
 [https://learngitbranching.js.org/?locale=ko](https://learngitbranching.js.org/?locale=ko)

강의

[https://www.youtube.com/watch?v=FXDjmsiv8fI&t=468s](https://www.youtube.com/watch?v=FXDjmsiv8fI&t=468s)
