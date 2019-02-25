from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from accounts.forms import UserForm,UserProfileInfoForm,BlogForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from accounts.models import UserProfileInfo,Blog
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(TemplateView):
    template_name = 'accounts/blog_list.html'

def index(request):
    return render(request,'accounts/blog_list.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True

            return render(request,'accounts/login.html',{})

        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'accounts/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                #return render(request,'accounts/blog_list.html',{})
            else:
                return HttpResponse('Please Login First')
        else:
            print('Something went wrong..!!')
            return render(request,'accounts/login.html',{'message':'Invalid Credentials'})
    else:
        return render(request,'accounts/login.html',{})

def about(request):
    return render(request,'accounts/about.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'accounts/login.html',{})

class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')

class BlogDetailView(DetailView):
    model = Blog

class CreateBlogView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'accounts/blog_detail.html'

    form_class = BlogForm


    model = Blog

class UpdateBlogView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'accounts/blog_detail.html'

    form_class = BlogForm
    
    model = Blog

class DeleteBlogView(LoginRequiredMixin,DeleteView):
    model = Blog

    success_url = reverse_lazy('accounts:blog_list')

@login_required
def blog_publish(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.publish()
    return redirect('blog_detail', pk=pk)