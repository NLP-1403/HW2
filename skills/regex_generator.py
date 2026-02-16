"""
Opsdroid Skill: Regex Generator Command

This skill provides a chatbot command interface for the genetic algorithm-based
regex pattern generator. Users can submit example strings and receive optimized
regex patterns that match their examples.

Command Usage:
    /generate [POPULATION] [GENERATION]
    <example1>
    <example2>
    ...

Parameters:
    POPULATION (optional): Number of patterns per generation (10-100, default: 100)
    GENERATION (optional): Number of evolution cycles (1-30, default: 2)

Example:
    User message:
        /generate 100 10
        test@example.com
        demo@test.org
        
    Bot response:
        score: 0.95    [a-z]+@[a-z]+\.[a-z]{2,3}
        score: 0.90    \w+@\w+\.\w+
        score: 0.85    .+@.+\..+

Author: NLP Course Spring 2024, Sharif University of Technology
Reference: https://github.com/maojui/Regex-Generator
"""

from opsdroid.skill import Skill
from opsdroid.matchers import match_regex
import sys

import os
sys.path.append(os.getcwd())
from regex_generator.generator import generator


# https://github.com/maojui/Regex-Generator/tree/master?tab=readme-ov-file
class RegexGenerator(Skill):
    @match_regex(r'^/generate')
    async def regex_generator(self, message):
        message_split = message.text.split('\n')

        message_split_space = message_split[0].split(' ')
        if 1 < len(message_split_space) < 3 or len(message_split_space) > 3:
            await message.respond('لطفاً تعداد جمعیت و نسل را وارد کنید.')
            return
        elif len(message_split_space) == 3:
            try:
                POPULATION = int(message_split.split(' ')[1])
                GENERATION = int(message_split.split(' ')[2])
            except ValueError:
                await message.respond('لطفاً تعداد جمعیت و نسل را به صورت عدد وارد کنید.')
                return
        else:
            POPULATION = 100
            GENERATION = 2

        if not 30 >= GENERATION >= 1:
            await message.respond('لطفاً تعداد نسل را بین ۱ تا ۳۰ وارد کنید.')
            return
        if not 100 >= POPULATION >= 10:
            await message.respond('لطفاً تعداد جمعیت را بین ۱۰ تا ۱۰۰ وارد کنید.')
            return

        message_split = message_split[1:]
        if len(message_split) == 0:
            await message.respond('لطفاً ورودی را وارد کنید.')
            return

        result = generator(message_split, POPULATION, GENERATION)
        for fit, regex in sorted(set(result), key=lambda x: -x[0])[:3]:
            await message.respond(f'score: {fit}\t\t{regex}')
