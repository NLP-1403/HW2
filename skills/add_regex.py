"""
Opsdroid Skill: Add Custom Regex Pattern

This skill allows users to store custom regex patterns in the database with
unique names. These patterns can later be used to test messages for matches.

Command Usage:
    /add <pattern_name>
    <regex_pattern>

Parameters:
    pattern_name: Unique identifier for the regex pattern
    regex_pattern: Regular expression to store (can be multi-line)

Features:
    - Prevents duplicate pattern names
    - Stores patterns persistently in SQLite database
    - Patterns available for testing via /checkall command

Example:
    User message:
        /add postal_code
        \d{10}
        
    Bot response:
        رجکس postal_code با موفقیت اضافه شد.
        (Pattern 'postal_code' successfully added)

Error Cases:
    - Missing pattern name: "لطفاً نام را وارد کنید."
    - Duplicate name: "رجکس {name} قبلاً اضافه شده است."

Author: NLP Course Spring 2024, Sharif University of Technology
"""

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
