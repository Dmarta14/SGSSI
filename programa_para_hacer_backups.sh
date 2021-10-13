#!/bin/bash
cd /var/tmp/Backups/Copia_de_Seguridad/Archivos_De_Seguridad
mkdir $(date +%d-%m-%y)
cd /home/dmarta14/Escritorio/Seguridad

if [-z ls /var/tmp/Backups/Copia_de_Seguridad/Archivos_De_Seguridad/$(date -d yesterday + %d-%m-%y)| grep "$(date -d yesteday +%d-%m-%y)"]
then
rsync -av /home/dmarta14/Escritorio/Seguridad/ /var/tmp/Backups/Copia_de_Seguridad/Archivos_De_Seguridad/$(date +%d-%m-%y') 
else
rsync -av --link-dest=/var/tmp/Backups/Copia_de_Seguridad/Archivos_De_Seguridad/$(date -d yesterday +%d-%m-%y)
fi

cd /var/tmp/Backups/Copia_de_Seguridad/Bases_De_Datos
mkdir $(date +%d-%m-%y)
mysqldump --user=root -p SGSSI>/var/tmp/Backups/Copìa_de_Seguridad/Bases_De_Datos/$(date +%d-%m-%y)/copia_de_seguridad.slq

