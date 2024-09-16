# Proyecto 1 de Cloud computing (Pyhton)

## Pasos a seguir:

Inicializamos el aws

Guadamos las credenciales en el directorio de .aws con el siguiente comando 

   ```bash
   notepad $env:USERPROFILE.aws\credentials
   ```

Creamos un nuveo bucket 
![](./images/1.png)

Buscamos nuestra id del AMI

Buscamos tambien la id del panel VPC
![](./images/2.png)


Creamos un archivo en vscode de python con los sigueintes comandos 

   ```bash
    pip install aws-cdk-lib

    cdk init app --language python
   ```

Ajustamos el codigo de tal manera que utilice las credenciales y tenaga los roles establecidos para que pueda abirir los puertos 8080 y 8081

Usamos los siguietes comando para deployar

   ```bash
   cdk deploy
   ```

Comporbamos que se haya deployado una nueva instancia en nuestro ec2
![](./images/3.png)


Uilizamos el id de esta instancia y comprobamos con los puertos establecidos

![](./images/4.png)
![](./images/5.png)


