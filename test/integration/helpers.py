######################################################################
#
# File: test/integration/helpers.py
#
# Copyright 2022 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################

from typing import Optional
import random
import string

import pytest

from b2sdk.v2 import *

GENERAL_BUCKET_NAME_PREFIX = 'sdktst'
BUCKET_NAME_CHARS = string.ascii_letters + string.digits + '-'
BUCKET_NAME_LENGTH = 50
BUCKET_CREATED_AT_MILLIS = 'created_at_millis'


def bucket_name_part(length):
    return ''.join(random.choice(BUCKET_NAME_CHARS) for _ in range(length))


def authorize(b2_auth_data):
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    b2_api.authorize_account("production", *b2_auth_data)
    return b2_api, info
