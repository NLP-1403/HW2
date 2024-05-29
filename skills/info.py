from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import os
import sys

sys.path.append(os.getcwd())
from info.extractor import Extractor


class Info(Skill):
    @match_regex(r'^/info\s*\d*')
    async def info(self, message):
        message_split = message.text.split('\n')
        try:
            number = message_split[0].split(' ')[1]
            number = number.strip() if number.isdigit() else None
        except IndexError:
            number = None

        message_split = message_split[1:]
        if len(message_split) == 0:
            await message.respond('لطفاً ورودی را وارد کنید.')
            return

        if number is None:
            await message.respond(Extractor(message_split))
        elif number.isdigit():
            await message.respond(Extractor(message_split, number))
        else:
            await message.respond('لطفاً یک عدد وارد کنید.')
