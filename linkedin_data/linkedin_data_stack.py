from aws_cdk import (
    core as cdk,
    aws_lambda as _lambda,
    aws_s3 as s3,
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class LinkedinDataStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Output bucket
        output_bucket = s3.Bucket(self, 'OutputBucket',
                                  removal_policy=cdk.RemovalPolicy.DESTROY)

        LAMBDA_ENVS = {
            "OUTPUT_TABLE": output_bucket.bucket_name,
        }

        scraper_lambda = _lambda.Function(
            self, "ScraperLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='index.handler',
            code=_lambda.Code.from_asset(
                "lambda/scraper",
                bundling=core.BundlingOptions(
                    image=_lambda.Runtime.PYTHON_3_8.bundling_image,
                    command=[
                        "bash", "-c",
                        "pip install --no-cache -r requirements.txt -t /asset-output && cp -au . /asset-output"
                    ],
                ),
            ),
            environment={**LAMBDA_ENVS},
            timeout=core.Duration.minutes(1),
            profiling=True,
        )

        output_bucket.grant_read_write(scraper_lambda)