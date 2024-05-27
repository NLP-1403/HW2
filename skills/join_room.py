from opsdroid.events import JoinRoom
from opsdroid.matchers import match_event
from opsdroid.skill import Skill


class JoinRoom(Skill):
    @match_event(JoinRoom)
    async def join_room(self, event):
        event.respond("سلام 👋🏻\n")
