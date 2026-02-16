"""
Opsdroid Skill: Information Extraction Command

This skill provides a chatbot interface for extracting structured information
from text messages, including emails, phone numbers, addresses, and message
classification.

Command Usage:
    /info [THRESHOLD]
    <text line 1>
    <text line 2>
    ...

Parameters:
    THRESHOLD (optional): Character count threshold for message classification
                         (default: 100). Messages shorter than this are classified
                         as "short", otherwise "long".

Output Format:
    تلفن (Phone Numbers):
        ثابت (Landline): [list]
        همراه (Mobile): [list]
    ایمیل (Email): [list]
    نشانی‌ها (Addresses): [list]
    طبقه‌بندی پیام (Classification): short/long

Example:
    User message:
        /info 50
        Email: test@example.com
        Phone: 09123456789
        
    Bot response:
        تلفن
            همراه: 09123456789
        ایمیل: test@example.com
        طبقه‌بندی پیام: پیام کوتاه

Author: NLP Course Spring 2024, Sharif University of Technology
"""

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
            # result = json.dumps(result, ensure_ascii=False, indent=4)
            await message.respond(result)
