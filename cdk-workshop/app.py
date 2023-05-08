#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack

from config import *

app = cdk.App()
CdkWorkshopStack(app, "cdk-workshop",
    env=cdk.Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION),
)

app.synth()
