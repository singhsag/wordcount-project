from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(request):
    return render(request, 'first_app/home.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    countdict = {}
    for word in words:
        if word in countdict:
            #increase
            countdict[word] += 1
        else:
            # Add
            countdict[word] = 1
    sortedwords = sorted(countdict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'first_app/count.html', {'fulltext': fulltext,
                                                    'words': len(words),
                                                    'sortedwords':sortedwords})

def about(request):
    return render(request, 'first_app/about.html')
