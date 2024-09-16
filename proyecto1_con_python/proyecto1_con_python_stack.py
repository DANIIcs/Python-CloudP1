#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
)
from constructs import Construct

class Proyecto1ConPythonStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        # Definir el `synthesizer` con los roles y el bucket especificado
        synthesizer = cdk.DefaultStackSynthesizer(
            file_assets_bucket_name="proyecto-cloud",
            bucket_prefix="",
            cloud_formation_execution_role="arn:aws:iam::298526054328:role/LabRole",
            deploy_role_arn="arn:aws:iam::298526054328:role/LabRole",
            file_asset_publishing_role_arn="arn:aws:iam::298526054328:role/LabRole",
            image_asset_publishing_role_arn="arn:aws:iam::298526054328:role/LabRole"
        )

        # Combinar props con el `synthesizer`
        super().__init__(scope, id, synthesizer=synthesizer, **kwargs)

        # Buscar la VPC existente por su ID
        vpc = ec2.Vpc.from_lookup(self, "MyVpc", vpc_id="vpc-05190e608cebfb9be")

        # Usar un IAM Role existente
        instance_role = iam.Role.from_role_arn(self, "LabRole", "arn:aws:iam::298526054328:role/LabRole")

        # Buscar la última AMI de Ubuntu
        ubuntu_ami = ec2.LookupMachineImage(
            name="ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*",
            owners=["099720109477"]  # ID del propietario de Ubuntu en AWS
        )

        # Crear una instancia EC2 con los parámetros especificados
        instance = ec2.Instance(self, "WebServerProyecto1", 
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ubuntu_ami,
            vpc=vpc,
            role=instance_role
        )

        # Comandos de UserData
        user_data_commands = [
            "apt-get update -y",
            "apt-get install -y git",
            "git clone https://github.com/DANIIcs/websimple.git",
            "git clone https://github.com/DANIIcs/webplantilla.git",
            "cd websimple",
            "nohup python3 -m http.server 8080 &",
            "cd ../webplantilla",
            "nohup python3 -m http.server 8081 &"
        ]

        # Agregar los comandos de UserData a la instancia
        for cmd in user_data_commands:
            instance.user_data.add_commands(cmd)

        # Permitir tráfico HTTP en los puertos 8080 y 8081 desde cualquier IPv4
        instance.connections.allow_from_any_ipv4(ec2.Port.tcp(8080), "Allow HTTP traffic on port 8080")
        instance.connections.allow_from_any_ipv4(ec2.Port.tcp(8081), "Allow HTTP traffic on port 8081")


app = cdk.App()
Proyecto1ConPythonStack(app, "Proyecto1ConPythonStack", 
    env=cdk.Environment(account="298526054328", region="us-east-1"))

app.synth()
