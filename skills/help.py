from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class Help(Skill):
    @match_regex(r'help')
    async def help(self, message):
        await message.respond('You asked for help!')
