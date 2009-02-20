#!/bin/sh
#
# File path: /usr/local/bin/update-feeds.sh
#

SOURCE_DIR="$(pwd)/../src"

export PYTHONPATH=$SOURCE_DIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=djangobrasil.settings

python $SOURCE_DIR/djangobrasil/apps/aggregator/bin/update_feeds.py
