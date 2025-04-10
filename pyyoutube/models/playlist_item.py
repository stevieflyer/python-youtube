"""
These are playlistItem related models.
"""

from typing import List, Optional

from pydantic import Field as field

from .base import BaseModel
from .mixins import DatetimeTimeMixin
from .common import BaseApiResponse, BaseResource, ResourceId, Thumbnails


class PlaylistItemContentDetails(BaseModel, DatetimeTimeMixin):
    """
    A class representing the playlist item's content details info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems#contentDetails
    """

    videoId: Optional[str] = field(default=None)
    note: Optional[str] = field(default=None, repr=False)
    videoPublishedAt: Optional[str] = field(default=None)
    startAt: Optional[str] = field(default=None, repr=False)
    endAt: Optional[str] = field(default=None, repr=False)


class PlaylistItemSnippet(BaseModel, DatetimeTimeMixin):
    """
    A class representing the playlist item's snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems#snippet
    """

    publishedAt: Optional[str] = field(default=None, repr=False)
    channelId: Optional[str] = field(default=None, repr=False)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    thumbnails: Optional[Thumbnails] = field(default=None, repr=False)
    channelTitle: Optional[str] = field(default=None, repr=False)
    videoOwnerChannelTitle: Optional[str] = field(default=None, repr=False)
    videoOwnerChannelId: Optional[str] = field(default=None, repr=False)
    playlistId: Optional[str] = field(default=None, repr=False)
    position: Optional[int] = field(default=None, repr=False)
    resourceId: Optional[ResourceId] = field(default=None, repr=False)


class PlaylistItemStatus(BaseModel):
    """
    A class representing the playlist item's status info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems#status
    """

    privacyStatus: Optional[str] = field(default=None)


class PlaylistItem(BaseResource):
    """
    A class representing the playlist item's info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems
    """

    snippet: Optional[PlaylistItemSnippet] = field(default=None, repr=False)
    contentDetails: Optional[PlaylistItemContentDetails] = field(
        default=None, repr=False
    )
    status: Optional[PlaylistItemStatus] = field(default=None, repr=False)


class PlaylistItemListResponse(BaseApiResponse):
    """
    A class representing the playlist item's retrieve response info.

    Refer: https://developers.google.com/youtube/v3/docs/playlistItems/list#response_1
    """

    items: Optional[List[PlaylistItem]] = field(default_factory=None, repr=False)
