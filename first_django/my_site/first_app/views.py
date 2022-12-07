from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


def simple_view(request):
    return render(request, 'first_app/example.html')

# articles = {
#     'sports': 'Sports Page',
#     'finance': 'Finance Page',
#     'politics': 'Politics Page'
# }
#
# def news_view(request, topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(articles[topic])
#     except:
#         result = 'No page for that topic'
#         raise Http404('404 GENERIC ERROR')
#
# def add_view(request, num1, num2):
#
#     result = num1 + num2
#     return HttpResponse(str(result))
#
# # domain.com/first_app/1 ---> domain.com/first_app/politics
#
# def num_page_view(request, num_page):
#     topics_list = list(articles.keys())
#     topic = topics_list[num_page]
#
#     webpage = reverse('topic-page', args=[topic])
#     return HttpResponseRedirect(webpage)



# Create your views here.
