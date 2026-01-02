from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from contract.models import (
ContractType,ContractTemplate,ContractStatus,CountryContract,Contract,ContractAttachment,ContractAuthor,ContractCounterparty,ContractHistory
)
from customer_and_user_management.models import (
Customer,User,Language,Currency,DateFormat,Group,Role,Permission,Country
)
from counterparty.models import (
Counterparty
)
import pytest
import os
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from pathlib import Path

########################## ContractType ################################

@pytest.mark.django_db
class TestContractTypeViews:

    def test_contract_type_list_view(self):
        client = APIClient()
        url = reverse('ContractType_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_type_create_view(self):
        client = APIClient()
        url = reverse('ContractType_create')
        data = {
                'contract_type': 'Test Contract type',
                'description': 'Test description',
                'created_at':'2022-02-20',
                'updated_at':'2022-02-20',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_type_retrieve_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractType_oneview', kwargs={'pk': contract_type.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_type_update_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract type', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractType_update', kwargs={'pk': contract_type.pk})
        data = {
                'contract_type': 'Test Updated Contract type',
                'description': 'Test description',
                'created_at': '2022-04-25',
                'updated_at': '2022-05-25',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractType.objects.get(pk=contract_type.pk).contract_type == 'Test Updated Contract type'

    def test_contract_type_delete_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract type', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractType_delete', kwargs={'pk': contract_type.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(ContractType.DoesNotExist):
            ContractType.objects.get(pk=contract_type.pk)

##################  ContractTemplate #################

@pytest.mark.django_db
class TestContractTemplateViews:

    def test_contractTemplate_list_view(self):
        client = APIClient()
        url = reverse('contracttemplate_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contractTemplate_create_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('contracttemplate_create')
        data = {'contract_template_name': 'Test ContractTemplate',
                'contract_template_doc_file_path': 'Test path',
                'qa_template_file_path':'test path',
                'contract_type':contract_type.contract_type_id,
                'created_at':'2021-05-10',
                'updated_at':'2021-10-10',}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contractTemplate_retrieve_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('contracttemplate_oneview', kwargs={'pk': contract_template.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contractTemplate_update_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('contracttemplate_update', kwargs={'pk': contract_template.pk})
        data = {'contract_template_name': 'Test updated ContractTemplate',
                'contract_template_doc_file_path': 'Test path',
                'qa_template_file_path':'test path',
                'contract_type':contract_type.contract_type_id,
                'created_at':'2021-05-10',
                'updated_at':'2021-10-10',}
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractTemplate.objects.get(pk=contract_template.pk).contract_template_name == 'Test updated ContractTemplate'

    def test_contractTemplate_delete_view(self):
        contract_type = ContractType.objects.create(contract_type='Test Contract', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        contract_template = ContractTemplate.objects.create(contract_template_name='Test contract template', contract_template_doc_file_path='Test path', qa_template_file_path='Test path', contract_type = contract_type, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('contracttemplate_delete', kwargs={'pk': contract_template.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_template.DoesNotExist):
            ContractTemplate.objects.get(pk=contract_template.pk)

    ##################  ContractStatus #################

@pytest.mark.django_db
class TestContractStatusViews:

    def test_contractStatus_list_view(self):
        client = APIClient()
        url = reverse('ContractStatus_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contractStatus_create_view(self):
        client = APIClient()
        url = reverse('ContractStatus_create')
        data = {'contract_status': 'Test ContractStatus',
                'description': 'Test description',
                'created_at':'2021-05-10',
                'updated_at':'2021-10-10',}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contractStatus_retrieve_view(self):
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractStatus_oneview', kwargs={'pk': contract_status.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contractStatus_update_view(self):
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractStatus_update', kwargs={'pk': contract_status.pk})
        data = {'contract_status': 'Test updated_Con',
                'description': 'Test description',
                'created_at':'2021-05-10',
                'updated_at':'2021-10-10',}
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractStatus.objects.get(pk=contract_status.pk).contract_status == 'Test updated_Con'

    def test_contractStatus_delete_view(self):
        contract_status = ContractStatus.objects.create(contract_status='Test ContractStatus', description='Test description', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractStatus_delete', kwargs={'pk': contract_status.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_status.DoesNotExist):
            ContractStatus.objects.get(pk=contract_status.pk)

    ##################  country #################

@pytest.mark.django_db
class TestCountryViews:

    def test_country_list_view(self):
        client = APIClient()
        url = reverse('Country_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_country_create_view(self):
        client = APIClient()
        url = reverse('Country_create')
        data = {'country_name': 'Test Country',
                'status': True,
                'created_at':'2021-05-10',
                'updated_at':'2021-10-10',}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_country_retrieve_view(self):
        country = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('Country_oneview', kwargs={'pk': country.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_country_update_view(self):
        country = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('Country_update', kwargs={'pk': country.pk})
        data = {'country_name': 'Test updated Country',
                'status': True,
                'created_at':'2021-05-10',
                'updated_at':'2021-10-10',}
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert CountryContract.objects.get(pk=country.pk).country_name == 'Test updated Country'

    def test_country_delete_view(self):
        country = CountryContract.objects.create(country_name='Test Country', status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('Country_delete', kwargs={'pk': country.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(country.DoesNotExist):
            CountryContract.objects.get(pk=country.pk)

##################  Contract #################

@pytest.mark.django_db
class TestContractViews:

    def test_contract_list_view(self):
        client = APIClient()
        url = reverse('Contract_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_create_view(self):
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
        client = APIClient()
        url = reverse('Contract_create')
        data = {'contract_status': contract_status.contract_status_id,
                'customer': customer.customer_id,
                'created_date':'2022-12-10',
                'created_user':user.user_id,
                'contract_type':contract_type.contract_type_id,
                'contract_manager':user.user_id,
                'expiry_date':'2025-12-10',
                'signed_date':'2020-12-10',
                'last_updated_date': '2021-12-10',
                'country':country_contract.country_id,
                'contract_price':'200',
                'contract_industry':'test contract industry',
                'contract_document_path':'test path',
                'qa_template_file_path':'test path',
                'contract_template':contract_template.contract_template_id,
                'contract_uploaded_source':'test source',
                'meta_tag_document_path':'test path',
                'contract_name':'test_contract_name',
                'created_at':'2021-05-10',
                'updated_at':'2021-10-10',}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_retrieve_view(self):
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
        client = APIClient()
        url = reverse('Contract_oneview', kwargs={'pk': contract.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_update_view(self):
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
        client = APIClient()
        url = reverse('Contract_update', kwargs={'pk': contract.pk})
        data = {'contract_status': contract_status.contract_status_id,
                'customer': customer.customer_id,
                'created_date':'2022-12-10',
                'created_user':user.user_id,
                'contract_type':contract_type.contract_type_id,
                'contract_manager':user.user_id,
                'expiry_date':'2025-12-10',
                'signed_date':'2020-12-10',
                'last_updated_date': '2021-12-10',
                'country':country_contract.country_id,
                'contract_price':'200',
                'contract_industry':'test contract industry',
                'contract_document_path':'test path',
                'qa_template_file_path':'test path',
                'contract_template':contract_template.contract_template_id,
                'contract_uploaded_source':'test source',
                'meta_tag_document_path':'test path',
                'contract_name':'test_updated_contract_name',
                'created_at':'2021-05-10',
                'updated_at':'2021-10-10',}
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Contract.objects.get(pk=contract.pk).contract_name == 'test_updated_contract_name'

    def test_contract_delete_view(self):
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
        client = APIClient()
        url = reverse('Contract_delete', kwargs={'pk': contract.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract.DoesNotExist):
            Contract.objects.get(pk=contract_template.pk)

    def test_contracts_by_status_view(self):
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
        Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name-1', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name-2', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('contracts_by_status', kwargs={'status_id': contract_status.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_all_contract_by_customer_view(self):
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
        Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name-1', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name-2', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('retrieve_all_contract', kwargs={'customer_id': customer.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_all_contract_authors_by_contract_view(self):
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
        contract=Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name-1', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        ContractAuthor.objects.create(user=user, contract= contract, status=True, remarks='test remark 1', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        ContractAuthor.objects.create(user=user, contract= contract, status=True, remarks='test remark 2', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('contract_authors_by_contract', kwargs={'contract_id': contract.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_all_contract_versions_by_contract_view(self):
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
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name-1', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('contract_versions_by_contract', kwargs={'contract_id': contract.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_retrieve_all_contract_attachments_by_contract_view(self):
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
        contract = Contract.objects.create(contract_status=contract_status, customer=customer, created_date=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), created_user=user, contract_type=contract_type, contract_manager=user, expiry_date=timezone.make_aware(datetime(2025, 5, 12, 0, 0)), signed_date=timezone.make_aware(datetime(2022, 5, 12, 0, 0)), last_updated_date=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), country=country_contract, contract_price='300', contract_industry='test industry', contract_document_path='test path', qa_template_file_path ='test path', contract_template = contract_template, contract_uploaded_source='test source', meta_tag_document_path='test path', contract_name='test_contract_name-1', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        ContractAttachment.objects.create(user=user, file_path='Test path',  contract= contract, attachment_name='test name 1', uploaded_date=timezone.make_aware(datetime(2021, 2, 12, 0, 0)))
        ContractAttachment.objects.create(user=user, file_path='Test path',  contract= contract, attachment_name='test name 2', uploaded_date=timezone.make_aware(datetime(2021, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('retrieve_contract_attachments', kwargs={'contract_id': contract.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    

##################  ContractAttachment #################

@pytest.mark.django_db
class TestContractAttachmentViews:

    def test_contract_attachment_list_view(self):
        client = APIClient()
        url = reverse('ContractAttachment_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_attachment_create_view(self):
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
        client = APIClient()
        url = reverse('ContractAttachment_create')
        data = {'user': user.user_id,
                'file_path': 'test path',
                'contract':contract.contract_id,
                'attachment_name':'test name',
                'uploaded_date':'2025-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_attachment_retrieve_view(self):
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
        contract_attachment = ContractAttachment.objects.create(user=user, file_path='Test path',  contract= contract, attachment_name='test name', uploaded_date=timezone.make_aware(datetime(2021, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractAttachment_oneview', kwargs={'pk': contract_attachment.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_attachment_update_view(self):
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
        contract_attachment = ContractAttachment.objects.create(user=user, file_path='Test path',  contract= contract, attachment_name='test name', uploaded_date=timezone.make_aware(datetime(2021, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractAttachment_update', kwargs={'pk': contract_attachment.pk})
        data = {'user': user.user_id,
                'file_path': 'test path',
                'contract':contract.contract_id,
                'attachment_name':'updated test name',
                'uploaded_date':'2025-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractAttachment.objects.get(pk=contract_attachment.pk).attachment_name == 'updated test name'

    def test_contract_attachment_delete_view(self):
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
        contract_attachment = ContractAttachment.objects.create(user=user, file_path='Test path',  contract= contract, attachment_name='test name', uploaded_date=timezone.make_aware(datetime(2021, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractAttachment_delete', kwargs={'pk': contract_attachment.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_attachment.DoesNotExist):
            ContractAttachment.objects.get(pk=contract_attachment.pk)

##################  ContractAuthor #################

@pytest.mark.django_db
class TestContractAuthorViews:

    def test_contract_author_list_view(self):
        client = APIClient()
        url = reverse('ContractAuthor_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_author_create_view(self):
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
        client = APIClient()
        url = reverse('ContractAuthor_create')
        data = {'user': user.user_id,
                'contract':contract.contract_id,
                'file_path': 'test path',
                'status':True,
                'remarks':'test remark',
                'created_at':'2021-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_author_retrieve_view(self):
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
        contract_author = ContractAuthor.objects.create(user=user, contract= contract, status=True, remarks='test remark', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractAuthor_oneview', kwargs={'pk': contract_author.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_author_update_view(self):
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
        contract_author = ContractAuthor.objects.create(user=user, contract= contract, status=True, remarks='test remark', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractAuthor_update', kwargs={'pk': contract_author.pk})
        data = {'user': user.user_id,
                'contract':contract.contract_id,
                'file_path': 'test path',
                'status':True,
                'remarks':'test updated remark',
                'created_at':'2021-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractAuthor.objects.get(pk=contract_author.pk).remarks == 'test updated remark'

    def test_contract_author_delete_view(self):
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
        contract_author = ContractAuthor.objects.create(user=user, contract= contract, status=True, remarks='test remark', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractAuthor_delete', kwargs={'pk': contract_author.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_author.DoesNotExist):
            ContractAuthor.objects.get(pk=contract_author.pk)

##################  ContractCounterparty #################

@pytest.mark.django_db
class TestContractCounterpartyViews:

    def test_contract_counterparty_list_view(self):
        client = APIClient()
        url = reverse('ContractCounterparty_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_counterparty_create_view(self):
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
        counterparty = Counterparty.objects.create(company_name='test company', company_web='test web', company_address='test address', customer=customer, company_contact_number='0772154315', country=country, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        client = APIClient()
        url = reverse('ContractCounterparty_create')
        data = {'counterparty': counterparty.counterparty_id,
                'contract':contract.contract_id,
                'status':True,
                'created_at':'2021-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_counterparty_retrieve_view(self):
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
        counterparty = Counterparty.objects.create(company_name='test company', company_web='test web', company_address='test address', customer=customer, company_contact_number='0772154315', country=country, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        contract_counterparty = ContractCounterparty.objects.create(counterparty=counterparty, contract= contract, status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractCounterparty_oneview', kwargs={'pk': contract_counterparty.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_counterparty_update_view(self):
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
        counterparty = Counterparty.objects.create(company_name='test company', company_web='test web', company_address='test address', customer=customer, company_contact_number='0772154315', country=country, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        contract_counterparty = ContractCounterparty.objects.create(counterparty=counterparty, contract= contract, status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractCounterparty_update', kwargs={'pk': contract_counterparty.pk})
        data = {'counterparty': counterparty.counterparty_id,
                'contract':contract.contract_id,
                'status':True,
                'created_at':'2021-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_counterparty_delete_view(self):
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
        counterparty = Counterparty.objects.create(company_name='test company', company_web='test web', company_address='test address', customer=customer, company_contact_number='0772154315', country=country, created_at=timezone.make_aware(datetime(2021, 4, 20, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 4, 20, 0, 0)))
        contract_counterparty = ContractCounterparty.objects.create(counterparty=counterparty, contract= contract, status=True, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('ContractCounterparty_delete', kwargs={'pk': contract_counterparty.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_counterparty.DoesNotExist):
            ContractCounterparty.objects.get(pk=contract_counterparty.pk)

##################  ContractHistory #################

@pytest.mark.django_db
class TestContractHistoryViews:

    def test_contract_history_list_view(self):
        client = APIClient()
        url = reverse('ContractHistory_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_history_create_view(self):
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
        client = APIClient()
        url = reverse('ContractHistory_create')
        data = {
                'contract':contract.contract_id,
                'version_number': '001',
                'contract_document_path':'test path',
                'created_at':'2021-12-10',
                'updated_at':'2022-12-10',
                'qa_template_file_path':'test path',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_contract_history_retrieve_view(self):
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
        contract_history = ContractHistory.objects.create(contract= contract, version_number='001', contract_document_path='test path', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)), qa_template_file_path='test path')
        client = APIClient()
        url = reverse('ContractHistory_oneview', kwargs={'pk': contract_history.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_contract_history_update_view(self):
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
        contract_history = ContractHistory.objects.create(contract= contract, version_number='001', contract_document_path='test path', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)), qa_template_file_path='test path')
        client = APIClient()
        url = reverse('ContractHistory_update', kwargs={'pk': contract_history.pk})
        data = {
                'contract':contract.contract_id,
                'version_number': '001',
                'contract_document_path':'test updated path',
                'created_at':'2021-12-10',
                'updated_at':'2022-12-10',
                'qa_template_file_path':'test path',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert ContractHistory.objects.get(pk=contract_history.pk).contract_document_path == 'test updated path'

    def test_contract_history_delete_view(self):
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
        contract_history = ContractHistory.objects.create(contract= contract, version_number='001', contract_document_path='test path', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)), qa_template_file_path='test path')
        client = APIClient()
        url = reverse('ContractHistory_delete', kwargs={'pk': contract_history.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(contract_history.DoesNotExist):
            ContractHistory.objects.get(pk=contract_history.pk)
