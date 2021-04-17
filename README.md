# how to run

## for dev
docker-compose -f docker-compose.dev.yml up -d

## for prod
docker-compose -f docker-compose.prod.yml up -d

## super user
super user credentials: benjamin:whatever


## import
after running, django needs import:
enter django container:
docker exec -it polity_django_dev[or prod] /bin/bash

afterwards enter django shell

```python
python manage.py shell
```

```python
from locations import load

load.country_import()
load.canton_import()
load.municipality_import()
```

exit shell ctrl + D

afterwards import data dump:
python manage.py loaddata import/dump2...json

good to go.

/api/v1/ for api responses
/admin for django admin

👋