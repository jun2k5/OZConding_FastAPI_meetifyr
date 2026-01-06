from pydantic import BaseModel

from meetifyr.dtos.frozen_config import FROZNEN_CONFIG

class GetMeetingResponse(BaseModel):
    model_config = FROZNEN_CONFIG

    url_code: str
