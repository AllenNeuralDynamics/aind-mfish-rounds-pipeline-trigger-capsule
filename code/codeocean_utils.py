from aind_codeocean_api.codeocean import CodeOceanClient
from aind_codeocean_api.models.computations_requests import RunCapsuleRequest, ComputationNamedParameter, ComputationProcess, ComputationDataAsset


def get_codeocean_client():
    return CodeOceanClient(domain='https://codeocean.allenneuraldynamics.org', token=os.environ['CUSTOM_KEY_2'])


def get_response_content_as_dict(response):
    return json.loads(response.content.decode())

def is_computation_complete(codeocean_client, computation_id):
    response = codeocean_client.get_computation(computation_id)
    response_content = get_response_content_as_dict(response)
    
    # use the presence of end_status as the check
    return 'end_status' in response_content