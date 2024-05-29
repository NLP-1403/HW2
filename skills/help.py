from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class Help(Skill):
    @match_regex(r'help')
    async def help(self, message):
        response = 'نکات زیر در رابطه با استفاده از ربات مفید است:'
        response += '\n'
        response += 'alh l'
        await message.respond(response)
