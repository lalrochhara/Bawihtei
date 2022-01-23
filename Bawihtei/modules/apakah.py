import random
from Bawihtei.events import register
from Bawihtei import telethn

APAKAH_STRING = ["Yes", 
                 "Not", 
                 "Possible", 
                 "Probably not", 
                 "It could be", 
                 "Probably not",
                 "Impossible",
                 "YNTKTS",
                 "Your father isn't broke",
                 "Is it true?",
                 "Just ask your mama kid"
                 ]


@register(pattern="^/is ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Give me a question 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
