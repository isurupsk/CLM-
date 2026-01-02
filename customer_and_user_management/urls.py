from django.urls import include, path
from customer_and_user_management import views
from .views import RetrieveAllGroupsByCustomerView, RetrieveAllGroupsByRoleView, RetrieveAllRolesByCustomerView, RetrieveAllUsersByCustomerView, RetrieveAllUsersByGroupView, RetrieveAllUsersByRoleView, UserLoginView, UserLogoutView, UserProfileView

urlpatterns = [
    # User loging logout profile

    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    # Extra
    path('hello', views.hello_world, name='hello-world'),
    path('user/<int:pk>/group-assignment/',
         views.UserGroupAssignmentView.as_view(), name='user_group_assignment'),
    path('change-password/',
         views.ChangePasswordView.as_view(),
         name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls',
         namespace='password_reset')),
    path('user/<int:pk>/deactivate/',
         views.UserDeactivationView.as_view(), name='user-deactivate'),
    # Permission

#     path('permission/create',
#          views.PermissionCreateView.as_view(),
#          name='permission_create'),
#     path('permission/list',
#          views.PermissionListView.as_view(),
#          name='permission_list'),
#     path('permission/retrieve/<int:pk>/',
#          views.PermissionOneView.as_view(), name='permission_retrieve'),
#     path('permission/update/<int:pk>/',
#          views.PermissionUpdateView.as_view(), name='permission_update'),
#     path('permission/delete/<int:pk>/',
#          views.PermissionDeleteView.as_view(), name='permission_delete'),

    # Role

    path('role/create',
         views.RoleCreateView.as_view(), name='role_create'),
    path('role/list',
         views.RoleListView.as_view(), name='role_list'),
    path('role/retrieve/<int:pk>/',
         views.RoleOneView.as_view(), name='role_retrieve'),
    path('role/update/<int:pk>/',
         views.RoleUpdateView.as_view(), name='role_update'),
    path('role/delete/<int:pk>/',
         views.RoleDeleteView.as_view(), name='role_delete'),
##################### Janitha 07.05 ##########################################
    path('retrieve_all_role/<int:customer_id>/', 
         RetrieveAllRolesByCustomerView.as_view(), name='retrieve_all_roles_by_customer'),
##################### End ##################################################

    # User

    path('user/create',
         views.UserCreateView.as_view(), name='user_create'),
    path('user/list', views.UserListView.as_view(), name='user_list'),
    path('user/retrieve/<int:pk>/',
         views.UserOneView.as_view(), name='user_retrieve'),
    path('user/update/<int:pk>/',
         views.UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/',
         views.UserDeleteView.as_view(), name='user_delete'),
##################### Janitha 07.04 ##########################################
    path('retrieve_all_users_by_role/<int:customer_id>/<int:role_id>/', 
     RetrieveAllUsersByRoleView.as_view(), 
     name='retrieve_all_users_by_role'),

    path('retrieve_all_user_by_group/<int:customer_id>/<int:group_id>/', 
         RetrieveAllUsersByGroupView.as_view(), name='retrieve_all_users_by_group'),
##################### End ##################################################
##################### Janitha 07.05 ##########################################
    path('retrieve_all_user/<int:customer_id>/', 
         RetrieveAllUsersByCustomerView.as_view(), name='retrieve_all_users_by_customer'),
##################### End ##################################################

    # Country

    path('country/create',
         views.CountryCreateView.as_view(), name='country_create'),
    path('country/list',
         views.CountryListView.as_view(), name='country_list'),
    path('country/retrieve/<int:pk>/',
         views.CountryOneView.as_view(), name='country_retrieve'),
    path('country/update/<int:pk>/',
         views.CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<int:pk>/',
         views.CountryDeleteView.as_view(), name='country_delete'),

    # Customer

    path('customer/create',
         views.CustomerCreateView.as_view(),
         name='customer_create'),
    path('customer/list',
         views.CustomerListView.as_view(), name='customer_list'),
    path('customer/retrieve/<int:pk>/',
         views.CustomerOneView.as_view(), name='customer_retrieve'),
    path('customer/update/<int:pk>/',
         views.CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/',
         views.CustomerDeleteView.as_view(), name='customer_delete'),

    # RolePermission

    path('RolePermission/create',
         views.RolePermissionCreateView.as_view(),
         name='RolePermission_create'),
    path('RolePermission/list',
         views.RolePermissionListView.as_view(),
         name='RolePermission_list'),
    path('RolePermission/retrieve/<int:pk>/',
         views.RolePermissionOneView.as_view(),
         name='RolePermission_retrieve'),
    path('RolePermission/update/<int:pk>/',
         views.RolePermissionUpdateView.as_view(),
         name='RolePermission_update'),
    path('RolePermission/delete/<int:pk>/',
         views.RolePermissionDeleteView.as_view(),
         name='RolePermission_delete'),

