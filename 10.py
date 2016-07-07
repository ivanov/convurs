# let's roll this out to our server..
#
#
# I've taken care of getting a subdomain up on a server that I have shared
# hosting on. pirsquared.org
#
# I've made a user snarq - and made it possible for me to log into the server
# without having to type in my password (ssh keys are your friend)
#
#
# import sys
# sys.path.insert(0, '<your_local_path>/lib/python2.6/site-packages'))
#
# virtualenv .snarq-env
#
# source .snarq-env/bin/activate
#
#
# # pip install flup
#
# deploying fastcgi
# http://flask.pocoo.org/docs/0.10/deploying/fastcgi/
#
# flup version flup==1.0.3.dev-20110405
#
#
# https://www.google.com/search?q=ImportError%3A+No+module+named+_dummy_thread+flup&oq=ImportError%3A+No+module+named+_dummy_thread+flup&aqs=chrome..69i57j69i58.1693j0j7&sourceid=chrome&es_sm=91&ie=UTF-8
#
# https://issues.mediagoblin.org/ticket/5373
#
#
#
# set up .htaccess - re-write rules to redirect everything through
# dispatch.fcgi
