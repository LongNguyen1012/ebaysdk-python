import sys

sys.path.insert(0, '/Users/longn.ctr/Documents/Projects/ebaysdk-python/')

from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as Finding


try:
    api = Finding(config_file="/Users/longn.ctr/Documents/Projects/ebaysdk-python/ebay.yaml")
    response = api.execute('findItemsbyCategory', verb_attrs={"category_id": 10181, "entries_per_page": 2})
    print(response.dict())
    print(response.reply)
except ConnectionError as e:
    print(e)
    print(e.response.dict())
