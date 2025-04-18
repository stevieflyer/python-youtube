"""
These are i18n language and region related models.
"""

from typing import List, Optional

from pydantic import Field as field

from .base import BaseModel
from .common import BaseResource, BaseApiResponse


class I18nRegionSnippet(BaseModel):
    """
    A class representing the I18n region snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nRegions#snippet
    """

    gl: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)


class I18nRegion(BaseResource):
    """
    A class representing the I18n region info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nRegions#resource-representation
    """

    snippet: Optional[I18nRegionSnippet] = field(default=None)


class I18nRegionListResponse(BaseApiResponse):
    """
    A class representing the I18n region list response info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nLanguages/list#response_1
    """

    items: Optional[List[I18nRegion]] = field(default_factory=list, repr=False)


class I18nLanguageSnippet(BaseModel):
    """
    A class representing the I18n language snippet info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nLanguages#snippet
    """

    hl: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)


class I18nLanguage(BaseResource):
    """
    A class representing the I18n language info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nLanguages#resource-representation
    """

    snippet: Optional[I18nLanguageSnippet] = field(default=None)


class I18nLanguageListResponse(BaseApiResponse):
    """
    A class representing the I18n language list response info.

    Refer: https://developers.google.com/youtube/v3/docs/i18nLanguages/list#response_1
    """

    items: Optional[List[I18nLanguage]] = field(default_factory=list, repr=False)
