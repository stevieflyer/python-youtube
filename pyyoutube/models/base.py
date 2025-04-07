from typing import Any, ClassVar

from pydantic import BaseModel as PydanticBaseModel, ConfigDict


class BaseModel(PydanticBaseModel):

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    _json: ClassVar[dict[str, Any]] = {}

    @classmethod
    def from_dict(cls, kvs: dict[str, Any], *, infer_missing: bool = False):
        instance = cls.model_validate(kvs, strict=False)
        setattr(cls, "_json", kvs)
        return instance

    def to_dict_ignore_none(self) -> dict[str, Any]:
        return {k: v for k, v in self.model_dump().items() if v is not None}
