from django.views.generic import TemplateView
import random

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        n = random.randint(1,100)
        context["random_value"] = str(n)
        return context


class AboutPageView(TemplateView): 
    template_name = "about.html"