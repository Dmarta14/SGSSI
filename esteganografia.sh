#!/bin/bash
cont=1
for i in /home/dmarta14/Documentos/Seguridad/Imagenes/*.jpg
do
	
	echo $(md5sum /home/dmarta14/Documentos/Seguridad/Imagenes/imagen$cont.jpg| grep "e5ed313192776744b9b93b1320b5e268")
	cont=$(($cont+1))
done
