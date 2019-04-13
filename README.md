# Description
Simple Python code to retrieve data from the Mevo Metropolitan Bicycle system. It's capable of downloading key for location.js file, setting proper headers and cookies to automate communication with the datasource, just like a browser. 

# Usage
Get raw data from location.js:
```
from pymevo.mevo import Mevo
m = Mevo()
m.get_locationjs()
```

With proxy or non-random user agent:
```
m = Mevo(user_agent=value, https_proxy=value})
```

Don't download key and cookies when creating object (for dry run/testing):
```
m = Mevo(init=False)
```

# To be done
 - data parsing
 - key rotation (invalidated each hour)