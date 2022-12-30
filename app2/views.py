from django.shortcuts import render

# Create your views here.
def jinja_print2(request):

    d={'Name':'Virat Kohli', 'No':18}
    return render(request,'jinja_print2.html',context=d)
    