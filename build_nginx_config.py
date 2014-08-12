import urllib2
import zipfile
import os

CONFIGBUNDLE = 'nginx-config.zip'
ENDPOINT = '/admin/api/nginx.zip?provider_key='

def build_provider_url():
    provider_key = os.environ['THREESCALE_PROVIDER_KEY']
    admin_domain = os.environ['THREESCALE_ADMIN_DOMAIN']
    url = 'https://%s%s%s' % (admin_domain, ENDPOINT, provider_key)
    return url

def download_config_bundle(url):
    req = urllib2.urlopen(url)
    with open(CONFIGBUNDLE, 'w') as zip_bundle:
        zip_bundle.write(req.read())
    with zipfile.ZipFile(CONFIGBUNDLE, 'r') as z:
        z.extractall()

def modify_config_for_heroku():
    pass

url = build_provider_url()
print 'DEBUG: url %s' % (url)
download_config_bundle(url)
print 'DEBUG: done'
