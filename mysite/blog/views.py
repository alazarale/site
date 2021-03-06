from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm, ContactForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/blogs.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            status='published',
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    comments = post.comments.filter(active=True)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post, 'comment_form': comment_form, 'comments': comments})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'fordjangouse@gmail.com', [cd['to']])
            sent =True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})

def contact(request):
    if request.POST:
        form_contact = ContactForm(data=request.POST)
        if form_contact.is_valid():
            form_contact.save()
    else:
        form_contact = ContactForm()

    return render(request, 'blog/post/contact.html', {'form_contact': form_contact})











