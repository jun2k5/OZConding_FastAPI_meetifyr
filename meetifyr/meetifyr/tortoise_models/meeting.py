from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from tortoise import Model, fields

from meetifyr.tortoise_models.base_model import BaseModel

if TYPE_CHECKING:
    from meetifyr.tortoise_models.participant import ParticipantModel


class MeetingModel(BaseModel, Model):
    url_code = fields.CharField(max_length=255, unique=True)
    title = fields.CharField(max_length=255, default="")
    location = fields.CharField(max_length=255, default="")
    start_date = fields.DateField(null=True)
    end_date = fields.DateField(null=True)
    participants: list[ParticipantModel]

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
        return (
            await cls.filter(url_code=url_code)
            .prefetch_related("participants", "participants__participant_dates")
            .get_or_none()
        )

    @classmethod
    async def update_start_and_end(cls, url_code: str, start_date: date, end_date: date) -> None:
        await cls.filter(url_code=url_code).update(start_date=start_date, end_date=end_date)

    @classmethod
    async def update_title(cls, url_code: str, title: str) -> int:
        return await cls.filter(url_code=url_code).update(title=title)

    @classmethod
    async def update_location(cls, url_code: str, location: str) -> int:
        return await cls.filter(url_code=url_code).update(location=location)
