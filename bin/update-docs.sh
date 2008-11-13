#!/bin/sh
#
# File path: /usr/local/bin/update-docs.sh
#

L10N_DOCS_DIR=/usr/local/src/django-l10n-portuguese_docs
HTTP_DOCS_DIR=/srv/static/docs.djangobrasil.org

cd $L10N_DOCS_DIR
svn up
make html
cd - > /dev/null
cp -r $L10N_DOCS_DIR/* $HTTP_DOCS_DIR/.
