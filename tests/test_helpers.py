import os
import mock
import pytest
from blockfrost import SignatureVerificationError, verify_webhook_signature

request_body = b'{"id":"47668401-c3a4-42d4-bac1-ad46515924a3","webhook_id":"cf68eb9c-635f-415e-a5a8-6233638f28d7","created":1650013856,"type":"block","payload":{"time":1650013853,"height":7126256,"hash":"f49521b67b440e5030adf124aee8f88881b7682ba07acf06c2781405b0f806a4","slot":58447562,"epoch":332,"epoch_slot":386762,"slot_leader":"pool1njjr0zn7uvydjy8067nprgwlyxqnznp9wgllfnag24nycgkda25","size":34617,"tx_count":13,"output":"13403118309871","fees":"4986390","block_vrf":"vrf_vk197w95j9alkwt8l4g7xkccknhn4pqwx65c5saxnn5ej3cpmps72msgpw69d","previous_block":"9e3f5bfc9f0be44cf6e14db9ed5f1efb6b637baff0ea1740bb6711786c724915","next_block":null,"confirmations":0}}'
success_fixtures_list = [
    {
        'description': 'valid signature',
        'request_body': request_body,
        'signature_header': 't=1650013856,v1=f4c3bb2a8b0c8e21fa7d5fdada2ee87c9c6f6b0b159cc22e483146917e195c3e',
        'secret': '59a1eb46-96f4-4f0b-8a03-b4d26e70593a',
        'current_timestamp_mock': 1650013856 + 1,
        'result': True
    },
    {
        'description': '2 signatures, one valid and one invalid',
        'request_body': request_body,
        'signature_header': 't=1650013856,v1=abc,v1=f4c3bb2a8b0c8e21fa7d5fdada2ee87c9c6f6b0b159cc22e483146917e195c3e',
        'secret': '59a1eb46-96f4-4f0b-8a03-b4d26e70593a',
        'current_timestamp_mock': 1650013856 + 1,
        'result': True
    }
]

error_fixtures_list = [
    {
        'description': 'throws due to invalid header fromat',
        'request_body': request_body,
        'signature_header': 'v1=f4c3bb2a8b0c8e21fa7d5fdada2ee87c9c6f6b0b159cc22e483146917e195c3e',
        'secret': '59a1eb46-96f4-4f0b-8a03-b4d26e70593a',
        'current_timestamp_mock': 1650013856 + 1,
        'result_error': 'Invalid signature header format.'
    },
    {
        'description': 'throws due to sig version not supported by this sdk',
        'request_body': request_body,
        'signature_header': 't=1650013856,v42=abc',
        'secret': '59a1eb46-96f4-4f0b-8a03-b4d26e70593a',
        'current_timestamp_mock': 1650013856 + 1,
        'result_error': 'No signatures with supported version scheme.'
    },
    {
        'description': 'throws due to no signature match',
        'request_body': request_body,
        'signature_header': 't=1650013856,v1=abc',
        'secret': '59a1eb46-96f4-4f0b-8a03-b4d26e70593a',
        'current_timestamp_mock': 1650013856 + 1,
        'result_error': 'No signature matches the expected signature for the payload.'
    },
    {
        'description': 'throws due to timestamp out of tolerance zone',
        'request_body': request_body,
        'signature_header': 't=1650013856,v1=f4c3bb2a8b0c8e21fa7d5fdada2ee87c9c6f6b0b159cc22e483146917e195c3e',
        'secret': '59a1eb46-96f4-4f0b-8a03-b4d26e70593a',
        'current_timestamp_mock': 1650013856 + 7200,
        'result_error': 'Signature\'s timestamp is outside of the time tolerance.'
    }
]


@pytest.mark.parametrize("fixture", success_fixtures_list)
def test_verify_webhook_signature(fixture):
    with mock.patch('blockfrost.helpers.get_unix_timestamp', return_value=fixture['current_timestamp_mock']):
        res = verify_webhook_signature(
            fixture['request_body'], fixture['signature_header'], fixture['secret'])
        assert res == fixture['result']


@pytest.mark.parametrize("fixture", error_fixtures_list)
def test_verify_webhook_signature_fails(fixture):
    with mock.patch('blockfrost.helpers.get_unix_timestamp', return_value=fixture['current_timestamp_mock']):
        with pytest.raises(SignatureVerificationError) as e_info:
            verify_webhook_signature(
                fixture['request_body'], fixture['signature_header'], fixture['secret'])
        assert str(e_info.value) == fixture['result_error']
        assert e_info.value.header == fixture['signature_header']
        assert e_info.value.request_body == fixture['request_body']
