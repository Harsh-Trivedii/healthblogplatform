from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from blogapp.forms import SignUpForm,CommentForm,ArticleForm
from blogapp.models import Article,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def home_view(request):
    return render(request,'blogapp/home.html')

def logout_view(request):
    logout(request)
    return render(request,'blogapp/logout.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    context={
        'form':form,
    }
    return render(request,'blogapp/signup.html',context)


@login_required
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blogapp/article_list.html', {'articles': articles})

@login_required
def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article)
    comment_form = CommentForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.article = article
                comment.save()
                return redirect('article_detail', article_id=article_id)
        else:
            return redirect('login')

    return render(request, 'blogapp/article_detail.html', {'article': article, 'comments': comments, 'comment_form': comment_form})


@login_required
def submit_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'blogapp/addarticle.html', {'form': form})