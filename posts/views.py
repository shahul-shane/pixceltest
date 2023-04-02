
from .models import Post, Slide, PortImage, Cover, AboutSecondImage, AboutFirstImage, AboutGallery
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):

  allimages = Post.objects.all()  
  cover = Cover.objects.all()
  slide = Slide.objects.all()
  return render(request, 'index.html', {"pics":allimages, "cover":cover, "slides":slide})

def aboutus(request):
  aboutone = AboutFirstImage.objects.all()
  abouttwo = AboutSecondImage.objects.all()
  gallery_images = AboutGallery.objects.all()
  if request.method == "POST":
    name = request.POST['message-name']
    email = request.POST['message-email']
    message = request.POST['message']

    print(name,email,message)

    send_mail(
      name,message,settings.EMAIL_HOST_USER,[email]
    )

    return render(request,'aboutus.html', {'name':name, "AboutFirstImage":aboutone, "AboutSecondImage":abouttwo, "gallery":gallery_images})

  else:
    return render(request, 'aboutus.html',{"AboutFirstImage":aboutone, "AboutSecondImage":abouttwo, "gallery":gallery_images})



def portfolio(request):
  allimages = PortImage.objects.all()  

  return render(request, 'portfolio.html', {"pics":allimages})

def footer(request):
  template = loader.get_template('footer.html')
  return HttpResponse(template.render())

def privacy(request):
  template = loader.get_template('privacy.html')
  return HttpResponse(template.render())


def contacts(request):
  if request.method == "POST":
    name = request.POST['message-name']
    email = request.POST['message-email']
    message = request.POST['message']

    print(name,email,message)

    send_mail(
      name,message,settings.EMAIL_HOST_USER,[email]
    )

    return render(request,'contacts.html', {'name':name})

  else:
    return render(request, 'contacts.html',{})



