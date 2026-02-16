"""
Opsdroid Skill: Check Custom Regex Pattern

This skill validates a custom regex pattern against a message without storing
the pattern in the database. Useful for one-time pattern testing.

Command Usage:
    /checkone
    <text to test>
    
    <regex pattern>

Note: Use double newline (blank line) to separate text from regex pattern.

Features:
    - Tests custom regex without database storage
    - Boolean match result (found/not found)
    - Instant validation for ad-hoc patterns

Example:
    User message:
        /checkone
        Test email: test@example.com
        
        \w+@\w+\.\w+
        
    Bot response (match found):
        مطابقت یافت شد.
        (Match found)
        
    Bot response (no match):
        مطابقت یافت نشد.
        (No match found)

Related Commands:
    - /add - Store pattern permanently
    - /checkall - Test against all stored patterns

Author: NLP Course Spring 2024, Sharif University of Technology
"""

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

