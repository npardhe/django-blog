from asyncio import IocpProactor
from audioop import reverse
import io
from unicodedata import category
from django.shortcuts import get_object_or_404, render,get_list_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from requests import delete, request #DetailView -- sent one blog post
from .models import Post,Category,Comment, Profile
from .forms import PostForm,EditPostForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer,ProfileSerializer,UserSerializer,CommentSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated  


# Create your views here.
'''
def home(request):
    return render(request,'home.html')'''

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']  #post ko letest order m display karna
    #ordering = ['post_date']
    #dropdown m data dikhane ke liye
    def get_context_data(self,*arg, **kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*arg, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    def get_context_data(self,*arg, **kwargs):
        cat_menu=Category.objects.all()
        context=super(DetailView,self).get_context_data(*arg, **kwargs)

        stuff=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context['liked']=liked
        return context

class AddPostView(CreateView):
    model=Post
    form_class = PostForm
    template_name= 'add_post.html'
    #fields = '__all__' # copy all fiels of models.py
    #fields=('title','body')
class AddCategoryView(CreateView):
    model=Category
    #form_class = PostForm
    template_name= 'add_category.html'
    fields = '__all__'
    #success_url=reverse_lazy('home')

def CategoryView(request,cats):
    
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    print(category_posts)
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})

def CategoryListView(request):
     cat_menu_list=Category.objects.all()
     return render(request,'category_list.html',{'cat_menu_list': cat_menu_list})



class UpdatePostView(UpdateView):
    model=Post
    form_class=EditPostForm
    template_name = 'update_post.html'
    #fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name = 'delete_post.html'
    success_url=reverse_lazy('home')


class AddCommentView(CreateView):
    model=Comment
    form_class = CommentForm
    template_name= 'add_comment.html'
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)



#      REST API

class ApiView(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self,request):
        post_obj=Post.objects.all()
        ser=PostSerializer(post_obj,many=True)
        return Response(ser.data)
    
    def post(self,request,format=None):
        #json_data=JSONParser().parse(request)
        ser=PostSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Post upload success ','status':'success','post':ser.data},status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors)
    def delete(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        py_data=JSONParser().parse(stream)
        id=py_data.get('id',None)
        if id is not None:
            try:
                s=Post.objects.get(id=id)
            except Post.DoesNotExist:
                res={'msg':'Not exist'}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application e')
            s.delete()
            res={'msg':'Delete success'}
            return Response(res)

class ApiViewUserProfile(APIView):
    def get(self,request):
        post_obj=Profile.objects.all()
        ser=ProfileSerializer(post_obj,many=True)
        return Response(ser.data)
    
    def post(self,request):
        json_data=JSONParser().parse(request)
        ser=ProfileSerializer(data=json_data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,safe=False)
        else:
            return JSONParser(ser.errors,safe=False)



class ApiViewUser(APIView):
    def get(self,request):
        post_obj=User.objects.all()
        ser=UserSerializer(post_obj,many=True)
        return Response(ser.data)
    
    def post(self,request):
        json_data=JSONParser().parse(request)
        ser=UserSerializer(data=json_data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,safe=False)
        else:
            return JSONParser(ser.errors,safe=False)
    def delete(self,request):
        json_data=request.body
        print("000000000000",json_data)
        stream=io.BytesIO(json_data)
        print(stream)
        py_data=JSONParser().parse(stream)
        print(py_data)
        id=py_data.get('id',None)
        print(id)
        if id is not None:
            try:
                s=User.objects.get(id=id)
            except Post.DoesNotExist:
                res={'msg':'Not exist'}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application e')
            s.delete()
            res={'msg':'Delete success'}
            return Response(res)


class ApiViewComment(APIView):
    def get(self,request):
        post_obj=Comment.objects.all()
        ser=CommentSerializer(post_obj,many=True)
        return Response(ser.data)
    
    def post(self,request):
        json_data=JSONParser().parse(request)
        ser=CommentSerializer(data=json_data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,safe=False)
        else:
            return JSONParser(ser.errors,safe=False)