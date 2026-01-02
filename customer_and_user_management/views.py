from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from customer_and_user_management.models import (
    Country, Customer, Group, GroupRole, Permission,
    Role, RolePermission, User, UserGroup, UserRole
)
from customer_and_user_management import serializer
from .serializer import GroupSerializer, RoleSerializer, UserGroupSerializer, UserSerializer
from .serializer import ChangePasswordSerializer
from django.middleware.csrf import get_token


# Views


@api_view()
@permission_classes([permissions.AllowAny])
def hello_world(request):
    return Response('Hello, World!')


######################### Janitha 06.22 ###################################
class ChangePasswordView(generics.UpdateAPIView):
    """An endpoint for changing the password."""
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializeri = self.get_serializer(data=request.data)

        if serializeri.is_valid():
            # Check old password
            if not self.object.check_password(serializeri.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializeri.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializeri.errors, status=status.HTTP_400_BAD_REQUEST)

################################# End ####################################################

################################################################

# deactivate

class UserDeactivationView(APIView):
    @staticmethod
    def put(request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.is_active = False  # Deactivate the user
            user.save()
            return Response({'detail': 'User deactivated successfully.'},
                            status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'},
                            status=status.HTTP_404_NOT_FOUND)
# Deactivate

#  User Looging logout and Profile


# class UserLoginView(APIView):

#     permission_classes = [permissions.AllowAny]

#     @staticmethod
#     @csrf_exempt
#     def post(request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = authenticate(request, email=email, password=password)
#         if user:
#             login(request, user)
#             serializeri = UserSerializer(user)
#             return Response(serializeri.data)
#         return Response({'error': 'Invalid credentials'},
#                         status=status.HTTP_401_UNAUTHORIZED)
###########################################################################

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            serializeri = UserSerializer(user)
            response_data = serializeri.data

            # Include CSRF token in the response
            response_data['csrf_token'] = get_token(request)

            return Response(response_data)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#############################################################################
class UserLogoutView(APIView):
    @staticmethod
    def post(request):
        logout(request)
        return Response({'detail': 'User logged out successfully'})


class UserProfileView(APIView):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            serializeri = UserSerializer(request.user)
            return Response(serializeri.data)
        return Response({'error': 'User is not authenticated'},
                        status=status.HTTP_401_UNAUTHORIZED)

#  End of the Use Loging logout  and Profile


class UserGroupAssignmentView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        group_id = request.data.get('group_id')
        try:
            user = self.queryset.get(pk=user_id)
            group = Group.objects.get(pk=group_id)
        except (User.DoesNotExist, Group.DoesNotExist):
            return Response(status=404)

        user.groups.add(group)
        user.save()
        return Response({'message': 'User assigned to group successfully'})


# Create your views here.

# Permission

# ListView
class PermissionListView(generics.ListAPIView):
    """View for retrieving the Permission List."""

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()

# OneView


class PermissionOneView(generics.RetrieveAPIView):
    """View for retrieving the Permission entry."""

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()

# CreateView


class PermissionCreateView(generics.CreateAPIView):
    """View for retrieving the Permission Create."""

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()

# UpdateView


class PermissionUpdateView(generics.UpdateAPIView):
    """View for retrieving the Permission Update."""

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()

# DeleteView


class PermissionDeleteView(generics.DestroyAPIView):
    """View for retrieving the Permission Delete."""

    serializer_class = serializer.PermissionSerializer

    queryset = Permission.objects.all()


# Role

# ListView
class RoleListView(generics.ListAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

# OneView


class RoleOneView(generics.RetrieveAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

# CreateView


class RoleCreateView(generics.CreateAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

# UpdateView


class RoleUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

# DeleteView


class RoleDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.RoleSerializer

    queryset = Role.objects.all()

############################# Janitha 07.04 ################################
class RetrieveAllUsersByRoleView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        role_id = self.kwargs['role_id']

        customer = get_object_or_404(Customer, pk=customer_id)
        role = get_object_or_404(Role, pk=role_id)

        # Filter users based on the given customer and role.
        return User.objects.filter(customer_id=customer, roles=role)
############################## End #########################################
############################# Janitha 07.05 ################################
class RetrieveAllRolesByCustomerView(generics.ListAPIView):
    serializer_class = RoleSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Role.objects.filter(customer_id=customer_id)
############################## End #########################################


# User

# ListView


class UserListView(generics.ListAPIView):

    serializer_class = serializer.UserSerializer
    queryset = User.objects.all()

# OneView


class UserOneView(generics.RetrieveAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()

# CreateView


class UserCreateView(generics.CreateAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()

# UpdateView


class UserUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()

# DeleteView


class UserDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.UserSerializer

    queryset = User.objects.all()

######################## Janitha 07.04 ###################################

class RetrieveAllUsersByGroupView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        group_id = self.kwargs['group_id']
        return User.objects.filter(usergroup__group_id=group_id, usergroup__user_id__customer_id=customer_id)

########################## End ##############################################
######################## Janitha 07.05 ###################################

class RetrieveAllUsersByCustomerView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return User.objects.filter(customer_id=customer_id)

########################## End ##############################################


# Country

# ListView
class CountryListView(generics.ListAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# OneView


class CountryOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# CreateView


class CountryCreateView(generics.CreateAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# UpdateView


class CountryUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()

# DeleteView


class CountryDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CountrySerializer

    queryset = Country.objects.all()


# Customer

# ListView
class CustomerListView(generics.ListAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()

# OneView


class CustomerOneView(generics.RetrieveAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()

# CreateView


class CustomerCreateView(generics.CreateAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()

# UpdateView


class CustomerUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()

# DeleteView


class CustomerDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.CustomerSerializer

    queryset = Customer.objects.all()


# RolePermission

# ListView
class RolePermissionListView(generics.ListAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

# OneView


class RolePermissionOneView(generics.RetrieveAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

# CreateView


class RolePermissionCreateView(generics.CreateAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

# UpdateView


class RolePermissionUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

# DeleteView


class RolePermissionDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.RolePermissionSerializer

    queryset = RolePermission.objects.all()

################## Janitha 07.04 ######################################
class RetrieveRolePermissionView(generics.RetrieveAPIView):
    serializer_class = serializer.RolePermissionSerializer
    queryset = RolePermission.objects.all()

    def retrieve(self, request, *args, **kwargs):
        role_id = kwargs.get('role_id')
        try:
            role_permission = self.queryset.get(role_id=role_id)
            serializer = self.get_serializer(role_permission)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RolePermission.DoesNotExist:
            return Response({"message": "Role permission not found."}, status=status.HTTP_404_NOT_FOUND)
################## End ################################################


# UserRole

# ListView
class UserRoleListView(generics.ListAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()

# OneView


class UserRoleOneView(generics.RetrieveAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()

# CreateView


class UserRoleCreateView(generics.CreateAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()

# UpdateView


class UserRoleUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()

# DeleteView


class UserRoleDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.UserRoleSerializer

    queryset = UserRole.objects.all()


# Group

# ListView
class GroupListView(generics.ListAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

# OneView


class GroupOneView(generics.RetrieveAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

# CreateView


class GroupCreateView(generics.CreateAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

# UpdateView


class GroupUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

# DeleteView


class GroupDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.GroupSerializer

    queryset = Group.objects.all()

#################### Janitha 07.04 #####################################

#Retrieve All Groups By Role View
class RetrieveAllGroupsByRoleView(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        role_id = self.kwargs['role_id']

        customer = get_object_or_404(Customer, pk=customer_id)
        role = get_object_or_404(Role, pk=role_id)

        group_role_ids = GroupRole.objects.filter(
            group_id__customer_id=customer_id,
            role_id=role_id
        ).values_list('group_id', flat=True)

        return Group.objects.filter(pk__in=group_role_ids)

################### End ##################################################

#################### Janitha 07.05 #####################################

class RetrieveAllGroupsByCustomerView(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Group.objects.filter(customer_id=customer_id)

################### End ##################################################


# GroupRole

# ListView
class GroupRoleListView(generics.ListAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# OneView


class GroupRoleOneView(generics.RetrieveAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# CreateView


class GroupRoleCreateView(generics.CreateAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# UpdateView


class GroupRoleUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# DeleteView


class GroupRoleDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.GroupRoleSerializer

    queryset = GroupRole.objects.all()

# UserGroup

# ListView


class UserGroupListView(generics.ListAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

# OneView


class UserGroupOneView(generics.RetrieveAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

# CreateView


class UserGroupCreateView(generics.CreateAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

# UpdateView


class UserGroupUpdateView(generics.UpdateAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

# DeleteView


class UserGroupDeleteView(generics.DestroyAPIView):

    serializer_class = serializer.UserGroupSerializer

    queryset = UserGroup.objects.all()

############################### Janitha 07.04 #######################################
   
#Retrieve All Groups By Customer View
class RetrieveAllGroupsByCustomerView(generics.ListAPIView):
    serializer_class = UserGroupSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return UserGroup.objects.filter(user_id__customer_id=customer_id)

############################# End ######################################################