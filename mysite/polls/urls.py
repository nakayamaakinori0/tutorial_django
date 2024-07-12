from django.urls import path

from . import views

# 名前空間 polls を定義することで、他のアプリケーションとのurl名の衝突を避ける
app_name = "polls"

"""
urlpatterns = [
  path("", views.index, name= "index"),
# ↓the 'name' value as called by the {% url %} template tag
  path("<int:question_id>/", views.detail, name="detail"),
  path("<int:question_id>/results/", views.results, name="results"),
  path("<int:question_id>/vote/", views.vote, name="vote"),
]
"""

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
