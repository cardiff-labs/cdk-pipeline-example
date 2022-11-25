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
                    "my-org/my-app",
                    "main",
                    connection_arn="arn:aws:codestar-connections:us-east-1:222222222222:connection/7d2469ff-514a-4e4f-9003-5ca4a43cdc41",
                ),
                commands=["npm ci", "npm run build", "npx cdk synth"],
            ),
        )

        pipeline.add_stage(ExampleApplication(self, "Test"))
