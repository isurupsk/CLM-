from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from customer_and_user_management.models import (
Customer,User,Language,Currency,DateFormat,Group,Role,Permission,Country
)
from counterparty.models import (
Counterparty,CounterpartyContact,CustomerCounterpartyContact
)
import pytest
import os
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from pathlib import Path

##################  Counterparty #################

@pytest.mark.django_db
class TestCounterpartyViews:

    def test_counterparty_list_view(self):
        client = APIClient()
        url = reverse('Counterparty_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_counterparty_create_view(self):
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
        client = APIClient()
        url = reverse('Counterparty_create')
        data = {
                'company_name':'test company',
                'company_web':'test web',
                'company_address':'test address',
                'customer':customer.customer_id,
                'company_contact_number':'0775421365',
                'city':'test city',
                'country':country.country_id,
                'contact_name':'test name',
                'email':'test@gmail.com',
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_counterparty_retrieve_view(self):
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
        counerparty = Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('Counterparty_retrieve', kwargs={'pk': counerparty.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_counterparty_update_view(self):
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
        counerparty = Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('Counterparty_update', kwargs={'pk': counerparty.pk})
        data = {
                'company_name':'test updated company',
                'company_web':'test web',
                'company_address':'test address',
                'customer':customer.customer_id,
                'company_contact_number':'0775421365',
                'city':'test city',
                'country':country.country_id,
                'contact_name':'test name',
                'email':'test@gmail.com',
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Counterparty.objects.get(pk=counerparty.pk).company_name == 'test updated company'

    def test_counterparty_delete_view(self):
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
        counerparty = Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('Counterparty_delete', kwargs={'pk': counerparty.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(counerparty.DoesNotExist):
            Counterparty.objects.get(pk=counerparty.pk)

    def test_counterparties_by_customer_view(self):
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
            Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
            Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
            client = APIClient()
            url = reverse('counterparties_by_customer', kwargs={'customer_id': customer.customer_id})
            response = client.get(url)
            assert response.status_code == status.HTTP_200_OK

##################  CounterpartyContract #################

@pytest.mark.django_db
class TestCounterpartyContractViews:

    def test_counterparty_contract_list_view(self):
        client = APIClient()
        url = reverse('CounterpartyContract_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_counterparty_contract_create_view(self):
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
        counterparty=Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('CounterpartyContract_create')
        data = {
                'counterparty_id':counterparty.counterparty_id,
                'user_id':user.user_id,
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_counterparty_contract_retrieve_view(self):
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
        counterparty=Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        counterparty_contract=CounterpartyContact.objects.create(counterparty_id=counterparty, user_id=user, is_primary=False, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('CounterpartyContract_retrieve', kwargs={'pk': counterparty_contract.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_counterparty_contract_update_view(self):
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
        counterparty=Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        counterparty_contract=CounterpartyContact.objects.create(counterparty_id=counterparty, is_primary=False, user_id=user, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('CounterpartyContract_update', kwargs={'pk': counterparty_contract.pk})
        data = {
                'counterparty_id':counterparty.counterparty_id,
                'user_id':user.user_id,
                'is_primary':False,
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        # assert CounterpartyContact.objects.get(pk=counterparty_contract.pk).internal_or_external == 'external'

    def test_contract_delete_view(self):
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
        counterparty=Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        counterparty_contract=CounterpartyContact.objects.create(counterparty_id=counterparty, user_id=user,is_primary=False, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('CounterpartyContract_delete', kwargs={'pk': counterparty_contract.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(counterparty_contract.DoesNotExist):
            CounterpartyContact.objects.get(pk=counterparty_contract.pk)

##################  CustomerCounterpartyContact #################

@pytest.mark.django_db
class TestCustomerCounterpartyContactViews:

    def test_customer_counterparty_contract_list_view(self):
        client = APIClient()
        url = reverse('CustomerCounterpartyContact_list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_customer_counterparty_contract_create_view(self):
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
        counterparty=Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        counterparty_contract=CounterpartyContact.objects.create(counterparty_id=counterparty, is_primary=False, user_id=user, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('CustomerCounterpartyContact_create')
        data = {
                'customer_id':customer.customer_id,
                'counterparty_contact_id':counterparty_contract.counterparty_contact_id,
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_customer_counterparty_contract_retrieve_view(self):
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
        counterparty=Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        counterparty_contract=CounterpartyContact.objects.create(counterparty_id=counterparty, user_id=user, is_primary=False, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        customer_counterparty_contract=CustomerCounterpartyContact.objects.create(customer_id=customer, counterparty_contact_id=counterparty_contract, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('CustomerCounterpartyContact_retrieve', kwargs={'pk': customer_counterparty_contract.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_customer_counterparty_contract_update_view(self):
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
        counterparty=Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        counterparty_contract=CounterpartyContact.objects.create(counterparty_id=counterparty, is_primary=False, user_id=user, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        customer_counterparty_contract=CustomerCounterpartyContact.objects.create(customer_id=customer, counterparty_contact_id=counterparty_contract, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('CustomerCounterpartyContact_update', kwargs={'pk': customer_counterparty_contract.pk})
        data = {
                'customer_id':customer.customer_id,
                'counterparty_contact_id':counterparty_contract.counterparty_contact_id,
                'created_at':'2020-12-10',
                'updated_at':'2022-12-10',
                }
        response = client.put(url, data)
        assert response.status_code == status.HTTP_200_OK
        # assert ContractReviewer.objects.get(pk=contract_reviewer.pk).internal_or_external == 'external'

    def test_customer_counterparty_contract_delete_view(self):
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
        counterparty=Counterparty.objects.create(company_name='test company name', country=country, company_web='test web', company_address='test address', customer=customer, company_contact_number='0775486321', created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        counterparty_contract=CounterpartyContact.objects.create(counterparty_id=counterparty, is_primary=False, user_id=user, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        customer_counterparty_contract=CustomerCounterpartyContact.objects.create(customer_id=customer, counterparty_contact_id=counterparty_contract, created_at=timezone.make_aware(datetime(2021, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2022, 2, 12, 0, 0)))
        client = APIClient()
        url = reverse('CustomerCounterpartyContact_delete', kwargs={'pk': customer_counterparty_contract.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        with pytest.raises(customer_counterparty_contract.DoesNotExist):
            CustomerCounterpartyContact.objects.get(pk=customer_counterparty_contract.pk)