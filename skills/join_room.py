from opsdroid.skill import Skill
from opsdroid.matchers import match_event
from opsdroid.events import JoinRoom


class NewJoinSkill(Skill):
    @match_event(JoinRoom)
    async def new_join(self, event):
        await event.respond(f"Welcome {event.user} to the room!")
