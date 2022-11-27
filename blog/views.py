from django.shortcuts import render , get_object_or_404
#این خط داره کتابخانه های رندر و گت ابجکت رو ایمپورت میکنه که هر کدوم با توجه به خاصیت های خود در توابع پایین فراخوانی بشن
from django.http import HttpResponse
#این خط داره کتابخانه اچ ریسپانس رو ایمپورت میکنه تا در توابع پایین فراخوانی بشه
from .models import Post
#این خط از قسمت مدل ها داره کلاس پست رو ایمپورت میکنه تا در یکی از توابع پایین فراخوانی بشه
# Create your views here.

def index1(request):
#تابع درخواستی ایندکس رو تعریف میکنیم
    return render(request, 'blog/index.html')
#بطور بازگشتی فراخوانی میشه به اچ تی ام ال ایندکس

def post(request , slug):
#تابع درخواستی ایندکس1 رو تعریف میکنیم
    detail = get_object_or_404(Post, slug=slug, status='P')
#کتابخوانه گت ابجگت رو در متغیر دیتیل فراخوانی میکنیم با پست هایی که استچیوس پی دارند
    context = {
        "detail": detail
    }
    return render(request , 'blog/post.html' , context)
# یک دیکشنری تعریف میکنیم و ولیو رو دیتیل میذاریم تا هر جا دیتیل  بزنیم موارد داخل متغیر دیتیل رو نشون بده

#تابع رو فراخوانی میکنیم و به اچ تی ام ال ایندکس پاس میدهیم

def index(request):
    #تابع درخواستی پست رو تعریف میکنیم
    post = Post.objects.filter(status='P').order_by('-publish')
    #تابع پست رو برابر با پست هایی که استچیوس انها پی یعنی منتشر شده قرار داده و ترتیب نشان دادن اونها با توجه به اخرین پست که منتشر شده به اولی است
    context = {'post': post}
    #یک دیکشنری تعریف میکنیم و ولیو رو پست میذاریم تا هر جا پست باشه بزنیم پست هارو نشون بده
    return render(request, 'blog/index.html', context)
#تابع رو فراخوانی میکنیم و به اچ تی ام ال پست پاس میدهیم