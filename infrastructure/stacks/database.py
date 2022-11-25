import aws_cdk as cdk
from aws_cdk import aws_dynamodb


class DatabaseStack(cdk.Stack):
    def __init__(self, scope, id):
        super().__init__(scope, id)

        self.table = aws_dynamodb.Table(
            self, "Table", partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING)
        )
