
from django.shortcuts import render, redirect
from pytube import *
from django.contrib import messages

def youtube_downloader(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        
        if link is not None:
            video = YouTube(link)
            stream = video.streams.get_lowest_resolution()
            # stream = video.streams.filter(res="720p").first()
            
            # stream.download()
            # print('Video downloaded successfully')
            # return render(request, 'home.html')
            download_url = stream.url
            return redirect(download_url)
        else :
            messages.error(request, "Must Pass the link")
    return render(request, 'home.html')
