from aws_cdk import Stage

from .database import DatabaseStack


class ExampleApplication(Stage):
    def __init__(self, scope, id, *, env=None, outdir=None):
        super().__init__(scope, id, env=env, outdir=outdir)

        DatabaseStack(self, "Database")
        # TODO: also create a lambda and use table name as argument
