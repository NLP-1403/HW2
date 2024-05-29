from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

import os
import sys
sys.path.append(os.getcwd())
from new_regex.main import add_regex


class AddRegex(Skill):
    @match_regex(r'^/add')
    async def add_regex(self, message):
        message_split = message.text.split('\n')
        if len(message_split) < 1:
            await message.respond('لطفاً نام و رجکس را وارد کنید.')
            return

        name = message_split[0].split(' ')[1:]
        name = ' '.join(name)
        if not name:
            await message.respond('لطفاً نام را وارد کنید.')
            return

        regex = message_split[1:]
        regex = '\n'.join(regex)

        status = add_regex(name, regex)
        if not status:
            await message.respond(f'رجکس {name} قبلاً اضافه شده است.')
        else:
            await message.respond(f'رجکس {name} با موفقیت اضافه شد.')
