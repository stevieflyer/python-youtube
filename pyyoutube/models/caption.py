"""
These are caption related models
"""

from typing import List, Optional

from pydantic import Field as field

from .base import BaseModel
from .mixins import DatetimeTimeMixin
from .common import BaseResource, BaseApiResponse


class CaptionSnippet(BaseModel, DatetimeTimeMixin):
    """
    A class representing the caption snippet resource info.

    Refer: https://developers.google.com/youtube/v3/docs/captions#snippet
    """

    videoId: Optional[str] = field(default=None)
    lastUpdated: Optional[str] = field(default=None)
    trackKind: Optional[str] = field(default=None, repr=False)
    language: Optional[str] = field(default=None, repr=False)
    name: Optional[str] = field(default=None, repr=False)
    audioTrackType: Optional[str] = field(default=None, repr=False)
    isCC: Optional[bool] = field(default=None, repr=False)
    isLarge: Optional[bool] = field(default=None, repr=False)
    isEasyReader: Optional[bool] = field(default=None, repr=False)
    isDraft: Optional[bool] = field(default=None, repr=False)
    isAutoSynced: Optional[bool] = field(default=None, repr=False)
    status: Optional[str] = field(default=None, repr=False)
    failureReason: Optional[str] = field(default=None, repr=False)


class Caption(BaseResource):
    """
    A class representing the caption resource info.

    Refer: https://developers.google.com/youtube/v3/docs/captions
    """

    snippet: Optional[CaptionSnippet] = field(default=None)


class CaptionListResponse(BaseApiResponse):
    """
    A class representing the activity response info.

    Refer: https://developers.google.com/youtube/v3/docs/captions/list?#response_1
    """

    items: Optional[List[Caption]] = field(default_factory=list, repr=False)
