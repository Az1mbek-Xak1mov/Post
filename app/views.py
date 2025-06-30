from django.shortcuts import render, redirect
from .models import Comment

def reviewView(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        name = request.POST.get('name')
        Comment.objects.create(book_name=book_name, rating=rating, comment=comment, name=name)
        return redirect('review')
    elif request.method == 'GET':
        data = Comment.objects.all()
        context = {'comments': data}
        return render(request, 'app/review.html', context)
