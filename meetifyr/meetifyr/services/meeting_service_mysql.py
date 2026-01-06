import uuid

from meetifyr.tortoise_models.meeting import MeetingModel
from meetifyr.utils.base62 import Base62


async def service_create_meeting_mysql() -> MeetingModel:
    return await MeetingModel.create_meeting(Base62.encode(uuid.uuid4().int))
