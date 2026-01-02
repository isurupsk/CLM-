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
from contract_review_approval.models import (
ContractReviewer,ContractActivityLog,ContractApprover,ContractMetadata,Metadata
)
import pytest
import os
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import urllib.request
from pathlib import Path

##################  ContractReviewer #################

@pytest.mark.django_db
class TestContractReviewerViews:

    def test_contract_reviewer_list_view(self):
        client = APIClient()
        url = reverse('ContractReviewer_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_reviewer_create_view(self):
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        country = Country.objects.create(country='Test Country', status=True)
        country_contract = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        folder_name = 'company_images'
        image_name = 'Django.png'
        image_path = os.path.join(settings.BASE_DIR, folder_name, image_name)
        customer = Customer.objects.create(
        company_url= 'https://example-updated.com',
        company_name= 'Test Company',
        company_address = '123 Street',
        contact_number ='1234567890',
        country =country,
        gst_tax_number= '55',
        company_logo_url= 'www.Hello',
        company_image= image_path,
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
        url = reverse('ContractReviewer_create')
        data = {
                'user_id':user.user_id,
                'review_status':'1',
                'contract_id':contract.contract_id,
                'review_order':'1',
                'internal_or_external':'internal',
                'remarks':'test remarks',
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_reviewer_retrieve_view(self):
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
        contract_reviewer = ContractReviewer.objects.create(user_id=user, review_status=1, contract_id=contract, review_order=1, internal_or_external='internal', remarks='test remarks', created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('ContractReviewer_retrieve', kwargs={'pk': contract_reviewer.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_reviewer_update_view(self):
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
        contract_reviewer = ContractReviewer.objects.create(user_id=user, review_status=1, contract_id=contract, review_order=1, internal_or_external='internal', remarks='test remarks', created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('ContractReviewer_update', kwargs={'pk': contract_reviewer.pk})
        data = {
                'user_id':user.user_id,
                'review_status':'1',
                'contract_id':contract.contract_id,
                'review_order':'1',
                'internal_or_external':'external',
                'remarks':'test remarks',
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractReviewer.objects.get(pk=contract_reviewer.pk).internal_or_external == 'external'

    def test_contract_reviewer_delete_view(self):
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
        contract_reviewer = ContractReviewer.objects.create(user_id=user, review_status=1, contract_id=contract, review_order=1, internal_or_external='internal', remarks='test remarks', created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('ContractReviewer_delete', kwargs={'pk': contract_reviewer.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_reviewer.DoesNotExist):
            ContractReviewer.objects.get(pk=contract_reviewer.pk)

##################  ContractActivityLog #################

@pytest.mark.django_db
class TestContractActivityLogViews:

    def test_contract_activity_log_list_view(self):
        client = APIClient()
        url = reverse('ContractActivityLog_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_activity_log_create_view(self):
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
        url = reverse('ContractActivityLog_create')
        data = {
                'user_id':user.user_id,
                'activity':'test activity',
                'activity_time':'2019-12-10',
                'contract_id':contract.contract_id,
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                'customer_id':customer.customer_id,
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_activity_log_retrieve_view(self):
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
        contract_activity = ContractActivityLog.objects.create(user_id=user, activity='test activity', activity_time=timezone.make_aware(datetime(2019, 4, 20, 0, 0)), contract_id=contract, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)), customer_id=customer)
        client = APIClient()
        url = reverse('ContractActivityLog_retrieve', kwargs={'pk': contract_activity.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_activity_log_update_view(self):
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
        contract_activity = ContractActivityLog.objects.create(user_id=user, activity='test activity', activity_time=timezone.make_aware(datetime(2019, 4, 20, 0, 0)), contract_id=contract, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)), customer_id=customer)
        client = APIClient()
        url = reverse('ContractActivityLog_update', kwargs={'pk': contract_activity.pk})
        data = {
                'user_id':user.user_id,
                'activity':'updated test activity',
                'activity_time':'2019-12-10',
                'contract_id':contract.contract_id,
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                'customer_id':customer.customer_id,
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractActivityLog.objects.get(pk= contract_activity.pk).activity == 'updated test activity'

    def test_contract_activity_log_delete_view(self):
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
        contract_activity = ContractActivityLog.objects.create(user_id=user, activity='test activity', activity_time=timezone.make_aware(datetime(2019, 4, 20, 0, 0)), contract_id=contract, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)), customer_id=customer)
        client = APIClient()
        url = reverse('ContractActivityLog_delete', kwargs={'pk': contract_activity.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_activity.DoesNotExist):
            ContractActivityLog.objects.get(pk=contract_activity.pk)

##################  ContractApprover #################

@pytest.mark.django_db
class TestContractApproverViews:

    def test_contract_approver_list_view(self):
        client = APIClient()
        url = reverse('ContractApprover_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_approver_create_view(self):
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
        url = reverse('ContractApprover_create')
        data = {
                'user_id':user.user_id,
                'contract_id':contract.contract_id,
                'review_order':'1',
                'approve_status':'1',
                'internal_or_external':'internal',
                'remarks':'test remarks',
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_approver_retrieve_view(self):
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
        contract_approver = ContractApprover.objects.create(user_id=user, contract_id=contract, review_order=1, approve_status=1, internal_or_external='internal', remarks='test remarks', created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('ContractApprover_retrieve', kwargs={'pk': contract_approver.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_all_contract_approver_retrieve_view(self):
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
        ContractApprover.objects.create(user_id=user, contract_id=contract, review_order=1, approve_status=1, internal_or_external='internal', remarks='test remarks', created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('retrieve_all_contract_approvers', kwargs={'contract_id': contract.contract_id})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_approver_update_view(self):
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
        contract_approver = ContractApprover.objects.create(user_id=user, contract_id=contract, review_order=1, approve_status=1, internal_or_external='internal', remarks='test remarks', created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('ContractApprover_update', kwargs={'pk': contract_approver.pk})
        data = {
                'user_id':user.user_id,
                'contract_id':contract.contract_id,
                'review_order':'1',
                'approve_status':'1',
                'internal_or_external':'internal',
                'remarks':'test updated remarks',
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractApprover.objects.get(pk= contract_approver.pk).remarks == 'test updated remarks'

    def test_contract_approver_delete_view(self):
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
        contract_approver = ContractApprover.objects.create(user_id=user, contract_id=contract, review_order=1, approve_status=1, internal_or_external='internal', remarks='test remarks', created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('ContractApprover_delete', kwargs={'pk': contract_approver.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_approver.DoesNotExist):
            ContractApprover.objects.get(pk=contract_approver.pk)

##################  Metadata #################

@pytest.mark.django_db
class TestMetadataViews:

    def test_metadata_list_view(self):
        client = APIClient()
        url = reverse('Metadata_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_metadata_create_view(self):
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
        url = reverse('Metadata_create')
        data = {
                'metadata_key':'test key',
                'created_date':'2020-12-10',
                'created_by_user_id':'1',
                'customer_id':customer.customer_id,
                'created_at':'2020-12-10',
                'updated_at':'2020-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_metadata_retrieve_view(self):
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('Metadata_retrieve', kwargs={'pk': meta_data.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_meta_data_update_view(self):
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('Metadata_update', kwargs={'pk': meta_data.pk})
        data = {
                'metadata_key':'test updated key',
                'created_date':'2020-12-10',
                'created_by_user_id':'1',
                'customer_id':customer.customer_id,
                'created_at':'2020-12-10',
                'updated_at':'2020-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Metadata.objects.get(pk= meta_data.pk).metadata_key == 'test updated key'

    def test_meta_data_delete_view(self):
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('Metadata_delete', kwargs={'pk': meta_data.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(meta_data.DoesNotExist):
            Metadata.objects.get(pk=meta_data.pk)

    def test_additional_metadata_create_view(self):
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
        url = reverse('create_additional_meta_tag')
        data = {
                'metadata_key':'test key',
                'created_date':'2020-12-10',
                'created_by_user_id':'1',
                'customer_id':customer.customer_id,
                'created_at':'2020-12-10',
                'updated_at':'2020-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_additional_meta_tag_contract_create_view(self):
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('add_additional_meta_tag_to_contract')
        data = {
                'metadata_id':meta_data.metadata_id,
                'contract_id':contract.contract_id,
                'added_by_user_id':user.user_id,
                'created_at':'2020-12-10',
                'updated_at':'2020-12-10',
                'metadata_value':'test metadata value',
                'additional_meta_tag_id':'test additional meta tag',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

##################  ContractMetadata #################

@pytest.mark.django_db
class TestContractMetadataViews:

    def test_contract_metadata_list_view(self):
        client = APIClient()
        url = reverse('ContractMetadata_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_metadata_create_view(self):
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('ContractMetadata_create')
        data = {
                'metadata_id':meta_data.metadata_id,
                'contract_id':contract.contract_id,
                'added_by_user_id':user.user_id,
                'created_at':'2020-12-10',
                'updated_at':'2020-12-10',
                'metadata_value':'test metadata value',
                'additional_meta_tag_id':'test additional meta tag',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_metadata_retrieve_view(self):
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        contract_meta_data = ContractMetadata.objects.create(metadata_id=meta_data, contract_id=contract, added_by_user_id=user, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)), metadata_value='test value', additional_meta_tag_id='test additional meta tag')
        client = APIClient()
        url = reverse('ContractMetadata_retrieve', kwargs={'pk': contract_meta_data.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_metadata_update_view(self):
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        contract_meta_data = ContractMetadata.objects.create(metadata_id=meta_data, contract_id=contract, added_by_user_id=user, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)), metadata_value='test value', additional_meta_tag_id='test additional meta tag')
        client = APIClient()
        url = reverse('ContractMetadata_update', kwargs={'pk': contract_meta_data.pk})
        data = {
                'metadata_id':meta_data.metadata_id,
                'contract_id':contract.contract_id,
                'added_by_user_id':user.user_id,
                'created_at':'2020-12-10',
                'updated_at':'2020-12-10',
                'metadata_value':'test updated metadata value',
                'additional_meta_tag_id':'test additional meta tag',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractMetadata.objects.get(pk= contract_meta_data.pk).metadata_value == 'test updated metadata value'

    def test_contract_metadata_delete_view(self):
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        contract_meta_data = ContractMetadata.objects.create(metadata_id=meta_data, contract_id=contract, added_by_user_id=user, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)), metadata_value='test value', additional_meta_tag_id='test additional meta tag')
        client = APIClient()
        url = reverse('ContractMetadata_delete', kwargs={'pk': contract_meta_data.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_meta_data.DoesNotExist):
            ContractMetadata.objects.get(pk=contract_meta_data.pk)

    def test_all_additonal_meta_tag_retrieve_view(self):
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
        role = Role.objects.create(role_name='Test Role', status=True, customer_id=customer,created_at='2021-03-02',updated_at='2023-01-03')
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
        meta_data = Metadata.objects.create(metadata_key='test key', created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_by_user_id=1, customer_id=customer, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        ContractMetadata.objects.create(metadata_id=meta_data, contract_id=contract, added_by_user_id=user, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)), metadata_value='test value', additional_meta_tag_id='test additional meta tag')
        client = APIClient()
        url = reverse('retrieve_all_additional_meta_tag', kwargs={'customer_id': customer.customer_id, 'contract_id': contract.contract_id})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK