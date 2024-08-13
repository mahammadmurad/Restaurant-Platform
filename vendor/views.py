from django.shortcuts import render

def v_profile(request):
    return render(request, 'vendor/v_profile.html')
