

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,admin
from django.urls import reverse_lazy
from .models import book,issuedbook,student
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def home(request):
    return render(request,'lms/home.html')

@login_required(login_url='login')
def success(request):
    return render(request,'lms/success.html')



def success_admin(request):
    return render(request,'lms/success_admin.html')

def my_view(request):
    if request.method=='POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            
            return redirect('/success')
    else:
        return render(request,'lms/student_login.html')

def admin_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        admin = authenticate(request, username=username, password=password)
        if admin is not None:
            login(request, admin)
        # Redirect to a success page.
            
            return redirect('/success_admin')
    else:
        return render(request,'lms/admin_login.html')



def add_books(request):
    if request.method=='POST':
        name=request.POST['name']
        isbn=request.POST['isbn']
        author=request.POST['author']
        book_obj=book.objects.create(book_name=name,isbn=isbn,author=author)
        book_obj.save()
        return redirect('/viewbook')
    else:
        return render(request,'lms/addbook.html')
class Home(ListView):
    model=book
    context_object_name='book_list'
class Update(UpdateView):
    model=book
    fields="__all__"
    success_url="/viewbook/"
class Delete(DeleteView):
    model=book
    success_url="/viewbook/"
def studentsignup_view(request):
    form1=forms.StudentUserForm()
    form2=forms.StudentExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2=forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)

        return redirect('/login')
    return render(request,'lms/signup.html',context=mydict)



def issuebook_view(request):
    form=forms.IssuedBookForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.IssuedBookForm(request.POST)
        if form.is_valid():
            obj=models.issuedbook()
            obj.enrollment=request.POST.get('enrollment')
            obj.isbn=request.POST.get('isbn')
            obj.save()
            return render(request,'lms/inter.html')
    return render(request,'lms/issuebook.html',{'form':form})



def viewissuedbook_view(request):
    issuedbooks=models.issuedbook.objects.all()
    li=[]
    for ib in issuedbooks:
        books=list(models.book.objects.filter(isbn=ib.isbn))
        students=list(models.student.objects.filter(enrollment=ib.enrollment))
        i=0
        for l in books:
            t=(students[i].get_name,students[i].enrollment,books[i].book_name,books[i].author)
            i=i+1
            li.append(t)
    return render(request,'lms/viewissuedbook.html',{'li':li})

login_required(login_url='login/')
def viewissuedbookbystudent(request):
    student=models.student.objects.filter(user_id=request.user.id) #gets logged in student object
    issuedbook=models.issuedbook.objects.filter(enrollment=student[0].enrollment) #gets the issued books of enrollment of logged in student
    li1=[]
    for ib in issuedbook:
        books=models.book.objects.filter(isbn=ib.isbn) #gets all books whoose isbn is same as the isbn of the books with enrollment value same as the enrollment value of the logged in student
        for book in books:
            t=(request.user,student[0].enrollment,book.book_name,book.author)
            li1.append(t)

    return render(request,'lms/viewissuedbookbystudent.html',{'li1':li1})

def logout(request):
    return render(request,'lms/logged_out.html')