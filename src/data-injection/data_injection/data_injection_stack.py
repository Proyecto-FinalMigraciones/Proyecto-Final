from aws_cdk import (
    Duration,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,

    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class DataInjectionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "DataInjectionQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # Crea un recurso para la regla de EventBridge
        event_rule_target = _lambda.Function(
            self, "EventRuleCronCargaIncremental",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "S3_BUCKET_NAME": "csvdatainjection"
            }
        )

        rule = events.Rule(self, "RuleCronCargaIncremental",        
            schedule=events.Schedule.rate(Duration.minutes(120)),
            targets=[targets.LambdaFunction(event_rule_target)]
)

        # Asocia una política IAM a la función Lambda para permitir el acceso al bucket de S3
        event_rule_target.add_to_role_policy(
            iam.PolicyStatement(
                actions=["s3:GetObject"],
                resources=[f"arn:aws:s3:::csvdatainjection/*"]
            )
        )
