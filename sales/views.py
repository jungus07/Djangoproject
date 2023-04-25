from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sale,Person
from .forms import SaleForm,SaleModelForm

# Create your views here.
def 세일목록(request):
    사람 = Sale.objects.all()
    context ={
        "사람키": 사람
    }#딕셔너리
    return render(request, "newfolder/세일목록.html",context)

def 세일상세(request,pk):
    print(pk)

    사람 = Sale.objects.get(id=pk)

    context = {
        "사람키": 사람
    }
    return render(request, "newfolder/세일상세.html", context)

def 세일입력(request):
    form = SaleModelForm()
    if request.method == "POST":
        form = SaleModelForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("/홈페이지")

    context = {
        "Form키": SaleModelForm()
    }

    return render(request,"newfolder/세일입력.html",context)

""" def 세일입력(request):
    form = SaleForm()
    if request.method == "POST":
        print("POST METHOD로 왔네요")
        form = SaleForm(request.POST)
        if form.is_valid():
            print("유효함")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            person = Person.objects.first()

            Sale.objects.create(
                first_name = first_name, 
                last_name = last_name, 
                age = age,
                person = person
            )
            print("세일이 입력됐습니다.")
            
            return redirect("/홈페이지")

    context = {
        "Form키": SaleForm()
    }

    return render(request,"newfolder/세일입력.html",context) """