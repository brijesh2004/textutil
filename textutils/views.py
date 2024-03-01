# i have created this file
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    # params = {'name':'Brijesh' , 'place':'Mars'}
    # return render(request , "index.html", params)
    #return HttpResponse("Home")
    return render(request , "index.html")


def analyse(request):
    # get the text
    djtext = request.POST.get('text','default')

    #check box values
    removepunc = request.POST.get('removepunc' , "off")
    fullcaps = request.POST.get('fullcaps' , "off")
    newlineremover = request.POST.get('newlineremover' , "off")
    extraspaceremover = request.POST.get('extraspaceremover' , "off")
    # print(djtext)
    # print(removepunc)
    analyzed = djtext
    
    if(removepunc == 'on'):
        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose':'Removed Punctiation' , 'analyzed_text':analyzed}
        # analyse the text
        return render(request ,"analyse.html", params)
    elif(fullcaps=="on"):
        analyzed = djtext.upper()
        params={'purpose':'Changed to Uppercase' , 'analyzed_text':analyzed}
        return render(request , "analyse.html" , params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed+char
        params={'purpose':'Remove New Line' , 'analyzed_text':analyzed}
        return render(request , "analyse.html" , params)
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index-1]==" "):
                analyzed = analyzed+char
        params={'purpose':'Remove Extra Space' , 'analyzed_text':analyzed}
        return render(request , "analyse.html" , params)
    else:
        return HttpResponse("Error")

# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst page")

# def newlineremove(request):
#     return HttpResponse("newlineremove page")

# def spaceremove(request):
#     return HttpResponse("spaceremove page")

# def charcount(request):
#     return HttpResponse("charcount page")
