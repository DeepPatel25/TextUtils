# I have created this file - Deep
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text', 'default')

    # Check box Value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # Check which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for i, char in enumerate(djtext):
            if not(djtext[i] == " " and djtext[i+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcounter == 'on':
        count = 0
        for char in djtext:
            if char!=" ":
                count = count + 1

        params = {'purpose': 'Char Counter', 'analyzed_text': f"Character Count is : {count}"}

    if removepunc!='on' and newlineremover!='on' and extraspaceremover!='on' and fullcaps!='on' and charcounter!='on':
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)