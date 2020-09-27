from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout    
from blog.models import Post
# Create your views here.
def home(request):
    # return HttpResponse("nitin")
    return render(request,'home/home.html')
    
def about(request):
    return render(request,'home/about.html')
    
def contact(request):
     if request.method=='POST':
         name = request.POST['name']
         email = request.POST['email']
         phone = request.POST['phone']
         content = request.POST['content']
         print(name,email,phone,content)

         if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "plz Fill the Correct information")    
         else:
            contact = Contact(name=name,email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your message has been succesfully sent..")  
     return render(request,'home/contact.html')
    
def search(request):
    query = request.GET['query'].upper()
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent,allPostsAuthor)

    if allPosts.count() == 0:
         messages.warning(request,"No search Results found.Please refine Your query")
    params = {'allPosts':allPosts, 'query':query}
    return render(request,"home/search.html",params)


#django API System
def signupHandle(request):
    # get the post param
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
         # check the errorneous inputs
        if len(username) > 10 or len(username) < 2:
            messages.error(request,"Username Must be Under 10 Characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"Username Should only Contain Letter and Characters")
            return redirect('home')

        if len(pass1) > 20 or len(pass1) < 2:
            messages.error(request,"Password Must be Under 10 Characters")
            return redirect('home')           

        if pass1 != pass2:
            messages.error(request,"Password Does Not Match,Please Enter Right Password")
            return redirect('home')

        # create the user(import user auth)
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your I-Coder Acoount Has been Successfully Created.....!")
        return redirect('home')
    else:
        return HttpResponse('404 - NOt Found!!')
       

# loggin - model
def loginHandle(request):
    if request.method == 'POST':
        usernamelogin = request.POST['usernamelogin']
        passwordlogin = request.POST['passwordlogin']

        user = authenticate(username = usernamelogin, password=passwordlogin)
        
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged In")
        else:
            messages.error(request,"Invalid Credentials , Please Try Again")
    return redirect('home')

# log-out model
def logoutHandle(request):
    logout(request)
    messages.success(request,"Successfully Logged In")    
    return redirect('home')
