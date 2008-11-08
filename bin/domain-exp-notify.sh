#!/bin/sh
#
# File path: /usr/local/bin/domain-exp-notify.sh
#

DB_DOMAIN=$1

M_SUBJECT="Dominio $DB_DOMAIN expirando..."
M_DEST=root@localhost

cat <<EOF | mail -s "$M_SUBJECT" $M_DEST
Atencao! O dominio $DB_DOMAIN expira nos proximos dias.

Favor verificar com os responsaveis a respeito da renovacao.

--
Mensagem enviada pelo script domain-exp-notify.sh
EOF
