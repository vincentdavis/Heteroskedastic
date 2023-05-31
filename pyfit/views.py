from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import FitFileUpload
from pyfitness.load_data import fitfileinfo

import markdown



# Create your views here.
class PyFitIndex(TemplateView):
    template_name = "pyfit/index.html"

    def get_context_data(self, **kwargs):
        print("Hello from PyFitnessIndex")
        context = super().get_context_data(**kwargs)
        context["PyFit"] = "Home"
        return context

class FitFileData(TemplateView):
    template_name = "pyfit/fitfiledata.html"
    form = FitFileUpload()

    def post(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Fit File Data"
        form = FitFileUpload(self.request.POST, self.request.FILES)
        if form.is_valid():
            print("valid form")
            fit_file = self.request.FILES["fit_file"]
            data = fitfileinfo(fit_file)
            html = markdown.markdown(data)
            print(html)
            context['data'] = html
            context['form'] = FitFileUpload()
        return render(self.request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Fit File Data"
        form = FitFileUpload()
        context.update({"form": form})
        return render(request, self.template_name, {"form": form})