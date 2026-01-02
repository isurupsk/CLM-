import json
from datetime import date, datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from customer_and_user_management.models import (
Country,
Customer,
Permission,
Role,
RolePermission,
Group,
GroupRole,
User,
Language,
Currency,
DateFormat,
UserRole,
UserGroup,
)
import pytest
import os
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from customer_and_user_management.serializer import RoleSerializer
from django.conf import settings
from pathlib import Path

####################### country #######################

@pytest.mark.django_db
class TestCountryViews:

    def test_country_list_view(self):
        client = APIClient()
        url = reverse('country_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_country_create_view(self):
        client = APIClient()
        url = reverse('country_create')
        data = {'country': 'Test Country'}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_country_retrieve_view(self):
        country = Country.objects.create(country='Test Country')
        client = APIClient()
        url = reverse('country_retrieve', kwargs={'pk': country.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_country_update_view(self):
        country = Country.objects.create(country='Test Country')
        client = APIClient()
        url = reverse('country_update', kwargs={'pk': country.pk})
        data = {'country': 'Updated Country'}
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Country.objects.get(pk=country.pk).country == 'Updated Country'

    def test_country_delete_view(self):
        country = Country.objects.create(country='Test Country')
        client = APIClient()
        url = reverse('country_delete', kwargs={'pk': country.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(Country.DoesNotExist):
            Country.objects.get(pk=country.pk)

####################### customer #######################

@pytest.mark.django_db
class TestCustomerViews:
    def test_customer_create(self):
        client = APIClient()
        url = reverse('customer_create')
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png' 
        with open(image_path, 'rb') as file:
          image_file = SimpleUploadedFile(name='Django.png', content=file.read(), content_type='image/png')
        data = {
        'company_url': 'https://example-updated.com',
        'company_name': 'Test Company',
        'company_address': '123 Street',
        'contact_number': '1234567890',
        'country': country.country_id,
        'gst_tax_number': '55',
        'company_logo_url': 'www.Hello',
        'company_image': image_file,
        'contact_name': 'XGays2',
        'contact_email': 'Isuru1@gmail.com',
        'contact_phone_number': '221613',
        'licence_type': 'xyz',
        'licence_start_date': '2022-02-13',  
        'licence_end_date': '2023-02-13',
        'licence_user_quantity': 5,
        'status': True,
        'is_social_login_enabled': False,
        'unique_id': 'ABC123',
        'city': 'City Name',
        'state': 'State Name',
        'org_admin_email': 'admin@example.com',
        'org_admin_full_name': 'Admin Name',
        'org_admin_contact_number': '9876543210',
        'contract_manager_email': 'manager@example.com',
        'contract_manager_full_name': 'Manager Name',
        'contract_manager_contact_number': '9876543210',
      }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Customer.objects.count() == 1
        assert response.data['company_name'] == 'Test Company'

    
    def test_customer_list_view(self):
        client = APIClient()
        url = reverse('customer_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK     

    def test_customer_update(self):
        client = APIClient()
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
        company_url= 'https://example-updated.com',
        company_name= 'Test Company',
        company_address = '123 Street',
        contact_number ='1234567890',
        country =country,
        gst_tax_number= '55',
        company_logo_url= 'www.Hello',
        company_image= absolute_file_path,
        contact_name= 'XGays2',
        contact_email= 'Isuru1@gmail.com',
        contact_phone_number= '221613',
        licence_type= 'xyz',
        licence_start_date ='2022-02-13',  
        licence_end_date ='2023-02-13',
        licence_user_quantity= '5',
        status= True,
        is_social_login_enabled =False,
        unique_id= 'ABC123',
        city= 'City Name',
        state ='State Name',
        org_admin_email ='admin@example.com',
        org_admin_full_name ='Admin Name',
        org_admin_contact_number= '9876543210',
        contract_manager_email= 'manager@example.com',
        contract_manager_full_name= 'Manager Name',
        contract_manager_contact_number= '9876543210',
          
        )
        url = reverse('customer_update', kwargs={'pk': customer.pk})

        data = {
        'company_url': 'https://example-updated.com',
        'company_name': 'Test Company Updated',
        'company_address': '123 Street',
        'contact_number': '1234567890',
        'country': country.country_id,
        'gst_tax_number': '55',
        'company_logo_url': 'www.Hello',
        'company_image': open(absolute_file_path, 'rb'),
        'contact_name': 'XGays2',
        'contact_email': 'Isuru1@gmail.com',
        'contact_phone_number': '221613',
        'licence_type': 'xyz',
        'licence_start_date': '2022-02-13',  
        'licence_end_date': '2023-02-13',
        'licence_user_quantity': 5,
        'status': True,
        'is_social_login_enabled': False,
        'unique_id': 'ABC123',
        'city': 'City Name',
        'state': 'State Name',
        'org_admin_email': 'admin@example.com',
        'org_admin_full_name': 'Admin Name',
        'org_admin_contact_number': '9876543210',
        'contract_manager_email': 'manager@example.com',
        'contract_manager_full_name': 'Manager Name',
        'contract_manager_contact_number': '9876543210',
      }

        response = client.put(url, data)
        print(response.data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['company_name'] == 'Test Company Updated'

    def test_customer_retrieve_view(self):
        client = APIClient()
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
        company_url= 'https://example-updated.com',
        company_name= 'Test Company',
        company_address = '123 Street',
        contact_number ='1234567890',
        country =country,
        gst_tax_number= '55',
        company_logo_url= 'www.Hello',
        company_image= absolute_file_path,
        contact_name= 'XGays2',
        contact_email= 'Isuru1@gmail.com',
        contact_phone_number= '221613',
        licence_type= 'xyz',
        licence_start_date ='2022-02-13',  
        licence_end_date ='2023-02-13',
        licence_user_quantity= '5',
        status= True,
        is_social_login_enabled =False,
        unique_id= 'ABC123',
        city= 'City Name',
        state ='State Name',
        org_admin_email ='admin@example.com',
        org_admin_full_name ='Admin Name',
        org_admin_contact_number= '9876543210',
        contract_manager_email= 'manager@example.com',
        contract_manager_full_name= 'Manager Name',
        contract_manager_contact_number= '9876543210',
          
        )

        url = reverse('customer_retrieve', args=[customer.customer_id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['company_name'] == 'Test Company'

    def test_customer_delete_view(self):
        client = APIClient()
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
        company_url= 'https://example-updated.com',
        company_name= 'Test Company',
        company_address = '123 Street',
        contact_number ='1234567890',
        country =country,
        gst_tax_number= '55',
        company_logo_url= 'www.Hello',
        company_image= absolute_file_path,
        contact_name= 'XGays2',
        contact_email= 'Isuru1@gmail.com',
        contact_phone_number= '221613',
        licence_type= 'xyz',
        licence_start_date ='2022-02-13',  
        licence_end_date ='2023-02-13',
        licence_user_quantity= '5',
        status= True,
        is_social_login_enabled =False,
        unique_id= 'ABC123',
        city= 'City Name',
        state ='State Name',
        org_admin_email ='admin@example.com',
        org_admin_full_name ='Admin Name',
        org_admin_contact_number= '9876543210',
        contract_manager_email= 'manager@example.com',
        contract_manager_full_name= 'Manager Name',
        contract_manager_contact_number= '9876543210',
          
        )

        url = reverse('customer_delete', kwargs={'pk': customer.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(Customer.DoesNotExist):
            Customer.objects.get(pk=customer.pk)

####################### Permisson #######################

@pytest.mark.django_db
class TestPermissionViews:
    def test_permission_create(self):
        client = APIClient()
        url = reverse('permission_create')
        data = {
            'permission': 'Test Permission',
            'status': True
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Permission.objects.count() == 1
        assert response.data['permission'] == 'Test Permission'

    def test_permission_list(self):
        client = APIClient()
        url = reverse('permission_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_permission_retrieve(self):
        client = APIClient()
        permission = Permission.objects.create(permission='Test Permission', status=True)
        url = reverse('permission_retrieve', args=[permission.permission_id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['permission'] == 'Test Permission'

    def test_permission_update(self):
        client = APIClient()
        permission = Permission.objects.create(permission='Test Permission', status=True)
        url = reverse('permission_update', args=[permission.permission_id])
        data = {
            'permission': 'Updated Permission',
            'status': False
        }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['permission'] == 'Updated Permission'

    def test_permission_delete(self):
        client = APIClient()
        permission = Permission.objects.create(permission='Test Permission', status=True)
        url = reverse('permission_delete', args=[permission.permission_id])
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Permission.objects.count() == 0

####################### role #######################

@pytest.mark.django_db
class TestRoleViews:
    def test_role_create(self):
        client = APIClient()
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
        company_url= 'https://example-updated.com',
        company_name= 'Test Company',
        company_address = '123 Street',
        contact_number ='1234567890',
        country =country,
        gst_tax_number= '55',
        company_logo_url= 'www.Hello',
        company_image= absolute_file_path,
        contact_name= 'XGays2',
        contact_email= 'Isuru1@gmail.com',
        contact_phone_number= '221613',
        licence_type= 'xyz',
        licence_start_date ='2022-02-13',  
        licence_end_date ='2023-02-13',
        licence_user_quantity= '5',
        status= True,
        is_social_login_enabled =False,
        unique_id= 'ABC123',
        city= 'City Name',
        state ='State Name',
        org_admin_email ='admin@example.com',
        org_admin_full_name ='Admin Name',
        org_admin_contact_number= '9876543210',
        contract_manager_email= 'manager@example.com',
        contract_manager_full_name= 'Manager Name',
        contract_manager_contact_number= '9876543210',
          
        )
       
        url = reverse('role_create')
        data = {
            'role_name': '1',
            'role_type': 'ContractManagement',
            'description': 'Test Role',
            'status': True,
            'customer_id': customer.customer_id,
           
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Role.objects.count() == 1
        role = Role.objects.first()
        assert role.description == 'Test Role'
        assert role.status == True
        assert role.customer_id_id == customer.customer_id
        assert role.role_name == '1'
        assert response.data == RoleSerializer(role).data
 
    def test_role_update(self):
        client = APIClient()
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample role
        role = Role.objects.create(
            role_name='1',
            role_type='ContractManagement',
            description='Test Role',
            status=True,
            customer_id=customer,   # custemer eke ID eka kiyala danna nikamana customer kiyala danna epaa. Model eka tiyana widhata balanna 
            
        )
        url = reverse('role_update', kwargs={'pk': role.pk})
        data = {
            'role_name': '2',
            'role_type': 'ContractManagement',
            'description': 'Updated Role',
            'status': False,
            'customer_id': customer.customer_id,
           
        }
        response = client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        role.refresh_from_db()
        assert role.description == 'Updated Role'
        assert role.status == False
        assert role.customer_id_id == customer.customer_id
        assert role.role_name == '2'
        assert response.data == RoleSerializer(role).data

    def test_role_list(self):
        client = APIClient()

        # Create a sample customer and roles
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image=absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  # Corrected field name
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        role1 = Role.objects.create(
            description='Role 1',
            status=True,
            customer_id=customer,
            role_name='ContractManager'
        )

        role2 = Role.objects.create(
            description='Role 2',
            status=False,
            customer_id=customer,
            role_name='ContractAuthor'
        )

        url = reverse('role_list')
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0] == RoleSerializer(role1).data
        assert response.data[1] == RoleSerializer(role2).data


    def test_role_retrieve(self):
        client = APIClient()

        # Create a sample customer and role
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  # Corrected field name
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        role = Role.objects.create(
            description='Test Role',
            status=True,
            customer_id=customer,
            role_name='ContractManager'
        )

        url = reverse('role_retrieve', kwargs={'pk': role.pk})
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == RoleSerializer(role).data

    @pytest.mark.django_db
    def test_role_delete(self):
        client = APIClient()

        # Create a sample customer and role
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  # Corrected field name
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        role = Role.objects.create(
            description='Test Role',
            status=True,
            customer_id=customer,
            role_name='ContractManager'
        )

        url = reverse('role_delete', kwargs={'pk': role.pk})
        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Role.objects.count() == 0


####################### role Permisson #######################

@pytest.mark.django_db
class TestRolePermissionViews:
    def test_role_permission_retrieve(self):
        client = APIClient()

        # Create a sample customer and role
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        role = Role.objects.create(
            role_name='1',
            role_type='ContractManagement',
            description='Test Role',
            status=True,
            customer_id=customer,    
            
        )

        # Create a sample permission
        permission = Permission.objects.create(
            permission='Test Permission',
            status=True
        )

        # Create a sample role permission
        role_permission = RolePermission.objects.create(
            role_id=role.role_id,
            permission_id=permission.permission_id
        )

        url = reverse('RolePermission_retrieve', kwargs={'pk': role_permission.pk})
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['role'] == role_permission.role_id
        assert response.data['permission'] == role_permission.permission_id

    def test_role_permission_update(self):
        client = APIClient()

        # Create a sample customer and role
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        role = Role.objects.create(
            role_name='1',
            role_type='ContractManagement',
            description='Test Role',
            status=True,
            customer_id=customer,    
            
        )

        # Create a sample permission
        permission = Permission.objects.create(
            permission='Test Permission',
            status=True
        )

        # Create a sample role permission
        role_permission = RolePermission.objects.create(
            role=role,
            permission=permission
        )

        new_permission = Permission.objects.create(
            permission='Updated Permission',
            status=True
        )

        url = reverse('RolePermission_update', kwargs={'pk': role_permission.pk})
        data = {
            'role': role.role_id,
            'permission': new_permission.permission_id
        }
        response = client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['role'] == role.role_id
        assert response.data['permission'] == new_permission.permission_id

    def test_role_permission_list(self):
        client = APIClient()

        # Create a sample customer and role
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        role = Role.objects.create(
            role_name='1',
            role_type='ContractManagement',
            description='Test Role',
            status=True,
            customer_id=customer,    
            
        )

        # Create sample permissions
        permission1 = Permission.objects.create(
            permission='Permission 1',
            status=True
        )

        permission2 = Permission.objects.create(
            permission='Permission 2',
            status=True
        )

        # Create sample role permissions
        role_permission1 = RolePermission.objects.create(
            role=role,
            permission=permission1
        )

        role_permission2 = RolePermission.objects.create(
            role=role,
            permission=permission2
        )

        url = reverse('RolePermission_list')
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]['role'] == role_permission1.role_id
        assert response.data[0]['permission'] == role_permission1.permission_id
        assert response.data[1]['role'] == role_permission2.role_id
        assert response.data[1]['permission'] == role_permission2.permission_id

    def test_role_permission_create(self):
        client = APIClient()

        # Create a sample customer and role
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210', 
        )

        role = Role.objects.create(
            role_name='1',
            role_type='ContractManagement',
            description='Test Role',
            status=True,
            customer_id=customer,    
            
        )

        # Create a sample permission
        permission = Permission.objects.create(
            permission='Test Permission',
            status=True
        )

        payload = {
            'role': role.role_id,
            'permission': permission.permission_id
        }

        url = reverse('RolePermission_create')
        response = client.post(url, json.dumps(payload), content_type='application/json')

        assert response.status_code == status.HTTP_201_CREATED
        assert RolePermission.objects.count() == 1
        assert response.data['role'] == role.role_id
        assert response.data['permission'] == permission.permission_id

    def test_role_permission_delete(self):
        client = APIClient()

        # Create a sample customer and role
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        role = Role.objects.create(
            role_name='1',
            role_type='ContractManagement',
            description='Test Role',
            status=True,
            customer_id=customer,    
            
        )

        # Create a sample permission
        permission = Permission.objects.create(
            permission='Test Permission',
            status=True
        )

        # Create a sample role permission
        role_permission = RolePermission.objects.create(
            role=role,
            permission=permission
        )

        url = reverse('RolePermission_delete', kwargs={'pk': role_permission.pk})
        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert RolePermission.objects.count() == 0

####################### group #######################

@pytest.mark.django_db
class TestGroupViews:
    def test_group_create(self):
        client = APIClient()

        # Create a sample customer
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Define the group payload
        group_payload = {
            'group_name': 'Test Group',
            'description': 'Test Group Description',
            'status': True,
            'customer_id': customer.customer_id
        }

        url = reverse('Group_create')
        response = client.post(url, data=group_payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert Group.objects.count() == 1
        assert Group.objects.first().group_name == 'Test Group'

    def test_group_retrieve(self):
        client = APIClient()

        # Create a sample customer
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample group
        group = Group.objects.create(
            group_name='Test Group',
            description='Test Group Description',
            status=True,
            customer_id=customer
        )

        url = reverse('Group_retrieve', kwargs={'pk': group.pk})
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['group_name'] == group.group_name
 
    def test_group_update(self):
        client = APIClient()

        # Create a sample customer
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample group
        group = Group.objects.create(
            group_name='Test Group',
            description='Test Group Description',
            status=True,
            customer_id=customer
        )

        # Update the group
        new_group_name = 'Updated Group Name'
        url = reverse('Group_update', kwargs={'pk': group.pk})
        data = {
            'group_name': new_group_name,
            'description': group.description,
            'status': group.status,
            'customer_id': group.customer_id.pk
        }
        response = client.put(url, data, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['group_name'] == new_group_name

        # Retrieve the updated group from the database
        updated_group = Group.objects.get(pk=group.pk)

        assert updated_group.group_name == new_group_name

    def test_group_list(self):
        client = APIClient()
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create sample groups
        group1 = Group.objects.create(
            group_name='Group 1',
            description='Group 1 Description',
            status=True,
            customer_id=customer
        )
        group2 = Group.objects.create(
            group_name='Group 2',
            description='Group 2 Description',
            status=True,
            customer_id=customer
        )

        url = reverse('Group_list')
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2  # Assert that the response contains the correct number of groups
        assert response.data[0]['group_name'] == group1.group_name
        assert response.data[1]['group_name'] == group2.group_name

    def test_group_delete(self):
        client = APIClient()
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample group
        group = Group.objects.create(
            group_name='Test Group',
            description='Test Group Description',
            status=True,
            customer_id=customer
        )

        url = reverse('Group_delete', kwargs={'pk': group.pk})
        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Group.objects.count() == 0

####################### group role #######################

@pytest.mark.django_db
class TestGroupRoleViews:
    def test_grouprole_create(self):
        client = APIClient()

        # Create a sample customer
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample role
        role = Role.objects.create(
            role_name='ContractManager',
            description='Test Role',
            status=True,
            customer_id=customer
        )

        # Create a sample group
        group = Group.objects.create(
            group_name='Test Group',
            description='Test Group Description',
            status=True,
            customer_id=customer
        )

        data = {
            'group_id': group.pk,
            'role_id': role.pk,
            'status': True,
            'is_group_lead': True
        }

        url = reverse('GroupRole_create')
        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert GroupRole.objects.count() == 1
        assert response.data['group_id'] == group.pk
        assert response.data['role_id'] == role.pk
        assert response.data['status'] == True
        assert response.data['is_group_lead'] == True

    def test_grouprole_retrieve(self):
        client = APIClient()

        # Create a sample customer
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample role
        role = Role.objects.create(
            role_name='ContractManager',
            description='Test Role',
            status=True,
            customer_id=customer
        )

        # Create a sample group
        group = Group.objects.create(
            group_name='Test Group',
            description='Test Group Description',
            status=True,
            customer_id=customer
        )

        # Create a sample GroupRole
        grouprole = GroupRole.objects.create(
            group_id=group,
            role_id=role,
            status=True,
            is_group_lead=True
        )

        url = reverse('GroupRole_retrieve', kwargs={'pk': grouprole.pk})
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['group_id'] == group.pk
        assert response.data['role_id'] == role.pk
        assert response.data['status'] == True
        assert response.data['is_group_lead'] == True

    def test_grouprole_update(self):
        client = APIClient()

        # Create a sample customer
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample role
        role = Role.objects.create(
            role_name='ContractManager',
            description='Test Role',
            status=True,
            customer_id=customer
        )

        # Create a sample group
        group = Group.objects.create(
            group_name='Test Group',
            description='Test Group Description',
            status=True,
            customer_id=customer
        )

        # Create a sample GroupRole
        grouprole = GroupRole.objects.create(
            group_id=group,
            role_id=role,
            status=True,
            is_group_lead=True
        )

        url = reverse('GroupRole_update', kwargs={'pk': grouprole.pk})
        data = {
            'group_id': group.pk,
            'role_id': role.pk,
            'status': False,
            'is_group_lead': False
        }
        response = client.patch(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['group_id'] == group.pk
        assert response.data['role_id'] == role.pk
        assert response.data['status'] == False
        assert response.data['is_group_lead'] == False

        # Retrieve the updated GroupRole from the database
        updated_grouprole = GroupRole.objects.get(pk=grouprole.pk)
        assert updated_grouprole.status == False
        assert updated_grouprole.is_group_lead == False

    def test_grouprole_list(self):
        client = APIClient()

        # Create a sample customer
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample role
        role = Role.objects.create(
            role_name='ContractManager',
            description='Test Role',
            status=True,
            customer_id=customer
        )

        # Create a sample group
        group = Group.objects.create(
            group_name='Test Group',
            description='Test Group Description',
            status=True,
            customer_id=customer
        )

        # Create sample GroupRoles
        grouprole1 = GroupRole.objects.create(
            group_id=group,
            role_id=role,
            status=True,
            is_group_lead=True
        )

        grouprole2 = GroupRole.objects.create(
            group_id=group,
            role_id=role,
            status=True,
            is_group_lead=False
        )

        url = reverse('GroupRole_list')
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

        # Assert the first GroupRole in the response
        assert response.data[0]['group_id'] == group.pk
        assert response.data[0]['role_id'] == role.pk
        assert response.data[0]['status'] == True
        assert response.data[0]['is_group_lead'] == True

        # Assert the second GroupRole in the response
        assert response.data[1]['group_id'] == group.pk
        assert response.data[1]['role_id'] == role.pk
        assert response.data[1]['status'] == True
        assert response.data[1]['is_group_lead'] == False

    def test_grouprole_delete(self):
        client = APIClient()

        # Create a sample customer
        country = Country.objects.create(country='Test Country', status=True)
        image_path = Path(settings.BASE_DIR) / 'company_images'/'Django.png'
        base_dir = settings.BASE_DIR
        absolute_file_path = os.path.join(base_dir, image_path)
        customer = Customer.objects.create(
            company_url= 'https://example-updated.com',
            company_name= 'Test Company',
            company_address = '123 Street',
            contact_number ='1234567890',
            country =country,
            gst_tax_number= '55',
            company_logo_url= 'www.Hello',
            company_image= absolute_file_path,
            contact_name= 'XGays2',
            contact_email= 'Isuru1@gmail.com',
            contact_phone_number= '221613',
            licence_type= 'xyz',
            licence_start_date ='2022-02-13',  
            licence_end_date ='2023-02-13',
            licence_user_quantity= '5',
            status= True,
            is_social_login_enabled =False,
            unique_id= 'ABC123',
            city= 'City Name',
            state ='State Name',
            org_admin_email ='admin@example.com',
            org_admin_full_name ='Admin Name',
            org_admin_contact_number= '9876543210',
            contract_manager_email= 'manager@example.com',
            contract_manager_full_name= 'Manager Name',
            contract_manager_contact_number= '9876543210',
        )

        # Create a sample role
        role = Role.objects.create(
            role_name='ContractManager',
            description='Test Role',
            status=True,
            customer_id=customer
        )

        # Create a sample group
        group = Group.objects.create(
            group_name='Test Group',
            description='Test Group Description',
            status=True,
            customer_id=customer
        )

        # Create a sample group role
        grouprole = GroupRole.objects.create(
            group_id=group,
            role_id=role,
            status=True,
            is_group_lead=True
        )

        url = reverse('GroupRole_delete', kwargs={'pk': grouprole.pk})
        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert GroupRole.objects.count() == 0

####################### user #######################

@pytest.mark.django_db
class TestUserViews:

    def test_user_list_view(self):
        client = APIClient()
        url = reverse('user_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_user_create_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_url='www.elogic.lk',company_name='Test Customer', licence_type='test', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language_code='T001',language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency_code='T001',currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group',description='test description', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role', role_type='ContractManagement', description='test description',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True )
        client = APIClient()
        url = reverse('user_create')
        data = {
            'email': 'test@test.com',
            'status': True,
            'password': 'testpassword',
            'customer_id': customer.customer_id,
            'contact_phone_number': '1234567890',
            'department': 'Test Department',
            'language_id': language.language_id,
            'currency_id': currency.currency_id,
            'date_format_id': date_format.date_format_id,
            'organization_name':'test organization',
            'password_reset_token': 'testtoken',
            'password_reset_token_sent_at': '2022-01-01T00:00:00Z',
            'updated_at':'2022-01-01T00:00:00Z',
            'first_name': 'Test',
            'last_name': 'User',
            'username':'email',
            'groups': [group.group_id],
            'roles': [{'role': role.role_id, 'is_primary': True}],
            'user_permissions': [permission.permission_id],  
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

      
    def test_user_update_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )
        
        client = APIClient()
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id]) 

        url = reverse('user_update', kwargs={'pk': user.pk})
        data = {
            'email': 'updated@test.com',
            'status': True,
            'password': 'testpassword',
            'customer_id': customer.customer_id,
            'contact_phone_number': '1234567890',
            'department': 'Test Department',
            'language_id': language.language_id,
            'currency_id': currency.currency_id,
            'date_format_id': date_format.date_format_id,
            'organization_name':'test organization',
            'password_reset_token': 'testtoken',
            'password_reset_token_sent_at': '2022-01-01T00:00:00Z',
            'updated_at':'2022-01-01T00:00:00Z',
            'first_name': 'Test',
            'last_name': 'User',
            'username':'email',
            'groups': [group.group_id],
            'roles': [{'role': role.role_id, 'is_primary': True}],
            'user_permissions': [permission.permission_id],  
        }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert User.objects.get(pk=user.pk).email == 'updated@test.com'

    def test_user_delete_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )

        client = APIClient()
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])

        url = reverse('user_delete', kwargs={'pk': user.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(User.DoesNotExist):
            User.objects.get(pk=user.pk)

####################### user role #######################

@pytest.mark.django_db
class TestUserRolelViews:

    def test_user_role_list_view(self):
        client = APIClient()
        url = reverse('UserRole_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_user_role_create_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])
        client = APIClient()
        url = reverse('UserRole_create')
        data = {
            'user_id': user.user_id,
            'role_id': role.role_id,
            'status': True,
            'created_at':'2022-01-01T00:00:00Z',
            'updated_at':'2022-12-01T00:00:00Z',
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_user_role_retrieve_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])

        user_role = UserRole.objects.create(
            user_id=user,
            role_id=role,
            status=True,
            created_at='2022-01-01T00:00:00Z',
            updated_at='2022-12-01T00:00:00Z',
        )

        client = APIClient() 
        url = reverse('UserRole_retrieve', args=[user_role.user_role_id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        # assert response.data['first_name'] == 'Test'

    def test_user_role_update_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )
        
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])

        user_role = UserRole.objects.create(
            user_id=user,
            role_id=role,
            status=True,
            created_at='2022-01-01T00:00:00Z',
            updated_at='2022-12-01T00:00:00Z',
        ) 

        url = reverse('UserRole_update', kwargs={'pk': user_role.pk})
        data = {
            'user_id': user.user_id,
            'role_id': role.role_id,
            'status': True,
            'created_at':'2022-01-01T00:00:00Z',
            'updated_at':'2022-12-01T00:00:00Z',
        }
        
        client = APIClient() 
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        # assert User.objects.get(pk=user.pk).email == 'updated@test.com'

    def test_user_role_delete_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )

        client = APIClient()
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])

        user_role = UserRole.objects.create(
            user_id=user,
            role_id=role,
            status=True,
            created_at='2022-01-01T00:00:00Z',
            updated_at='2022-12-01T00:00:00Z',
        ) 

        url = reverse('UserRole_delete', kwargs={'pk': user_role.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(UserRole.DoesNotExist):
            UserRole.objects.get(pk=user_role.pk)

####################### user group #######################

@pytest.mark.django_db
class TestUserRollViews:

    def test_user_group_list_view(self):
        client = APIClient()
        url = reverse('UserGroup_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_user_group_create_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])
        client = APIClient()
        url = reverse('UserGroup_create')
        data = {
            'user_id': user.user_id,
            'group_id': group.group_id,
            'status': True,
            'created_at':'2022-01-01',
            'updated_at':'2022-12-01',
            'is_group_lead':True,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_user_group_retrieve_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])

        user_group = UserGroup.objects.create(
            user_id=user,
            group_id=group,
            status=True,
            created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), 
            updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)),
            is_group_lead=True
        )

        client = APIClient() 
        url = reverse('UserGroup_retrieve', args=[user_group.user_group_id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        # assert response.data['first_name'] == 'Test'

    def test_user_group_update_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )
        
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])

        user_group = UserGroup.objects.create(
            user_id=user,
            group_id=group,
            status=True,
            created_at='2022-01-01T00:00:00Z',
            updated_at='2022-12-01T00:00:00Z',
            is_group_lead=True
        )

        url = reverse('UserGroup_update', kwargs={'pk': user_group.pk})
        data = {
            'user_id': user.user_id,
            'group_id': group.group_id,
            'status': True,
            'created_at':'2022-01-01T00:00:00Z',
            'updated_at':'2022-12-03T00:00:00Z',
            'is_group_lead':True
        }
        client = APIClient() 
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        # assert User.objects.get(pk=user.pk).email == 'updated@test.com'

    def test_user_group_delete_view(self):
        country = Country.objects.create(country='Test Country', status=True)
        customer = Customer.objects.create(company_name='Test Customer', country = country, licence_start_date='2012-12-12',licence_end_date='2015-10-12',licence_user_quantity='4')
        language = Language.objects.create(language='Test Language',status = True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)))
        currency = Currency.objects.create(currency='Test Currency', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)),updated_at=timezone.make_aware(datetime(2022, 2, 20, 0, 0)))
        date_format = DateFormat.objects.create(date_format='Test Date Format',status=True,created_at=timezone.make_aware(datetime(2021, 3, 2, 0, 0)),updated_at=timezone.make_aware(datetime(2023, 1, 3, 0, 0)))
        group = Group.objects.create(group_name='Test Group', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        role = Role.objects.create(role_name='Test Role',status=True,customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
        permission = Permission.objects.create(permission='Test Permission', status=True,created_at='2021-03-02',updated_at='2023-01-03' )

        client = APIClient()
        user = User.objects.create(
            email='test@test.com',
            password='testpassword',
            status=True,
            customer_id=customer,
            first_name='Test',
            last_name='User',
            contact_phone_number='1234567890',
            department='Test Department',
            language_id=language,
            currency_id=currency,
            date_format_id=date_format,
            password_reset_token='testtoken',
            password_reset_token_sent_at='2022-01-01T00:00:00Z',
            updated_at='2022-01-01T00:00:00Z',
        )
        user.groups.set([group.group_id])  
        user.roles.set([role.role_id])  
        user.user_permissions.set([permission.permission_id])

        user_group = UserGroup.objects.create(
            user_id=user,
            group_id=group,
            status=True,
            created_at='2022-01-01T00:00:00Z',
            updated_at='2022-12-01T00:00:00Z',
            is_group_lead=True
        ) 

        url = reverse('UserGroup_delete', kwargs={'pk': user_group.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(UserGroup.DoesNotExist):
            UserGroup.objects.get(pk=user_group.pk)
