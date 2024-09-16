import aws_cdk as core
import aws_cdk.assertions as assertions

from proyecto1_con_python.proyecto1_con_python_stack import Proyecto1ConPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in proyecto1_con_python/proyecto1_con_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Proyecto1ConPythonStack(app, "proyecto1-con-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
