"""
vehicle
"""
from django.contrib import admin
from django.urls import path
from vehicle import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('customerclick', views.customerclick_view),
    path('mechanicsclick', views.mechanicsclick_view),
    path('mechanicsclick2', views.mechanicsclick2_view),

    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('mechanicsignup', views.mechanic_signup_view,name='mechanicsignup'),
    path('mechanicsignup2', views.mechanic_signup_view2,name='mechanicsignup2'),

    path('customerlogin', LoginView.as_view(template_name='vehicle/customerlogin.html'),name='customerlogin'),
    path('mechaniclogin', LoginView.as_view(template_name='vehicle/mechaniclogin.html'),name='mechaniclogin'),
    path('mechaniclogin2', LoginView.as_view(template_name='vehicle/mechaniclogin2.html'),name='mechaniclogin2'),
    path('adminlogin', LoginView.as_view(template_name='vehicle/adminlogin.html'),name='adminlogin'),

    path('mailsent',views.mailsent,name='mailsent'),

    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-customer', views.admin_customer_view,name='admin-customer'),
    path('admin-view-customer',views.admin_view_customer_view,name='admin-view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('admin-add-customer', views.admin_add_customer_view,name='admin-add-customer'),
    path('admin-view-customer-enquiry', views.admin_view_customer_enquiry_view,name='admin-view-customer-enquiry'),
    path('admin-view-customer-invoice', views.admin_view_customer_invoice_view,name='admin-view-customer-invoice'),


    path('admin-request', views.admin_request_view,name='admin-request'),
    path('admin-view-request',views.admin_view_request_view,name='admin-view-request'),
    path('admin-view-request2',views.admin_view_request_view2,name='admin-view-request2'),
    path('mechanic-view-request',views.mechanic_view_request_view,name='mechanic-view-request'),
    path('mechanic-view-request2',views.mechanic_view_request_view2,name='mechanic-view-request2'),
    path('change-status/<int:pk>', views.change_status_view,name='change-status'),
    path('admin-delete-request/<int:pk>', views.admin_delete_request_view,name='admin-delete-request'),
    path('admin-add-request',views.admin_add_request_view,name='admin-add-request'),
    path('admin-approve-request',views.admin_approve_request_view,name='admin-approve-request'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    
    path('admin-view-service-cost',views.admin_view_service_cost_view,name='admin-view-service-cost'),
    path('update-cost/<int:pk>', views.update_cost_view,name='update-cost'),

    path('admin-mechanic', views.admin_mechanic_view,name='admin-mechanic'),
    path('admin-mechanic2', views.admin_mechanic_view2,name='admin-mechanic2'),
    path('admin-view-mechanic',views.admin_view_mechanic_view,name='admin-view-mechanic'),
    path('admin-view-mechanic2',views.admin_view_mechanic_view2,name='admin-view-mechanic2'),
    path('delete-mechanic/<int:pk>', views.delete_mechanic_view,name='delete-mechanic'),
    path('delete-mechanic2/<int:pk>', views.delete_mechanic_view2,name='delete-mechanic2'),
    path('update-mechanic/<int:pk>', views.update_mechanic_view,name='update-mechanic'),
     path('update-mechanic2/<int:pk>', views.update_mechanic_view2,name='update-mechanic2'),
    path('admin-add-mechanic',views.admin_add_mechanic_view,name='admin-add-mechanic'),
    path('admin-add-mechanic2',views.admin_add_mechanic_view2,name='admin-add-mechanic2'),
     path('search',views.search,name='search'),
    path('admin-approve-mechanic',views.admin_approve_mechanic_view,name='admin-approve-mechanic'),
    path('admin-approve-mechanic2',views.admin_approve_mechanic_view2,name='admin-approve-mechanic2'),
    path('approve-mechanic/<int:pk>', views.approve_mechanic_view,name='approve-mechanic'),
    path('approve-mechanic2/<int:pk>', views.approve_mechanic_view2,name='approve-mechanic2'),
    path('delete-mechanic/<int:pk>', views.delete_mechanic_view,name='delete-mechanic'),
    path('delete-mechanic2/<int:pk>', views.delete_mechanic_view2,name='delete-mechanic2'),
    path('admin-view-mechanic-salary',views.admin_view_mechanic_salary_view,name='admin-view-mechanic-salary'),
    path('update-salary/<int:pk>', views.update_salary_view,name='update-salary'),

    path('admin-mechanic-attendance', views.admin_mechanic_attendance_view,name='admin-mechanic-attendance'),
    path('admin-take-attendance', views.admin_take_attendance_view,name='admin-take-attendance'),
    path('admin-view-attendance', views.admin_view_attendance_view,name='admin-view-attendance'),
    path('admin-feedback', views.admin_feedback_view,name='admin-feedback'),

    path('admin-report', views.admin_report_view,name='admin-report'),

    path('mechanic-dashboard', views.mechanic_dashboard_view,name='mechanic-dashboard'),
    path('mechanic-dashboard2', views.mechanic_dashboard_view2,name='mechanic-dashboard2'),
    path('mechanic-work-assigned', views.mechanic_work_assigned_view,name='mechanic-work-assigned'),
     path('mechanic-work-assigned2', views.mechanic_work_assigned_view2,name='mechanic-work-assigned2'),
    path('mechanic-update-status/<int:pk>', views.mechanic_update_status_view,name='mechanic-update-status'),
    path('mechanic-update-status2/<int:pk>', views.mechanic_update_status_view2,name='mechanic-update-status2'),
    path('mechanic-feedback', views.mechanic_feedback_view,name='mechanic-feedback'),
    path('mechanic-feedback2', views.mechanic_feedback_view2,name='mechanic-feedback2'),
    path('mechanic-salary', views.mechanic_salary_view,name='mechanic-salary'),
    path('mechanic-profile', views.mechanic_profile_view,name='mechanic-profile'),
    path('mechanic-profile2', views.mechanic_profile_view2,name='mechanic-profile2'),
    path('edit-mechanic-profile', views.edit_mechanic_profile_view,name='edit-mechanic-profile'),
    path('edit-mechanic-profile2', views.edit_mechanic_profile_view2,name='edit-mechanic-profile2'),

    path('mechanic-attendance', views.mechanic_attendance_view,name='mechanic-attendance'),



    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customer-request', views.customer_request_view,name='customer-request'),
    path('customer-add-request',views.customer_add_request_view,name='customer-add-request'),

    path('customer-profile', views.customer_profile_view,name='customer-profile'),
    path('edit-customer-profile', views.edit_customer_profile_view,name='edit-customer-profile'),
    path('customer-feedback', views.customer_feedback_view,name='customer-feedback'),
    path('customer-invoice', views.customer_invoice_view,name='customer-invoice'),
    path('customer-view-request',views.customer_view_request_view,name='customer-view-request'),
    path('customer-delete-request/<int:pk>', views.customer_delete_request_view,name='customer-delete-request'),
    path('customer-view-approved-request',views.customer_view_approved_request_view,name='customer-view-approved-request'),
    path('customer-view-approved-request-invoice',views.customer_view_approved_request_invoice_view,name='customer-view-approved-request-invoice'),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='vehicle/index.html'),name='logout'),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    #path('kommunicate', views.kommunicate,name='kommunicate'),

    path('pinsearch',views.pinsearch,name='pinsearch'),
    path('pinsearch2',views.pinsearch2,name='pinsearch2'),

    path('consumesearch',views.consumesearch,name='consumesearch'),
    path('consumesearch2',views.consumesearch2,name='consumesearch2'),

]
