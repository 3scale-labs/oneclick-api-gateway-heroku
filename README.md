## One-click deployment of a 3scale API Proxy

This is the simplest way to get a 3scale API proxy up and running. Clicking on the button below will deploy an Nginx-based API proxy on Heroku using the configuration generated from your 3scale account. That's it.

## Deploy your API gateway now

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Prerequisites

* a [3Scale](http://3scale.net) account (you can sign up for free if you don't have one yet)
* a [Heroku](http://heroku.com) account

## Steps

1. Go to your 3scale admin portal and configure your API following [the instructions](https://support.3scale.net/get-started/quickstarts/hello-world-nginx).
2. Click on the [Deploy to Heroku](#deploy-your-api-gateway-now) button above to deploy and start running your own proxy
3. You will be asked to enter a couple of pieces of information:
    * Heroku app name: the name of your Heroku application
    * 3scale provider key: you can find it in the Account menu of your 3scale admin portal
    * 3scale admin domain: the domain of your 3scale admin portal (e.g. companyname-admin.3scale.net)

## Troubleshooting

Most errors in the proxy configuration can be detected and solved by looking at the Nginx logs. To access the logs you will need to install the [Heroku toolbelt](https://toolbelt.heroku.com/) and then run:
```shell
heroku logs --app <your-heroku-app-name>
```

You can find more information about Nginx in the official documentation page: http://nginx.org/en/docs/

For more information on using and configuring the 3scale platform and your API proxy head over to the [3scale support portal](https://support.3scale.net/).

## Feedback

* email: support [at] 3scale.net
* twitter: [@3scale](http://www.twitter.com/3scale)

## Credits

* [Leaf Corcoran](https://github.com/leafo) creator of the package to run [OpenResty in Heroku with the Lua buildpack](https://github.com/leafo/heroku-openresty).
* [Taylor Brown](https://github.com/Taytay) for initially putting together the template to use the 3scale proxy in Heroku.
