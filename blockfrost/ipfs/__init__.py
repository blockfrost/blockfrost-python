import os

from ..utils import Api, ApiUrls


class BlockFrostIPFS(Api):

    def __init__(self, project_id: str = None, base_url: str = None, api_version: str = None):
        super().__init__(
            project_id=project_id,
            base_url=base_url if base_url else os.environ.get('BLOCKFROST_IPFS_URL', default=ApiUrls.ipfs.value),
            api_version=api_version)

    from .add import add
    from .gateway import gateway
    from .pins import \
        pin_object, \
        pined_list, \
        pined_object, \
        pined_object_remove
