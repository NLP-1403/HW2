from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import json

import os
import sys
sys.path.append(os.getcwd())
from new_regex.main import check_message_patterns


class CheckWithNewRegexes(Skill):
    @match_regex(r'^/checkall')
    async def check_with_new_regexes(self, message):
        message_split = message.text.split('\n')[1:]
        if len(message_split) == 0:
            await message.respond('لطفاً پیام را وارد کنید.')
            return

        message_split = '\n'.join(message_split)
        matches = check_message_patterns(message_split)
        if not matches or len(matches) == 0:
            await message.respond('هیچ موردی یافت نشد.')
        else:
            await message.respond(json.dumps(matches, ensure_ascii=False, indent=4))
