
from django.shortcuts import render, redirect
from pytube import *

def youtube_downloader(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        
        video = YouTube(link)
        stream = video.streams.get_lowest_resolution()
        # stream = video.streams.filter(res="720p").first()
        
        # stream.download()
        # print('Video downloaded successfully')
        # return render(request, 'home.html')
        download_url = stream.url
        return redirect(download_url)
    return render(request, 'home.html')
