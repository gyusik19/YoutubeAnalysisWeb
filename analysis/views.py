import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from analysis.models import Video, Content

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = BASE_PATH + '/data/'

# Create your views here.
def home(request):
    return render(request, 'home.html')


def get_video_data(self):
    file_list = os.listdir(DATA_PATH)
    for file in file_list:
        with open(DATA_PATH+file, 'r') as f:
            data = json.loads(f.read())
            base_link = 'https://www.youtube.com/watch?v='
            tmp_link = base_link + data['link']
            video_obj = Video(title=data['title'], link=tmp_link)
            video_obj.save()
            content_list = data['contents']
            for content in content_list:
                content_obj = Content(video=video_obj, timeStart=content['time_start'], timeEnd=content['time_end'],
                                      content=content['content'], type='action')
                content_obj.save()
            # video_obj.save()
    return HttpResponse(content_list[1]['time_start'])
