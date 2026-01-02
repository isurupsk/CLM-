from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contract.models import (
ContractType,ContractTemplate,ContractStatus,CountryContract,Contract
)
from customer_and_user_management.models import (
Customer,User,Language,Currency,DateFormat,Group,Role,Permission,Country
)
from contract_renew.models import (
UploadContract,RenewContract,UploadedContractStatus
)

import pytest
import os
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import urllib.request
from django.contrib.staticfiles import finders
from pathlib import Path

##################  UploadContract #################

@pytest.mark.django_db
class TestUploadContractViews:

    def test_upload_contract_list_view(self):
        client = APIClient()
        url = reverse('UploadContract_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_upload_contract_create_view(self):
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        folder_name = 'company_images'
        folder_path = Path(settings.BASE_DIR) / folder_name
        if folder_path.exists() and folder_path.is_dir():
            print(f"The '{folder_name}' folder is located at: {folder_path}")
        else:
            print(f"The '{folder_name}' folder was not found.")
         # Specify the image URL
        image_url = 'https://files.dimagi.com/wp-content/uploads/2016/01/Django.png'
        # Get the base directory of the Django project
        base_dir = settings.BASE_DIR
        # Construct the absolute path to the folder
        absolute_folder_path = os.path.join(base_dir, folder_path)
        # Create the folder if it doesn't exist
        os.makedirs(absolute_folder_path, exist_ok=True)
        # Extract the image file name from the URL
        file_name = os.path.basename(image_url)
        # Construct the absolute path to save the image
        absolute_file_path = os.path.join(absolute_folder_path, file_name)
        # Download the image from the URL and save it
        urllib.request.urlretrieve(image_url, absolute_file_path)
        # Print the path of the downloaded image
        print(f"The image is downloaded and saved at: {absolute_file_path}")
        customer = Customer.objects.create(
        company_url= 'https://example-updated.com',
        company_name= 'Test Company',
        company_address = '123 Street',
        contact_number ='1234567890',
        country =country,
        gst_tax_number= '55',
        company_logo_url= 'www.Hello',
        company_image=  absolute_file_path,
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
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('UploadContract_create')
        data = {
                'uploaded_user':user.user_id,
                'uploaded_contract_state':contract_status.contract_status_id,
                'contract':contract.contract_id,
                'uploaded_date':'2020-12-10',
                'contract_source_type':'test source',
                'contract_source_address':'test address',
                'contract_destination_address':'test address',
                'contract_upload_status':'test state',
                'contract_upload_filure_reasons':'test reason',
                'metadata_source_type':'test source',
                'metadata_source_address':'test source',
                'metadata_destination_address':'test address',
                'metadata_upload_status':'test status',
                'metadata_upload_filure_reasons':'test reason',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_upload_contract_retrieve_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
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
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        upload_contract = UploadContract.objects.create(uploaded_user=user, uploaded_contract_state=contract_status, contract=contract, uploaded_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), contract_source_type='test source type', contract_source_address='test address', contract_destination_address='test address', contract_upload_status='test status', contract_upload_filure_reasons='test reason', metadata_source_type='test source type', metadata_source_address='test address', metadata_destination_address='test address', metadata_upload_status='test status', metadata_upload_filure_reasons='test reason')
        client = APIClient()
        url = reverse('UploadContract_retrieve', kwargs={'pk': upload_contract.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_upload_contract_update_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
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
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        upload_contract = UploadContract.objects.create(uploaded_user=user, uploaded_contract_state=contract_status, contract=contract, uploaded_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), contract_source_type='test source type', contract_source_address='test address', contract_destination_address='test address', contract_upload_status='test status', contract_upload_filure_reasons='test reason', metadata_source_type='test source type', metadata_source_address='test address', metadata_destination_address='test address', metadata_upload_status='test status', metadata_upload_filure_reasons='test reason')
        client = APIClient()
        url = reverse('UploadContract_update', kwargs={'pk': upload_contract.pk})
        data = {
                'uploaded_user':user.user_id,
                'uploaded_contract_state':contract_status.contract_status_id,
                'contract':contract.contract_id,
                'uploaded_date':'2020-12-10',
                'contract_source_type':'test source',
                'contract_source_address':'updated test address',
                'contract_destination_address':'test address',
                'contract_upload_status':'test state',
                'contract_upload_filure_reasons':'test reason',
                'metadata_source_type':'test source',
                'metadata_source_address':'test source',
                'metadata_destination_address':'test address',
                'metadata_upload_status':'test status',
                'metadata_upload_filure_reasons':'test reason',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert UploadContract.objects.get(pk=upload_contract.pk).contract_source_address == 'updated test address'

    def test_upload_contract_delete_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
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
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        upload_contract = UploadContract.objects.create(uploaded_user=user, uploaded_contract_state=contract_status, contract=contract, uploaded_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), contract_source_type='test source type', contract_source_address='test address', contract_destination_address='test address', contract_upload_status='test status', contract_upload_filure_reasons='test reason', metadata_source_type='test source type', metadata_source_address='test address', metadata_destination_address='test address', metadata_upload_status='test status', metadata_upload_filure_reasons='test reason')
        client = APIClient()
        url = reverse('UploadContract_delete', kwargs={'pk': upload_contract.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(upload_contract.DoesNotExist):
            UploadContract.objects.get(pk=upload_contract.pk)

##################  RenewContract #################

@pytest.mark.django_db
class TestRenewContractViews:

    def test_renew_contract_list_view(self):
        client = APIClient()
        url = reverse('RenewContract_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_renew_contract_create_view(self):
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
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
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('RenewContract_create')
        data = {
                'renewed_user_id':user.user_id,
                'uploaded_contract_state':contract_status.contract_status_id,
                'renewed_data':'2020-12-10',
                'contract_id':contract.contract_id,
                'remarks':'test remarks',
                'customer_id':customer.customer_id,
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_renew_contract_retrieve_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
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
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        renew_contract = RenewContract.objects.create(renewed_user_id=user, renewed_data=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), contract_id=contract, remarks='test remarks', customer_id=customer)
        client = APIClient()
        url = reverse('RenewContract_retrieve', kwargs={'pk': renew_contract.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_renew_contract_update_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
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
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        renew_contract = RenewContract.objects.create(renewed_user_id=user, renewed_data=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), contract_id=contract, remarks='test remarks', customer_id=customer)
        client = APIClient()
        url = reverse('RenewContract_update', kwargs={'pk': renew_contract.pk})
        data = {
                'renewed_user_id':user.user_id,
                'uploaded_contract_state':contract_status.contract_status_id,
                'renewed_data':'2020-12-10',
                'contract_id':contract.contract_id,
                'remarks':'updated test remarks',
                'customer_id':customer.customer_id,
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert RenewContract.objects.get(pk=renew_contract.pk).remarks == 'updated test remarks'

    def test_renew_contract_delete_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
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
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        renew_contract = RenewContract.objects.create(renewed_user_id=user, renewed_data=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), contract_id=contract, remarks='test remarks', customer_id=customer)
        client = APIClient()
        url = reverse('RenewContract_delete', kwargs={'pk': renew_contract.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(renew_contract.DoesNotExist):
            RenewContract.objects.get(pk=renew_contract.pk)

##################  UploadedContractStatus #################

@pytest.mark.django_db
class TestUploadedContractStatustViews:

    def test_uploaded_contract_status_list_view(self):
        client = APIClient()
        url = reverse('UploadedContractStatus_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_uploaded_contract_status_create_view(self):
        client = APIClient()
        url = reverse('UploadedContractStatus_create')
        data = {
                'uploaded_contract_state':'test status',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_uploaded_contract_status_retrieve_view(self):
        uploaded_contract_status = UploadedContractStatus.objects.create(uploaded_contract_state='Test state')
        url = reverse('UploadedContractStatus_retrieve', kwargs={'pk': uploaded_contract_status.pk})
        client = APIClient()
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_uploaded_contract_status_update_view(self):
        uploaded_contract_status = UploadedContractStatus.objects.create(uploaded_contract_state='Test state')
        client = APIClient()
        url = reverse('UploadedContractStatus_update', kwargs={'pk': uploaded_contract_status.pk})
        data = {
                'uploaded_contract_state':'test updated status',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert UploadedContractStatus.objects.get(pk=uploaded_contract_status.pk).uploaded_contract_state == 'test updated status'

    def test_renew_contract_delete_view(self):
        uploaded_contract_status = UploadedContractStatus.objects.create(uploaded_contract_state='Test state')
        client = APIClient()
        url = reverse('UploadedContractStatus_delete', kwargs={'pk': uploaded_contract_status.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(uploaded_contract_status.DoesNotExist):
            UploadedContractStatus.objects.get(pk=uploaded_contract_status.pk)