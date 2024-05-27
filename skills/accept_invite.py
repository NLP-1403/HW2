from opsdroid.events import UserInvite, JoinRoom
from opsdroid.matchers import match_event
from opsdroid.skill import Skill


class AcceptInvite(Skill):
    @match_event(UserInvite)
    async def accept_invite(self, invite):
        if isinstance(invite, UserInvite):
            await invite.respond(JoinRoom())
            # await invite.respond(f'سلام 👋🏻\n'
            #                      f'من یک ربات هوشمند برای دسته‌بندی اطّلاعاتی همچون آدرس و شماره‌ی تلفن هستم. همچنین قابلیت‌های خفن بیش‌تری هم دارم. شما می‌توانید با اجرای //کمک لیست کامل قابلیت‌های من را ببینید.\n'
            #                      f'امیدوارم که بتوانم به شما کمک کنم. 🔥🔥')
        else:
            print("I don't know how to respond to this event.")
            await invite.respond("I don't know how to respond to this event.")
