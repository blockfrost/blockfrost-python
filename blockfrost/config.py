from enum import Enum
import pkg_resources


class ApiUrls(Enum):
    mainnet = 'https://cardano-mainnet.blockfrost.io/api'
    testnet = 'https://cardano-testnet.blockfrost.io/api'
    ipfs = 'https://ipfs.blockfrost.io/api'


DEFAULT_API_VERSION = 'v0'
DEFAULT_ORDER = 'asc'
DEFAULT_PAGINATION_PAGE_COUNT = 1
DEFAULT_PAGINATION_PAGE_ITEMS_COUNT = 100

ADDRESS_GAP_LIMIT = 20

package_name = 'blockfrost-python'
USER_AGENT = f'{package_name} {pkg_resources.get_distribution(package_name).version}'
