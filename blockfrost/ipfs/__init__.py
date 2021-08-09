import os

from ..utils import Api, ApiUrls
from .add import add


class BlockFrostIPFS(Api):

    def __init__(self, project_id: str = None, base_url: str = None, api_version: str = None):
        super().__init__(
            project_id=project_id,
            base_url=base_url if base_url else os.environ.get('BLOCKFROST_IPFS_URL', default=ApiUrls.ipfs.value),
            api_version=api_version)

    # add
    add = add
