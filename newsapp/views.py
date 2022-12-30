from django.shortcuts import render
import requests


def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=e3a7c5cbcba37d7b61f1cf15cf28dfe1&countries=ua')
    res = r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])
    news = zip(title, description, image, url)
    return render(request, 'index.html', {'news': news})