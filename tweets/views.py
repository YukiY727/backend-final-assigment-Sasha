from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):  # LoginRequiredMixinでログインしたユーザーのみhomeにアクセス可能
    template_name = "tweets/home.html"
