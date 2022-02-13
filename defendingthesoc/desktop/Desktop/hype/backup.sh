#!/bin/ash
TIME=`date +%b-%d-%y`
FILENAME=site_backup_$TIME.tar.gz	# Backup filename
SRCDIR=/var/www/html			# Backup source folder
DSTDIR=/home/hype/backups		# Backup destination folder
tar -cpzf $DSTDIR/$FILENAME $SRCDIR
