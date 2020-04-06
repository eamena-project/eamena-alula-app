# eamena-alula-app

INSALLATION GUIDE

1. Create virtual environment

2. Clone arches and install into virtual env. Need to do it this way so it picks up the requirements file and does the django override.

  git clone https://github.com/eamena-oxford/eamena-core-arches3
  cd au-app
  python setup.py install
  cd ..

3. Then install extra dependencies related to AlUla, this includes the edited version of arches_hip

  git clone https://github.com/eamena-oxford/eamena-alula-app
  cd eamena-alula-app/
  pip install -r requirements.txt

4. Create settings_local.py file in eamena/

5. Add gdal and geos settings to this file and set the database user and password. E.g.

  from arches_hip.settings import DATABASES

  GDAL_LIBRARY_PATH = '/local/eamena/lib/libgdal.so'
  GEOS_LIBRARY_PATH = '/local/eamena/lib/libgeos_c.so'

  DATABASES['default']['PASSWORD'] = 'PASSWORD'
  DATABASES['default']['USER'] = 'USER'
  
6. If there's a problem reading the GEOS version id, need to edit the site-packages/django/contrib/gis/geos/libgeos.py file.     Replace

  r'((rc(?P<release_candidate>\d+))|dev)?-CAPI-(?P<capi_version>\d+\.\d+\.\d+)( r\d+)?$'
  with

  r'((rc(?P<release_candidate>\d+))|dev)?-CAPI-(?P<capi_version>\d+\.\d+\.\d+)( r\d+)?.*$'
  
7. Setup database and elasticsearch

  python manage.py packages -o setup
  python manage.py packages -o start_elasticsearch
  python manage.py packages -o install
  
  
