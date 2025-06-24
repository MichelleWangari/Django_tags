from django.shortcuts import render
import datetime
from .models import Blog 
import markdown
from django.utils.safestring import mark_safe

# Create your views here.
def index(request) :
    return render(request, 'index.html',{"message": "Welcome to django"})

def about(request) :
    return render(request, 'about.html')

def contact(request) :
    return render(request, 'contact.html')

def filter_demo(request):
    context = {
        "my_string": "hello world",
        "my_date" : datetime.date(2025, 6, 18),
        "long_string": "This is a long string to be displayed entirely",
        "long_str": "We are working on django",
        "default_name": "Red",
        "sentence" : "i love walking.",
        "word_count" : "Michelle", 
        "fruits" : ["apple", "banana", "orange"],
        "multi_line" : "Number one. Number two. Number three."
    }   
    return render(request, 'filters.html', context)

def blog_list(request):
    blogs = Blog.objects.prefetch_related('editors').all()
    for blog in blogs:
        blog.rendered_text = mark_safe(markdown.markdown(blog.text))
    return render(request, 'blog_list.html', {'blogs':blogs})
