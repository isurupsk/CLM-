from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from customer_and_user_management.models import (
Customer,Country
)
from lables.models import (
LabelMaster
)
import pytest
import os
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from pathlib import Path

##################  LabelMaster #################
@pytest.mark.django_db
class TestLabelMasterViews:
    def test_labels_by_customer_view(self):
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
            LabelMaster.objects.create(label='Test label1',description = 'Test description',status=True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)),customer=customer)
            LabelMaster.objects.create(label='Test label2',description = 'Test description',status=True, created_at=timezone.make_aware(datetime(2023, 2, 12, 0, 0)), updated_at=timezone.make_aware(datetime(2023, 4, 12, 0, 0)),customer=customer)
            client = APIClient()
            url = reverse('labels_by_customer', kwargs={'customer_id': customer.pk})
            response = client.get(url)
            assert response.status_code == status.HTTP_200_OK
