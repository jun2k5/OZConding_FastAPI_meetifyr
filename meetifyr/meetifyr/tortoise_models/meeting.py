from __future__ import annotations

from tortoise import Model, fields

from meetifyr.tortoise_models.base_model import BaseModel


class MeetingModel(BaseModel, Model):
    url_code = fields.CharField(max_length=255, unique=True)

    class Meta:
        table = "meetings"

    @classmethod
    async def create_meeting(cls, url_code: str) -> MeetingModel:
        return await cls.create(url_code=url_code)

    # TEXT는 길이가 길다. 인덱스가 불가능하다
    # VARCHAR은 길이가 짧다. 인덱스가 가능하다.
    # MYSQL은 VARCHAR의 길이가 255보다 낮아도 255의 공간을 사용한다.

    # 응집성

    @classmethod
    async def get_by_url_code(cls, url_code: str) -> MeetingModel | None:
        return await cls.filter(url_code=url_code).get_or_none()
