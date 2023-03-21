from django.shortcuts import render
from django.views.generic import View

from .models import SettingMain

class HomePageView(View):
    def get(self, request):
        # setting
        settings = SettingMain.objects.get(activate=True)

        return render(request, 'home/index.html', locals())
