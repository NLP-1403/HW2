from opsdroid.events import UserInvite, JoinRoom
from opsdroid.matchers import match_event
from opsdroid.skill import Skill


class AcceptInvite(Skill):
    @match_event(UserInvite)
    async def accept_invite(self, invite):
        if isinstance(invite, UserInvite):
            await invite.respond(JoinRoom())
        else:
            print("I don't know how to respond to this event.")
            await invite.respond("I don't know how to respond to this event.")
