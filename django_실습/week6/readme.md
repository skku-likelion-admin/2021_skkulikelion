## ☄️배운 내용을 토대로 블로그 (조금) 꾸미기

---

### 🌀{{%for 예시 in 동영상%}}🌀

                                          (소리가 없는 영상이니 바뀐 화면 위주로 참고)

[https://s3-us-west-2.amazonaws.com/secure.notion-static.com/64fb5bd9-fa5d-4520-9220-1b95eb0c3d68/5.10_Practice.mp4](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/64fb5bd9-fa5d-4520-9220-1b95eb0c3d68/5.10_Practice.mp4)

정말 간단한 단계별 실습

### 1. 타이틀 바꾸기

Navbar에 위치한 타이틀과 home.html의 타이틀 모두 자신의 입맛대로 바꾸기!

### 2. Navbar 수정

1) home기능과 write blog 기능 만들기

- home 클릭 시 home.html로 이동
- write blog 클릭 시 new.html로 이동

```html
{{%url '이름'%}} 혹은 {{%url '이름' blog.id%}} 활용
```

2) 필요한 기능의 버튼만 남기기

### 3. 더보기(...more) 버튼으로 만들기

이전의 html, css 실습에서 해봤듯이 bootstrap 활용하여 버튼 입맛대로 고르고 꾸미기 버꾸버꾸

아래의 링크를 통해 버튼 고르기 가능!

[Buttons](https://getbootstrap.com/docs/5.0/components/buttons/)

### 4. 폰트 변경

base.html에서 body 부분 폰트 변경하기

아래의 링크를 통해 폰트 고르기 가능!

[Google Fonts](https://fonts.google.com/?subset=korean)

```html
관련 링크는 <head></head> 사이에 넣기
font-family는 <style></style> 사이에 넣기
```
