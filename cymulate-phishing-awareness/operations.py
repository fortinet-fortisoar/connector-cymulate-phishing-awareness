"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import requests
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('cymulate-phishing-awareness')

API_VERSION = '/v1'


def make_api_call(method="GET", endpoint="", config=None, params=None, data=None, json_data=None):
    try:
        headers = {
            "Content-Type": "application/json",
            "x-token": config.get("key")
        }
        server_url = config.get('url').strip('/')
        if not server_url.startswith('https://') and not server_url.startswith('http://'):
            server_url = "https://" + server_url
        server_url = server_url + API_VERSION + endpoint
        response = requests.request(method=method, url=server_url,
                                    headers=headers, data=data, json=json_data, params=params,
                                    verify=config.get('verify_ssl'))
        if response.ok:
            return response.json()
        else:
            if response.text != "":
                err_resp = response.json()
                failure_msg = err_resp['errors']
                error_msg = 'Response [{0}:{1} Details: {2}]'.format(response.status_code, response.reason,
                                                                     failure_msg if failure_msg else '')
            else:
                error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.reason)
            logger.error(error_msg)
            raise ConnectorError(error_msg)
    except requests.exceptions.SSLError:
        logger.error('An SSL error occurred')
        raise ConnectorError('An SSL error occurred')
    except requests.exceptions.ConnectionError:
        logger.error('A connection error occurred')
        raise ConnectorError('A connection error occurred')
    except requests.exceptions.Timeout:
        logger.error('The request timed out')
        raise ConnectorError('The request timed out')
    except requests.exceptions.RequestException:
        logger.error('There was an error while handling the request')
        raise ConnectorError('There was an error while handling the request')
    except Exception as err:
        raise ConnectorError(str(err))


def convert_date_time(str_date):
    return datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")


def build_payload(params):
    data = {}
    for k, v in params.items():
        if v:
            if k in ['fromDate', 'toDate']:
                data[k] = convert_date_time(v)
            else:
                data[k] = v
    return data


def get_phishing_awareness_report(config, params):
    params = build_payload(params)
    endpoint = "/phishing/attacks"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_phishing_awareness_assessment_id(config, params):
    params = build_payload(params)
    endpoint = "/phishing/ids"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_phishing_awareness_report_for_specific_assessment(config, params):
    endpoint = f"/phishing/attack/technical/{params.get('id')}"
    return make_api_call(endpoint=endpoint, config=config)


def get_phishing_awareness_assessment_history(config, params):
    params = build_payload(params)
    endpoint = "/phishing/history/get-ids"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def get_phishing_awareness_campaign_report_for_specific_assessment(config, params):
    params = build_payload(params)
    endpoint = f"/phishing/history/technical/{params.get('id')}"
    params.pop('id')
    return make_api_call(endpoint=endpoint, config=config, params=params)


def create_phishing_awareness_contact_group(config, params):
    params = build_payload(params)
    endpoint = "/phishing/contacts/group"
    return make_api_call(method='POST', endpoint=endpoint, config=config, params=params)


def get_phishing_awareness_contact_groups(config, params):
    endpoint = "/phishing/contacts/groups"
    return make_api_call(endpoint=endpoint, config=config)


def get_phishing_awareness_contacts(config, params):
    params = build_payload(params)
    endpoint = "/phishing/contacts"
    return make_api_call(endpoint=endpoint, config=config, params=params)


def _check_health(config):
    try:
        get_phishing_awareness_contact_groups(config, params={})
        return True
    except Exception as e:
        logger.error("Invalid Credentials: %s" % str(e))
        raise ConnectorError("Invalid Credentials")


operations = {
    'get_phishing_awareness_report': get_phishing_awareness_report,
    'get_phishing_awareness_assessment_id': get_phishing_awareness_assessment_id,
    'get_phishing_awareness_report_for_specific_assessment': get_phishing_awareness_report_for_specific_assessment,
    'get_phishing_awareness_assessment_history': get_phishing_awareness_assessment_history,
    'get_phishing_awareness_campaign_report_for_specific_assessment': get_phishing_awareness_campaign_report_for_specific_assessment,
    'create_phishing_awareness_contact_group': create_phishing_awareness_contact_group,
    'get_phishing_awareness_contact_groups': get_phishing_awareness_contact_groups,
    'get_phishing_awareness_contacts': get_phishing_awareness_contacts
}
