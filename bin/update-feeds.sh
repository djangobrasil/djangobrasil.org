#!/bin/sh
#
# File path: /usr/local/bin/update-feeds.sh
#

SOURCE_DIR=/srv/webapps/www.djangobrasil.org/online-branch/src

export PYTHONPATH=$SOURCE_DIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=djangobrasil.settings

python $SOURCE_DIR/djangobrasil/aggregator/bin/update_feeds.py
