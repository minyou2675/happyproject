from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Tag, Category
from .forms import CommentForm

# Create your views here.

class DiaryUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title','content','head_image','category','tag']
    template_name = 'diary/update_diary.html'
    def dispatch(self, request,*args,**kwargs):
        if request.user.is_authenticated and self.get_object().author == request.user:
            return super(DiaryUpdate,self).dispatch(request,*args,**kwargs)
        else:
            raise PermissionError

class DiaryCreate(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields = ['title','head_image','content','tag','category']
    template_name = 'diary/create_diary.html'

    def test_func(self):
        return self.request.user.is_authenticated or self.request.user.is_staff
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user.username
            return super(DiaryCreate, self).form_valid(form)
        else:
            return redirect('/yuneediary/')

    


class DiaryDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(DiaryDetail,self).get_context_data()
        context['comment_form'] = CommentForm
        return context


class DiaryList(ListView):
    model = Post  
    ordering = '-pk'
    #templates에 있는 model_list.html에다가 db를 넘겨준다. 
    
    def get_context_data(self, **kwargs):
        context = super(DiaryList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
    
def categories(request,slug):
    if slug=='no-category':
        category='미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug = slug)
        context = {
        
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
            'post_list' : Post.objects.filter(category=category)
        }
    return render(request,'diary/post_list.html',context)

def comment_upload(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        comment_temp = comment_form.save(commit=False)
        comment_temp.post = post
        comment_temp.save()
        return redirect(f'/yuneediary/{post.pk}')
        