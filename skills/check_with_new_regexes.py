"""
Opsdroid Skill: Check All Stored Patterns

This skill tests a message against all regex patterns stored in the database
and returns all matches found.

Command Usage:
    /checkall
    <text to test>

Features:
    - Tests message against all stored patterns simultaneously
    - Returns JSON output with pattern names and matched values
    - Useful for batch pattern validation

Example:
    User message:
        /checkall
        My postal code is 1234567890 and email test@example.com
        
    Bot response (if patterns exist):
        {
            "postal_code": "1234567890",
            "email": "test@example.com"
        }
        
    Bot response (no matches):
        هیچ موردی یافت نشد.
        (No matches found)

Related Commands:
    - /add - Add new patterns to database
    - /checkone - Test a single custom regex pattern

Author: NLP Course Spring 2024, Sharif University of Technology
"""

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
