from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import os
import sys
sys.path.append(os.getcwd())
from regex_generator.generator import generator


class RegexGenerator(Skill):
    @match_regex(r'^/شروع')
    async def hello(self, message):
        POPULATION = 100
        GENERATION = 2

        message_split = message.text.split('\n')[1:]
        if len(message_split) == 0:
            await message.respond('لطفا ورودی را وارد کنید')
            return
        target = message_split

        result = []
        result = generator(target, POPULATION, GENERATION)
        for fit, regex in  sorted( set(result),key=lambda x : -x[0] )[:20]:
            print(f'{fit}\t\t{regex}')
            await message.respond(f'{fit}\t\t{regex}')