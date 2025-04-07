"""
These are category related models.
Include VideoCategory
"""

from typing import List, Optional

from pydantic import Field as field

from .base import BaseModel
from .common import BaseApiResponse, BaseResource


class CategorySnippet(BaseModel):
    """
    This is base category snippet for video and guide.
    """

    channelId: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)


class VideoCategorySnippet(CategorySnippet):
    """
    A class representing video category snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/videoCategories#snippet
    """

    assignable: Optional[bool] = field(default=None, repr=False)


class VideoCategory(BaseResource):
    """
    A class representing video category info.

    Refer: https://developers.google.com/youtube/v3/docs/videoCategories
    """

    snippet: Optional[VideoCategorySnippet] = field(default=None, repr=False)


class VideoCategoryListResponse(BaseApiResponse):
    """
     A class representing the video category's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/videoCategories/list#response_1
    """

    items: Optional[List[VideoCategory]] = field(default=None, repr=False)
