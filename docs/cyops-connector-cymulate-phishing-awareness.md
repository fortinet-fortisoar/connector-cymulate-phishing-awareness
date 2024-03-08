## About the connector
Cymulate's Phishing Awareness campaigns evaluate employees' security awareness levels by simulating phishing attacks.
<p>This document provides information about the Cymulate Phishing Awareness Connector, which facilitates automated interactions, with a Cymulate Phishing Awareness server using FortiSOAR&trade; playbooks. Add the Cymulate Phishing Awareness Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cymulate Phishing Awareness.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-cymulate-phishing-awareness</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Cymulate Phishing Awareness server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cymulate Phishing Awareness server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cymulate Phishing Awareness</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Cymulate server URL to connect and perform the automated operations.</td>
</tr><tr><td>Secret Key</td><td>Specify the Secret Key of the API Application already created in the Cymulate Server.</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector

The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Phishing Awareness Report</td><td>Get the latest Phishing Awareness report results (overview) by the environment ID from Cymulate.</td><td>get_phishing_awareness_report <br/>Investigation</td></tr>
<tr><td>Get Phishing Awareness assessment IDs</td><td>Retrieve list of Phishing Awareness assessment IDs from Cymulate.</td><td>get_phishing_awareness_assessment_id <br/>Investigation</td></tr>
<tr><td>Get Phishing Awareness Report for Specific Assessment</td><td>Retrieve Phishing Awareness report results for a specific assessment from Cymulate.</td><td>get_phishing_awareness_report_for_specific_assessment <br/>Investigation</td></tr>
<tr><td>Get Phishing Awareness Assessment History</td><td>Retrieve the Phishing Awareness Campaign assessment history within the date range provided. If a date range is not provided, the response will retrieve the history from the last 30 days.</td><td>get_phishing_awareness_assessment_history <br/>Investigation</td></tr>
<tr><td>Get Phishing Awareness Campaign Report for Specific Assessment</td><td>Retrieve Phishing Awareness Campaign report results for a specific assessment from Cymulate.</td><td>get_phishing_awareness_campaign_report_for_specific_assessment <br/>Investigation</td></tr>
<tr><td>Create Phishing Awareness Contact Group</td><td>Create Phishing Awareness contact group under Phishing Awareness > Contacts in Cymulate.</td><td>create_phishing_awareness_contact_group <br/>Investigation</td></tr>
<tr><td>Get Phishing Awareness Contact Groups</td><td>Retrieve a list of Phishing Awareness contact groups and their IDs from Cymulate.</td><td>get_phishing_awareness_contact_groups <br/>Investigation</td></tr>
<tr><td>Get Phishing Awareness Contacts</td><td>Retrieve a list of contacts within a specific contact group by ID from Cymulate.</td><td>get_phishing_awareness_contacts <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Phishing Awareness Report

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>Specify the ID of the environment. If an ID is not provided, the request will return latest report results for the Default environment.
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "success": "",
    "cymulate": "",
    "errors": [
        {
            "msg": ""
        }
    ],
    "code": ""
}</pre>
### operation: Get Phishing Awareness assessment IDs
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>Specify the ID of the environment. If an ID is not provided, the request will return latest report results for the Default environment.
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "success": "",
    "cymulate": "",
    "data": []
}</pre>
### operation: Get Phishing Awareness Report for Specific Assessment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Assessment ID</td><td>Specify the assessment ID to fetch its phishing awareness report.
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "success": "",
    "cymulate": "",
    "errors": [
        {
            "msg": ""
        }
    ],
    "code": ""
}</pre>
### operation: Get Phishing Awareness Assessment History
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>From Date</td><td>Specify the date from where to fetch phishing awareness campaign assessments .
</td></tr><tr><td>To Date</td><td>Specify the date until which phishing awareness campaign assessments should be fetched.
</td></tr><tr><td>Environment ID</td><td>Specify the ID of the environment. If an ID is not provided, the request will return latest report results for the Default environment.
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "success": "",
    "cymulate": "",
    "data": {
        "attack": [],
        "total": ""
    }
}</pre>
### operation: Get Phishing Awareness Campaign Report for Specific Assessment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Assessment ID</td><td>Specify the assessment ID to fetch its phishing awareness campaign report.
</td></tr><tr><td>Offset</td><td>Specify the number of records to skip.
</td></tr><tr><td>Limit</td><td>Specify the limit of how many items to get.
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "success": "",
    "cymulate": "",
    "errors": [
        {
            "msg": ""
        }
    ],
    "code": ""
}</pre>
### operation: Create Phishing Awareness Contact Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Group Name</td><td>Specify the name for the new contact group.
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "success": "",
    "id": ""
}</pre>
### operation: Get Phishing Awareness Contact Groups
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "_id": "",
    "name": "",
    "client": "",
    "lastUpdated": "",
    "updated": "",
    "createdAt": "",
    "created": "",
    "canDelete": ""
}</pre>
### operation: Get Phishing Awareness Contacts
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Group ID</td><td>Specify the contact group ID to fetch its phishing awareness contacts.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
