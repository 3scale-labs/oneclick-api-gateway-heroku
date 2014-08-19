from fnmatch import fnmatch
import urllib2
import zipfile
import os
import sys
import fileinput

CONFIGBUNDLE = 'nginx-config.zip'
ENDPOINT = '/admin/api/nginx.zip?provider_key='
REPLACEMENTS = {
    '# daemon off;' : 'daemon off;',
    '# error_log stderr notice;' : 'error_log stderr;',
    'listen 80;' : 'listen ${{PORT}} ;',
    'access_by_lua_file lua_tmp.lua;' : 'access_by_lua_file nginx_3scale_access.lua;',
    'server_name' : '# server_name'
}

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

def find_file(namepattern):
    for file in os.listdir('.'):
        if fnmatch(file, namepattern):
            return file

def modify_config_for_heroku(nginx_conf_file):
    for line in fileinput.input(nginx_conf_file, inplace=True):
        for original, replacement in REPLACEMENTS.iteritems():
            if original in line:
                line = line.replace(original, replacement)
        sys.stdout.write(line)


url = build_provider_url()
download_config_bundle(url)
print '3SCALE: configuration bundle was successfully downloaded.'

nginxconf = find_file('nginx_*.conf')
nginxlua = find_file('nginx_*.lua')
modify_config_for_heroku(nginxconf)
os.rename(nginxconf, 'nginx.conf')
os.rename(nginxlua, 'nginx_3scale_access.lua')
print '3SCALE: configuration is ready to go.'
