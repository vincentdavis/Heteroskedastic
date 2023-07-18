import csv
import itertools

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import FitFileUpload
from pyfitness.load_data import fitfileinfo, fit2csv, fit2df

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
            fit_file = self.request.FILES["fit_file"].read()


            data = fitfileinfo(fit_file)
            html = markdown.markdown(data)
            context['fileinfo'] = html
            if self.request.POST.get('export_csv', None):
                print("export csv")
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="fitfile.csv"'
                writer = csv.writer(response)
                for row in data:
                    writer.writerow(row)
                # return response
            df = fit2df(fit_file)
            data_csv = csv.DictReader(fit2csv(df).decode("utf-8").splitlines())
            context['csv_header'] = data_csv.fieldnames
            print(context['csv_header'])
            context['csv_data'] = [ [v for v in row.values()] for row in itertools.islice(data_csv, 50)]
            # print(context['csv_data'])
            context['form'] = FitFileUpload()
        return render(self.request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Fit File Data"
        form = FitFileUpload()
        context.update({"form": form})
        return render(request, self.template_name, {"form": form})