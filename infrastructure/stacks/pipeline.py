import aws_cdk as cdk
from aws_cdk import Stack, pipelines

from .application import ExampleApplication


class MyPipelineStack(Stack):
    def __init__(
        self,
        scope,
        id,
        *,
        description=None,
        env=None,
        stack_name=None,
        tags=None,
        synthesizer=None,
        termination_protection=None,
        analytics_reporting=None,
        cross_region_references=None
    ):
        super().__init__(
            scope,
            id,
            description=description,
            env=env,
            stack_name=stack_name,
            tags=tags,
            synthesizer=synthesizer,
            termination_protection=termination_protection,
            analytics_reporting=analytics_reporting,
            cross_region_references=cross_region_references,
        )

        # Create a code commit repo and load in source

        # Reference repo from CodePipeline
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                # Use a connection created using the AWS console to authenticate to GitHub
                input=pipelines.CodePipelineSource.connection(
                    "cardiff-labs/cdk-pipeline-example",
                    "main",
                    connection_arn="arn:aws:codestar-connections:us-west-1:254688924456:connection/2261a500-932d-4a6f-93cc-b3064d536d52",
                ),
                commands=["make dev", "npm i -g aws-cdk", "cdk synth"],
            ),
        )

        pipeline.add_stage(ExampleApplication(self, "Test"))
