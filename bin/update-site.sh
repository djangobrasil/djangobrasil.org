#!/bin/sh
#
# File path: /usr/local/bin/update-site.sh
#

PROJECT_DIR=/srv/webapps/www.djangobrasil.org/online-branch

svn up $PROJECT_DIR
invoke-rc.d apache2 reload
