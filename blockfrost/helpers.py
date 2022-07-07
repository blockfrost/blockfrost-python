import hmac
import hashlib
import time


class SignatureVerificationError(Exception):
    def __init__(self, message, header, request_body):
        self.message = message
        self.header = header
        self.request_body = request_body
        super().__init__(self.message)


def get_unix_timestamp():
    return int(time.time())


def verify_webhook_signature(request_body, signature_header, secret, timestamp_tolerance_seconds=600):
    # Parse signature header
    # Example of Blockfrost-Signature header: t=1648550558,v1=162381a59040c97d9b323cdfec02facdfce0968490ec1732f5d938334c1eed4e,v1=...)
    tokens = signature_header.split(',')
    timestamp = None
    signatures = []
    for token in tokens:
        key, value = token.split('=')
        if key == 't':
            timestamp = value
        elif key == 'v1':
            signatures.append(value)
        else:
            print('Cannot parse part of the Blockfrost-Signature header, key "{}" is not supported by this version of Blockfrost SDK. Please upgrade.'.format(key))

    if timestamp is None or timestamp.isnumeric() is False or len(tokens) < 2:
        # timestamp and at least one signature must be present
        raise SignatureVerificationError(
            'Invalid signature header format.', signature_header, request_body)

    if len(signatures) == 0:
        # There are no signatures that this version of SDK supports
        raise SignatureVerificationError(
            'No signatures with supported version scheme.', signature_header, request_body)

    has_valid_signature = False
    for signature in signatures:
        # Recreate signature by concatenating the timestamp with the payload (all in bytes),
        # then compute HMAC using sha256 and provided secret (webhook auth token)
        signature_payload = timestamp.encode() + b"." + request_body
        local_signature = hmac.new(
            secret.encode(), signature_payload, hashlib.sha256).hexdigest()

        # computed signature should match at least one signature parsed from a signature header
        if (hmac.compare_digest(signature, local_signature)):
            has_valid_signature = True
            break

    if has_valid_signature == False:
        raise SignatureVerificationError(
            'No signature matches the expected signature for the payload.', signature_header, request_body)

    current_timestamp = get_unix_timestamp()

    if (current_timestamp - int(timestamp) > timestamp_tolerance_seconds):
        # Event is older than timestamp_tolerance_seconds
        raise SignatureVerificationError(
            'Signature\'s timestamp is outside of the time tolerance.', signature_header, request_body)
    else:
        # Successfully validate the signature only if it is within timestamp_tolerance_seconds tolerance
        return True
