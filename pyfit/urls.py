from django.urls import path
from pyfit.views import PyFitIndex, FitFileData

app_name = "pyfit"

urlpatterns = [
    path("", PyFitIndex.as_view(), name="pyfit_index"),
    path("fitfiledata/", FitFileData.as_view(), name="fitfiledata"),
]