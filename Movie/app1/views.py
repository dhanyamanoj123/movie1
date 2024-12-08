from django.shortcuts import render,redirect
def home(request):
      m=Movie.objects.all()
      context={'movie':m}
      return render(request,'home.html',context)
from app1.models import Movie
def addmovie(request):
      if (request.method == "POST"):
            t = request.POST['t']
            d = request.POST['d']
            l = request.POST['l']
            y = request.POST['y']
            i = request.FILES['i']
            m = Movie.objects.create(title=t,description=d,language=l,year=y,image=i)
            m.save()
            return redirect('home')
      return render(request,'addmovie.html')
def details(request,p):
      m=Movie.objects.get(id=p)
      context={'movie':m}
      return render(request,'details.html',context)
def delete(request,p):
      m=Movie.objects.get(id=p)
      m.delete()
      return redirect('home')
def edit(request,p):
      m=Movie.objects.get(id=p)
      if (request.method == "POST"):
            m.title = request.POST['t']
            m.description = request.POST['d']
            m.language = request.POST['l']
            m.year = request.POST['y']
      if (request.FILES.get('i') == None):
            m.save()
      else:
            m.image = request.FILES.get('i')
            m.save()
            return redirect('details',p)

      context={'movie':m}
      return render(request,'edit.html',context)