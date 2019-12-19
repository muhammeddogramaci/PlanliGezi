from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.contrib import messages
from .models import Seyahat,Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# article gördüğün yere Seyahat yaz

def seyahat(request):
    keyword = request.GET.get("keyword")

    if keyword:
        seyahat = Seyahat.objects.filter(title__contains = keyword)
        return render(request,"seyahat.html",{"seyahat":seyahat})
        
    seyahat = Seyahat.objects.all()
    
    return render(request,"seyahat.html",{"seyahat":seyahat})

def index(request):
    return render(request,"index.html")

def about(request):
     return render(request,"about.html")
@login_required(login_url = "user:login")
def dashboard(request):

    Seyahats = Seyahat.objects.filter(yazar = request.user)
    context ={
        "Seyahats":Seyahats
    }
    return render( request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addseyahat(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        Seyahat = form.save(commit=False)

        Seyahat.yazar = request.user
        Seyahat.save()
        messages.success(request,"Başarıyla Kaydedildi")
        return redirect("index")

    return render(request,"addseyahat.html",{"form":form})

def contact(request):
    return render(request,"contact.html")

def detail(request,id):
    seyahat = get_object_or_404(Seyahat,id = id)

    comments = seyahat.comments.all()

    return render(request,"detail.html",{"seyahat":seyahat,"comments":comments})
@login_required(login_url = "user:login")
def updateSeyahat(request,id):

    seyahat = get_object_or_404(Seyahat,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = seyahat)
    
    if form.is_valid():

        seyahat = form.save(commit=False)

        seyahat.yazar = request.user
        seyahat.save()

        messages.success(request,"Başarıyla Güncellendi.")
        return redirect("seyahat:dashboard")
    
    
        
    return render(request,"update.html",{"form":form})
@login_required(login_url = "user:login")
def deleteSeyahat(request,id):

    seyahat = get_object_or_404(Seyahat,id=id)

    seyahat.delete()

    messages.success(request,"Başarıyla Silindi.")

    return redirect("seyahat:dashboard")

def addComment(request,id):
    seyahat = get_object_or_404(Seyahat,id=id)
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

    newComment = Comment(comment_author = comment_author, comment_content=comment_content)
    newComment.Seyahat=seyahat
    newComment.save()

    return redirect(reverse("seyahat:detail",kwargs={"id":id}))

     