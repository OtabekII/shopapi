# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Goods.models import Banner
from .forms import BannerForm

# List (Bannerlarni ko'rish)
def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'back-office/banners/banner_list.html', {'banners': banners})

# Detail (Bannerni ko'rish)
def banner_detail(request, id):
    banner = get_object_or_404(Banner, id=id)
    return render(request, 'back-office/banners/banner_detail.html', {'banner': banner})

# Create (Yangi Banner yaratish)
def banner_create(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner muvaffaqiyatli yaratildi!')
            return redirect('banners:banner_list')
    else:
        form = BannerForm()
    return render(request, 'back-office/banners/banner_form.html', {'form': form})

# Update (Bannerni yangilash)
def banner_update(request, id):
    banner = get_object_or_404(Banner, id=id)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner muvaffaqiyatli yangilandi!')
            return redirect('banners:banner_detail', id=banner.id)
    else:
        form = BannerForm(instance=banner)
    return render(request, 'back-office/banners/banner_form.html', {'form': form, 'banner': banner})

# Delete (Bannerni o'chirish)
def banner_delete(request, id):
    banner = get_object_or_404(Banner, id=id)
    if request.method == 'POST':
        banner.delete()
        messages.success(request, 'Banner muvaffaqiyatli o\'chirildi!')
        return redirect('banners:banner_list')
    return render(request, 'back-office/banners/banner_confirm_delete.html', {'banner': banner})
