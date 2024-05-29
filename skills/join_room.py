from opsdroid.events import JoinRoom, Message
from opsdroid.matchers import match_event
from opsdroid.skill import Skill


class JoinRoom(Skill):
    def __init__(self, opsdroid, config):
        super(JoinRoom, self).__init__(opsdroid, config)

    @match_event(JoinRoom)
    async def greet(self, event):
        user_name = event.user_id
        await event.respond(Message(text=f'سلام {user_name} 👋🏻\n'
                                         f'من یک ربات هوشمند برای دسته‌بندی اطّلاعاتی همچون آدرس و شماره‌ی تلفن هستم. همچنین قابلیت‌های خفن بیش‌تری هم دارم. شما می‌توانید با اجرای help/ لیست کامل قابلیت‌های من را ببینید.\n'
                                         f'امیدوارم که بتوانم به شما کمک کنم. 🔥🔥',
                                    target=event.target))
