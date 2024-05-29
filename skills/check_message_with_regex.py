from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

import os
import sys
sys.path.append(os.getcwd())
from new_regex.main import check_custom_regex


class CheckMessageWithRegex(Skill):
    @match_regex(r'^/checkone')
    async def check_message_with_regex(self, message):
        message_split = message.text.split('\n\n')
        if len(message_split) < 2:
            await message.respond('لطفاً پیام را وارد کنید.')
            return

        message_text = message_split[0].split('\n')
        if len(message_text) < 2:
            await message.respond('لطفاً پیام را وارد کنید.')
            return
        message_text = '\n'.join(message_split[0].split('\n')[1:])
        regex = message.text.split('\n\n')[1]

        match = check_custom_regex(message_text, regex)
        if match:
            await message.respond('مطابقت یافت شد.')
        else:
            await message.respond(f'مطابقت یافت نشد.')

