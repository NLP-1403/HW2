from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import json

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
        if number is not None and not number.isdigit():
            await message.respond('لطفاً یک عدد وارد کنید.')
            return
        else:
            result = Extractor(message_split)
            result = json.dumps(result, ensure_ascii=False, indent=4)
            await message.respond(result)