################## Janitha 07.04 #########################
    path('retrieve_role_permission/<int:role_id>/', 
         views.RetrieveRolePermissionView.as_view(), 
         name='retrieve_role_permission'),
################## End ###################################

    # UserRole

    path('UserRole/create',
         views.UserRoleCreateView.as_view(),
         name='UserRole_create'),
    path('UserRole/list',
         views.UserRoleListView.as_view(), name='UserRole_list'),
    path('UserRole/retrieve/<int:pk>/',
         views.UserRoleOneView.as_view(),
         name='UserRole_retrieve'),
    path('UserRole/update/<int:pk>/',
         views.UserRoleUpdateView.as_view(),
         name='UserRole_update'),
    path('UserRole/delete/<int:pk>/',
         views.UserRoleDeleteView.as_view(),
         name='UserRole_delete'),

    # Group

    path('Group/create', views.GroupCreateView.as_view(), name='Group_create'),
    path('Group/list', views.GroupListView.as_view(), name='Group_list'),
    path('Group/retrieve/<int:pk>/',
         views.GroupOneView.as_view(), name='Group_retrieve'),
    path('Group/update/<int:pk>/',
         views.GroupUpdateView.as_view(), name='Group_update'),
    path('Group/delete/<int:pk>/',
         views.GroupDeleteView.as_view(), name='Group_delete'),

############################# Janitha 07.04 #########################################
    path('retrieve_all_group_by_role/<int:customer_id>/<int:role_id>/', 
         RetrieveAllGroupsByRoleView.as_view(), name='retrieve_all_group_by_role'),
############################ End ####################################################

############################# Janitha 07.05 #########################################
    path('retrieve_all_groups/<int:customer_id>/', 
         RetrieveAllGroupsByCustomerView.as_view(), name='retrieve_all_groups_by_customer'),
############################ End ####################################################
    # GroupRole

    path('GroupRole/create',
         views.GroupRoleCreateView.as_view(),
         name='GroupRole_create'),
    path('GroupRole/list',
         views.GroupRoleListView.as_view(), name='GroupRole_list'),
    path('GroupRole/retrieve/<int:pk>/',
         views.GroupRoleOneView.as_view(), name='GroupRole_retrieve'),
    path('GroupRole/update/<int:pk>/',
         views.GroupRoleUpdateView.as_view(), name='GroupRole_update'),
    path('GroupRole/delete/<int:pk>/',
         views.GroupRoleDeleteView.as_view(), name='GroupRole_delete'),

    # UserGroup

    path('UserGroup/create',
         views.UserGroupCreateView.as_view(),
         name='UserGroup_create'),
    path('UserGroup/list',
         views.UserGroupListView.as_view(), name='UserGroup_list'),
    path('UserGroup/retrieve/<int:pk>/',
         views.UserGroupOneView.as_view(), name='UserGroup_retrieve'),
    path('UserGroup/update/<int:pk>/',
         views.UserGroupUpdateView.as_view(), name='UserGroup_update'),
    path('UserGroup/delete/<int:pk>/',
         views.UserGroupDeleteView.as_view(), name='UserGroup_delete'),

################ Janitha 07.04 ##############################################
path('retrieve_all_groups/<int:customer_id>/', 
     RetrieveAllGroupsByCustomerView.as_view(), name='retrieve_all_groups_by_customer'),
################# End #######################################################

]
