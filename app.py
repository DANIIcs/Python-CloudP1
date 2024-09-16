#!/usr/bin/env python3
import aws_cdk as cdk
from proyecto1_con_python.proyecto1_con_python_stack import Proyecto1ConPythonStack

app = cdk.App()

# Crear el stack
Proyecto1ConPythonStack(app, "Proyecto1ConPythonStack", env={
    'account': '298526054328',
    'region': 'us-east-1'
})

app.synth()
