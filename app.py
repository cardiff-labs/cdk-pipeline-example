import aws_cdk as cdk

from infrastructure.stacks.pipeline import MyPipelineStack

app = cdk.App()
stack = MyPipelineStack(app, "pipeline")
cdk.Tags.of(app).add("project", "cdk-pipeline-example")
app.synth()
