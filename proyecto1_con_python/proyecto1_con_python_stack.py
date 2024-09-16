from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    Stack
)
from constructs import Construct

class Proyecto1ConPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Crear un bucket S3
        bucket = s3.Bucket(self, "Proyecto1Bucket", 
                           bucket_name="proyecto1-python")

        # IAM Role existente
        instance_role = iam.Role.from_role_arn(self, "LabRole", "arn:aws:iam::298526054328:role/LabRole")

        # Usar LookupMachineImage para encontrar la última imagen de Ubuntu
        ubuntu_ami = ec2.MachineImage.lookup(name="ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*", owners=["099720109477"])

        # VPC existente
        vpc = ec2.Vpc.from_lookup(self, "MyVpc", vpc_id="vpc-05190e608cebfb9be")

        # Crear una instancia EC2
        instance = ec2.Instance(self, "WebServerProyecto1",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ubuntu_ami,
            vpc=vpc,
            role=instance_role
        )

        # Agregar comandos de UserData para la instancia
        instance.user_data.add_commands(
            "apt-get update -y",
            "apt-get install -y git",
            "git clone https://github.com/DANIIcs/websimple.git",
            "git clone https://github.com/DANIIcs/webplantilla.git",
            "cd websimple && nohup python3 -m http.server 8080 &",
            "cd ../webplantilla && nohup python3 -m http.server 8081 &"
        )

        # Permitir tráfico HTTP en los puertos 8080 y 8081
        instance.connections.allow_from_any_ipv4(ec2.Port.tcp(8080), "Allow HTTP traffic on port 8080")
        instance.connections.allow_from_any_ipv4(ec2.Port.tcp(8081), "Allow HTTP traffic on port 8081")

        # Output para ver el bucket creado
        self.output_bucket_name(bucket.bucket_name)

    def output_bucket_name(self, bucket_name: str):
        print(f"Bucket creado: {bucket_name}")
