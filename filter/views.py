from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
import numpy as np
import cv2

# Create your views here.


def index(request):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for f in images:
            photo = Images(user_id=current_user.id, name="photo", images=f)
            photo.save()
        messages.success(request, "images added successfully")
        return HttpResponseRedirect(url)
    return render(request, 'index.html')

def gallery(request):
    context = dict()
    current_user = request.user
    context['photos'] = Images.objects.filter(user_id=current_user.id)
    return render(request, 'gallery.html', context)

def photo_detail(request, id):
    context = dict()
    current_user = request.user
    context['photo'] = get_object_or_404(Images, id=id, user_id=current_user.id)

    return render(request, 'filter.html', context)

def filter1(request, id):
    background = "C:/Users/ozgey/Desktop/instagram_filtre/static/images/i2.png"
    image = Images.objects.get(id=id)
    image.is_editted=True
    image.save()
    if request.method == 'POST':
        img_main  = cv2.imread(image.images.path)
        image2 = cv2.imread(background)
        print(image2)
        half = cv2.resize(image2, (img_main.shape[1], img_main.shape[0]), fx = 0.1, fy = 0.1)
        weightedSum = cv2.addWeighted(img_main, 0.5, half, 0.3, 0)  
        cv2.imwrite(image.editted_images.path, weightedSum)

    return redirect("editted_gallery")

def filter2(request, id):
    image.is_editted=True
    image.save()
    image = Images.objects.get(id=id)
    if request.method == 'POST':
        img_main  = cv2.imread(image.images.path)
        gray_image = cv2.cvtColor(img_main, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(image.editted_images.path, gray_image)

    return redirect("editted_gallery")

def filter3(request, id):
    background = "C:/Users/ozgey/Desktop/instagram_filtre/static/images/i3.jpg"
    image = Images.objects.get(id=id)
    image.is_editted=True
    image.save()
    if request.method == 'POST':
        img_main  = cv2.imread(image.images.path)
        image2 = cv2.imread(background)

        half = cv2.resize(image2, (img_main.shape[1], img_main.shape[0]), fx = 0.1, fy = 0.1)
        weightedSum = cv2.addWeighted(img_main, 0.9, half, 0.2, 0)

        im = np.zeros(weightedSum.shape, np.uint8)
        mean = 50
        sigma = 0
        cv2.randn(im,mean,sigma)
        final = cv2.add(weightedSum, im)
        cv2.imwrite(image.editted_images.path, final)

    return redirect("editted_gallery")

def filter4(request, id):
    image = Images.objects.get(id=id)
    image.is_editted=True
    image.save()
    if request.method == 'POST':

        img_main  = cv2.imread(image.images.path)

        filter = np.array([[0.272, 0.534, 0.131],
                   [0.349, 0.686, 0.168],
                   [0.393, 0.769, 0.189]])

        sepia_img=cv2.transform(img_main,filter)
        cv2.imwrite(image.editted_images.path, sepia_img)

    return redirect("editted_gallery")

def editted_gallery(request):
    context = dict()
    current_user = request.user
    context['photos'] = Images.objects.filter(user_id=current_user.id)
    return render(request, 'editted_gallery.html', context)