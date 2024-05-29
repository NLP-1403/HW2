from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import sys

import os
sys.path.append(os.getcwd())
from regex_generator.generator import generator


# https://github.com/maojui/Regex-Generator/tree/master?tab=readme-ov-file
class RegexGenerator(Skill):
    @match_regex(r'^/شروع')
    async def regex_generator(self, message):
        POPULATION = 100
        GENERATION = 2

        message_split = message.text.split('\n')[1:]
        if len(message_split) == 0:
            await message.respond('لطفاً ورودی را وارد کنید.')
            return

        result = []
        result = generator(message_split, POPULATION, GENERATION)
        for fit, regex in sorted(set(result), key=lambda x: -x[0])[:20]:
            await message.respond(f'{fit}\t\t{regex}')
