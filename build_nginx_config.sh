#!/usr/bin/env bash

NGINX_ENDPOINT="/admin/api/nginx.zip?provider_key="
PROVIDER_KEY=$THREESCALE_PROVIDER_KEY
ADMIN_DOMAIN=$THREESCALE_ADMIN_DOMAIN

echo "provider key is... $PROVIDER_KEY"
echo "admin domain is... $ADMIN_DOMAIN"

# download config from 3scale
# rename files to follow openresty buildpack pattern
# restart Nginx using new files
