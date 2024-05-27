from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class Test(Skill):
    @match_regex(r'hi')
    async def test(self, message):
        await message.respond('Hey')
