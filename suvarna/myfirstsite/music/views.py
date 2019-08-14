from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Album



def index1(request):
    latest_question_list = Album.objects.order_by('id')[:5]
    # template = loader.get_template('music/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request,'music/index.html', context)
# def index1(request):
#     all_album = Album.objects.all()
#     template = template.get_template('music/index.html')
#     context = {"all_album" : all_album,}
#     # html = ''
#     # for i in all_album:
#     #     url = 'music/' +str(i.id) + '/L
#     # latest_question_list = Album.objects.order_by('-id')[:5]
#     # output = "<html><body style='background-image:'https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjK86Kgkv3jAhWf6nMBHY3mAiQQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F422916221244586242%2F&psig=AOvVaw3RBz_nKrtqXj3oij99YiMO&ust=1565692763410512'> Album artist Is:<b style='color:Blue'>"+', '.join([q.artist for q in latest_question_list]) +"</b></body></html"
#     return HttpResponse(template.render(context,request))

def detail(request, album_id):
    return HttpResponse("You're looking at Album Id %s." %album_id)

def results(request, album_id):
    response = "You're looking at the Details of Album  For %s."
    return HttpResponse(response % album_id)