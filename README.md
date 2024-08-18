# First
1. Asegurarme que está instalado localstack
https://www.notion.so/ang3l/localstack-Mac-87b47e7e20df4a0cae98c3ce370f41f3?pvs=4

2. Asegurarme que está corriendo localstack. En caso de que no ejecutar:
```shell
localstack start -d
```

3. Asegurarme que tengo awslocal instalado, en caso de que no se tenga instalado, se puede ejecutar de forma local al proyecto mediante:
```shell
cd $PWD
python3 -m venv my_env
source my_env/bin/activate
pip3 install awscli-local
# Test
awslocal kinesis list-streams
```

4. Asegurarme que tengo terraform-local instalado, en caso de que no se tenga instalado, se puede ejecutar de forma local al proyecto mediante:
```shell
pip3 install terraform-local
# Test
tflocal
```

5. Asegurarme de que la variable de entorno siguiente está definida
```shell
export AWS_S3_FORCE_PATH_STYLE=true
```

6. Crear archivo main.tf con la información de la infraestructura a crear

7. Ejecutar terraform-local
```shell
tflocal init
tflocal plan
tflocal apply
tflocal destroy
```

8. Comandos útiles para el proyecto
```shell
# Ver eventbus
awslocal events list-event-buses
# Obtener información de un role
awslocal iam get-role --role-name lambda-exec-role
# listar lambdas existentes
awslocal lambda list-functions
# Ver información de una lambda. Una vez vista la información, se puede descargar el código usando la URL firmada dentro de "Location" que nos dirige a un bucket de s3 donde está la información
awslocal lambda get-function --function-name sn_producer-function
# Invocar una lambda
awslocal lambda invoke --function-name sn_producer-function output.txt
# Ver información dentro de cloudwatch generada a partir de la lambda
awslocal logs describe-log-groups
awslocal logs describe-log-streams --log-group-name /aws/lambda/sn_consumer1-function
awslocal logs get-log-events --log-group-name /aws/lambda/sn_consumer1-function --log-stream-name '2024/08/17/[$LATEST]a2b4e4186ca5aa8da3f83364608f7fdc'
```
