from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/new_user', views.register_user, name='register_user'),
    path('accounts/parent_signup/', views.parent_signup, name='parent_signup'),
    path('accounts/nonparent_signup/', views.nonparent_signup, name='nonparent_signup'),
    path('accounts/edit_password/', views.edit_password, name='edit_password'),
    path('children/', views.children_index, name='index'),
    path('children/add', views.add_child, name='add_child'),
    path('children/<int:child_id>/', views.child_detail, name='child_detail'),
    path('children/<int:child_id>/child_edit/', views.child_edit, name='child_edit'),
    path('children/<int:child_id>/add_parent/', views.add_parent, name='add_parent'),
    path('children/<int:child_id>/add_professional/', views.add_professional, name='add_professional'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_name/', views.edit_name, name='edit_name'),
    path('children/<int:child_id>', views.child_detail, name='child_detail'),
    path('children/<int:child_id>/add_parent', views.add_parent, name='add_parent'),
    path('children/<int:child_id>/add_professional', views.add_professional, name='add_professional'),
    path('children/<int:child_id>/add_picture/', views.add_picture, name='add_picture'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_name', views.edit_name, name='edit_name'),
    path('profile/edit_relationship', views.edit_relationship, name='edit_relationship'),
    path('profile/edit_organization', views.edit_organization, name='edit_organization'),
    path('profile/edit_username', views.edit_username, name='edit_username'),
]