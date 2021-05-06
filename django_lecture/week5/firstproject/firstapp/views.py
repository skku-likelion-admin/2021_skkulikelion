from django.shortcuts import render

# Create your views here.
# 접속할때 바로 실행되는 페이지에 해당한다. 
# 보이는 대로 welcome.html을 반환해준다. 
# 바로 views.py로 이동이 불가능하므로, urls.py로 가서 연결시켜준다.
def welcome(request):
    return render(request,"welcome.html")

def hello(request):
    userName=request.GET['name']
    return render(request,"hello.html",{'userName':userName})
