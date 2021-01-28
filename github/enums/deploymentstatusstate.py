"""
/github/enums/deploymentstatusstate.py

    Copyright (c) 2019-2020 ShineyDev

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from enum import Enum


class DeploymentStatusState(Enum):
    """
    Represents the state of a :class:`~github.DeploymentStatus`.
    """

    #: The deployment experienced an error.
    error = "ERROR"

    #: The deployment failed.
    failure = "FAILURE"

    #: The deployment is inactive.
    inactive = "INACTIVE"

    #: The deployment is in progress.
    in_progress = "IN_PROGRESS"

    #: The deployment is pending.
    pending = "PENDING"

    #: The deployment is queued.
    queued = "QUEUED"

    #: The deployment was successful.
    success = "SUCCESS"

    #: The deployment is waiting.
    waiting = "WAITING"
