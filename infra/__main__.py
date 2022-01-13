#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cdp_backend.infrastructure import CDPStack
from pulumi import export

###############################################################################

cdp_stack = CDPStack(
    gcp_project_id="cdp-jackson-dev-077",
    municipality_name="CDP Dev",
    firestore_location="us-central",
    hosting_github_url="https://github.com/JacksonMaxfield/cdp-dev",
    hosting_web_app_address="https://JacksonMaxfield.github.io/cdp-dev",
    governing_body="other",
)

export("firestore_address", cdp_stack.firestore_app.app_id)
export("gcp_bucket_name", cdp_stack.firestore_app.default_bucket)
