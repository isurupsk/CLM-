

-- Language Table 

INSERT INTO master_data_language (language_id, language_code, language, status, created_at, updated_at)
VALUES
  (6, 'en', 'English', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  (2, 'fr', 'French', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  (3, 'es', 'Spanish', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  (4, 'de', 'German', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  (5, 'ja', 'Japanese', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

 


-- Date 

INSERT INTO master_data_dateformat (date_format_id, date_format, status, created_at, updated_at)
VALUES
  (5, 'YYYY-MM-DD', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  (2, 'MM/DD/YYYY', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  (3, 'DD/MM/YYYY', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
  (4, 'YYYY/MM/DD', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


-- Contract_status

INSERT INTO contract_status (contract_status_id, description, contract_status, created_at, updated_at)
VALUES
    (1, 'When a contract is first created. Contract review process has started but both of these two tasks are NOT completed.', 'Draft', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (2, 'Pending Review', 'Pending Review', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (3, 'Approval process started but contract is not approved by all assigned approvers.', 'Pending Approval', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (4, 'Contract is signed. This state means every approver has approved and signed the contract.', 'Signed', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (5, 'Contract is signed and the contract is currently in "Active" state.', 'Active', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (6, 'Contract is expired.', 'Expired', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (7, 'Contract is cancelled/terminated before it expires.', 'Cancelled', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);



-- Currency

INSERT INTO master_data_currency (currency_id, currency_code, currency, status, created_at, updated_at)
VALUES
    (2, 'EUR', 'Euro', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (3, 'GBP', 'British Pound', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (4, 'JPY', 'Japanese Yen', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (5, 'AUD', 'Australian Dollar', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (6, 'LKR', 'Sri Lankan Rupee', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (7, 'INR', 'Indian Rupee', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (9, 'USD', 'US Dollar', true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

 
--  Role Sample SQL Query 

INSERT INTO customer_and_user_management_role (role_name, role_type, description, status, created_at, updated_at)
VALUES
    ('Create contract','ContractManagement','Allows user to create contracts', true, NOW(), NOW()),
    ('Contract Manager', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('View Contract', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Review Contract', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Approve Contract', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Collaborate Contract', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Sign Contract', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Share Contract', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Download Contract - PR Execution', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Download Contract - Po Execution', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Upload Contract', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('View Analytics', 'ContractManagement', 'Allows user to create contracts', true, NOW(), NOW());

INSERT INTO customer_and_user_management_role (role_name, role_type, description, status, created_at, updated_at)
VALUES
    ('ORG Admin', 'OperationalManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Add Edit Member', 'OperationalManagement', 'Allows user to create contracts', true, NOW(), NOW()),    
    ('Add Edit Team', 'OperationalManagement', 'Allows user to create contracts', true, NOW(), NOW()),   
    ('Edit Contract Settings', 'OperationalManagement', 'Allows user to create contracts', true, NOW(), NOW()),
    ('Manage Integrations', 'OperationalManagement', 'Allows user to create contracts', true, NOW(), NOW());



-- Contract Type 

INSERT INTO contract_contracttype (contract_type, description, created_at, updated_at)
VALUES
    ('House Rental Agreement', 'Agreement for renting a house', NOW(), NOW()),
    ('Partnership Agreement', 'Agreement between partners', NOW(), NOW()),
    ('Consulting Agreement', 'Agreement for consulting services', NOW(), NOW()),
    ('Non-Disclosure Agreement', 'Agreement to protect confidential information', NOW(), NOW()),
    ('Employment Agreement', 'Agreement between employer and employee', NOW(), NOW()),
    ('Sales Agreement', 'Agreement for sales of goods or services', NOW(), NOW()),
    ('Loan Agreement', 'Agreement for lending or borrowing money', NOW(), NOW()),
    ('Divorce Settlement Agreement', 'Agreement to settle terms of divorce', NOW(), NOW()),
    ('End User License Agreement', 'Agreement for software or application usage', NOW(), NOW()),
    ('Master Service Agreement', 'Agreement for comprehensive services', NOW(), NOW());


--  permission
INSERT INTO customer_and_user_management_permission (permission, status, created_at, updated_at)
VALUES
    ('Contract Creation', true, NOW(), NOW()),
    ('Contract Editing', true, NOW(), NOW()),
    ('Contract Viewing', true, NOW(), NOW()),
    ('Contract Reviewing', true, NOW(), NOW()),
    ('Contract Approval/Signing', true, NOW(), NOW()),
    ('Contract Download', true, NOW(), NOW()),
    ('Contract Upload', true, NOW(), NOW()),
    ('Contract Search', true, NOW(), NOW()),
    ('To Do List Creation', true, NOW(), NOW()),
    ('To Do List Viewing', true, NOW(), NOW()),
    ('Analytics Report Creation', true, NOW(), NOW()),
    ('Analytics Report Viewing', true, NOW(), NOW()),
    ('Analytics Report Download', true, NOW(), NOW()),
    ('User Creation', true, NOW(), NOW()),
    ('User Update', true, NOW(), NOW()),
    ('User Deletion', true, NOW(), NOW()),
    ('Password Change', true, NOW(), NOW());


-- Country 

INSERT INTO contract_country (country_name, status, created_at, updated_at)
VALUES
    ('India', true, NOW(), NOW()),
    ('United State', true, NOW(), NOW()),
    ('Algeria', true, NOW(), NOW()),
    ('Andorra', true, NOW(), NOW()),
    ('Angola', true, NOW(), NOW()),
    ('Antigua and Barbuda', true, NOW(), NOW()),
    ('Argentina', true, NOW(), NOW()),
    ('Armenia', true, NOW(), NOW()),
    ('Australia', true, NOW(), NOW()),
    ('Austria', true, NOW(), NOW()),
    ('Azerbaijan', true, NOW(), NOW()),
    ('Bahamas', true, NOW(), NOW()),
    ('Bahrain', true, NOW(), NOW()),
    ('Bangladesh', true, NOW(), NOW()),
    ('Barbados', true, NOW(), NOW()),
    ('Belarus', true, NOW(), NOW()),
    ('Belgium', true, NOW(), NOW()),
    ('Belize', true, NOW(), NOW()),
    ('Benin', true, NOW(), NOW()),
    ('Bhutan', true, NOW(), NOW());


-- password_policy
INSERT INTO password_policy_passwordpolicyrule (password_policy_rule_id, possword_policy_rule, answer_type, possible_answers, status)
VALUES
    (10, 'Must have at least one English uppercase character (A-Z)', 'string', 'A-Z', true),
    (11, 'Must have at least one English lowercase character (a-z)', 'string', 'a-z', true),
    (12, 'Must have at least one number (0-9)', 'numeric', '0-9', true),
    (13, 'Must have at least one symbol (such as !, #, or %)', 'string', '!#%', true),
    (14, 'Must have Ten or more characters total', 'string', '>=10', true),
    (15, 'Don''t allow alphabet sequence', 'boolean', 'True', true),
    (16, 'Don''t allow digit sequence', 'boolean', 'True', true),
    (17, 'Don''t allow last three passwords (during password change)', 'boolean', 'True', true),
    (18, 'Don''t require mandatory periodic password resets for user accounts', 'boolean', 'True', true),
    (19, 'Limit three wrong password attempts and Implement a Lock-Out Policy', 'boolean', 'True', true);
