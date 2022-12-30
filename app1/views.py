from django.shortcuts import render

# Create your views here.
def jinja_print(request):

    d={'name':'AB de Villiers', 'no':17}

    return render(request,'jinja_print.html',context=d)
