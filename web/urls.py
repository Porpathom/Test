from django.urls import path
from web.views import index, details, about, category, details_cate

urlpatterns = [
    path('',index, name='home' ),
    path('about/',about, name='about' ),
    path('category/',category, name='category' ),
    path('details_cate/<int:id>',details_cate, name='details_cate' ),
    path('details/<int:id>',details, name='details' ),
]