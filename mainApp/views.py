from django.shortcuts import render
from pytube import YouTube
from django.shortcuts import HttpResponseRedirect


# Create your views here.
def home(request):

    list_stream_video= []
    list_stream_audio=[]
    if(request.method=="POST"):
        url= request.POST.get("url")
        global yt
        yt=YouTube(url)
        s=yt.streams.filter(adaptive=True)
        
        for i in s:
            if(i.type=="video"):
                list_stream_video.append(i)
                
                
            elif(i.type=="audio"):
                list_stream_audio.append(i)
        
        
        return render (request, "index.html", {"Video":list_stream_video, "Audio":list_stream_audio, "You":yt,})
    
        
            
    return render (request, "index.html")

def download(request,tag):
    stream = yt.streams.get_by_itag(tag)
    print(stream)
    stream.download()   
    return HttpResponseRedirect("/")
    
        
        




