from django.urls import path
from .import views
# from .views import RegisterView,LoginView
from .views import BookAPI,RegisterUser
urlpatterns = [
    path('home',views.home,name='home'),
    path('',views.register,name='register'),
    # path('',RegisterUser.as_view(),name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('authorsandsellers/',views.authorsandsellers,name='aanss'),
    path('books/',views.books,name='books'),
    path('add_books/',views.add_books,name='add_books'),
    path('df/',views.df,name='dataframe'),
    path('sqlengine/',views.sqlengine,name='sqlengine'),
    
    path('book_api/',BookAPI.as_view()),
    path('api/register/',RegisterUser.as_view()),
    # path('api/login/',LoginView.as_view()),


    
]