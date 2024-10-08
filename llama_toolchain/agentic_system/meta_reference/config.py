# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

from pydantic import BaseModel


class AgenticSystemConfig(BaseModel):
    brave_search_api_key: Optional[str] = None
    wolfram_api_key: Optional[str] = None
