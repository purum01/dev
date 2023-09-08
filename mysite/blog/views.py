from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Post, User, Tag
from .forms import PostModelForm,  PostModelForm

def test1(request):
    return HttpResponse("blog/test1 응답")

def test2(request, no):
    print('no 타입:', type(no))
    return HttpResponse(f'no:{no}')

def test3(request, year, month, day):
    return HttpResponse(f'년:{year}, 월:{month}, 일:{day}')

# def list(request):
#     post_list = Post.objects.all()
#     titles = ''
#     for post in post_list:
#         titles += post.title
#     return HttpResponse(titles)

# def detail(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404('존재하지 않는 데이터입니다.')
    
#     return HttpResponse(post.title)

# def detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     return HttpResponse(post.title)


def list(request):
    post_list = Post.objects.all()
    search_key = request.GET.get("keyword")
    if search_key:
        post_list = Post.objects.filter(title__icontains=search_key)
    return render(request, 'blog/list.html', {'post_all':post_list, 'q':search_key})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_list = post.comments.all()
    tag_list = post.tag.all()
    return render(request, 'blog/detail.html', {'post':post, 'comment_all':comment_list, 'tag_list':tag_list})


def profile(request):
    user = User.objects.get(id=1)
    return render(request, 'blog/profile.html', {'user':user})


def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'blog/list.html', {'post_all':post_list})


def test7(request):
    print('요청방식:',request.method)
    print('GET방식으로 전달된 질의문자열 : ',request.GET)
    print('POST방식으로 전달된 질의 문자열 : ', request.POST)
    print('업로드 파일 : ', request.FILES)
    return render(request, 'blog/form_test.html')



def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)
    else:
        form = PostModelForm()
        return render(request, 'blog/post_form.html', {'form':form})
    
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'blog/post_form.html', {'form':form})
    
def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST' :
        post.delete()
        return redirect('blog:list')
    else:
        return render(request, 'blog/post_delete.html', {'post':post })
    
 