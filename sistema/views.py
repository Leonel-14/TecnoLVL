from django.shortcuts import render
 
def inicio(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request,'html/nosotros.html')

def ayuda(request):
    return render(request,"html/ayuda.html")
