from __future__ import annotations

from typing import TYPE_CHECKING

from tortoise import Model, fields

from meetifyr.tortoise_models.base_model import BaseModel
from meetifyr.tortoise_models.meeting import MeetingModel

if TYPE_CHECKING:
    from meetifyr.tortoise_models.participant_date import ParticipantDateModel


class ParticipantModel(BaseModel, Model):
    name = fields.CharField(max_length=255)
    meeting: fields.ForeignKeyRelation[MeetingModel] = fields.ForeignKeyField(
        "models.MeetingModel",
        related_name="participants",
        db_constraint=False,
        on_delete=fields.CASCADE,
        to_field="url_code",
        index=True,
    )
    meeting_id: str
    participant_dates: list[ParticipantDateModel]  # 추가

    class Meta:
        table = "participants"

    @classmethod
    async def create_participant(cls, name: str, meeting_url_code: str) -> ParticipantModel:
        return await cls.create(name=name, meeting_id=meeting_url_code)
