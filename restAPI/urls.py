from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('users-list/', views.getUsers_details, name="users-list"),
    path('get_user/<uuid:uid>/', views.get_user, name='get_user_details'),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('signup/', views.user_create, name="user-create"),
    path('login/', views.custom_user_login, name="user-login"),

	path('user-update/', views.userDetail_Update, name="user-update"),
	path('user-update-by-admin/<uuid:uid>/', views.update_user_by_Admin, name="user-update-by-admin"),
	path('alluser-delete/', views.delete_all_custom_users, name="user-delete"),
	path('specific_user-delete/', views.delete_specific_users, name="user-delete"),
    
	
	# ---------------------------question end points--------------------------------#
    path('create-question/',views.create_question,name="create-question"),
	path('question-list/',views.getQuestion,name="question-list"),
	path('answersForQuestion/',views.getAnswersForQuestion,name="answersForQuestion"),
    path('question-delete/',views.deleteQuestion,name='question-delete'),

	#--------------------------- Answer end points----------------------------------#
	path('write-answer/',views.answer_question,name="answer-a-question"),
    path('answer-delete/',views.deleteAnswer,name='detele-Answer'),
    
    path('refresh-token/', views.refresh_token, name='refresh-token')
]