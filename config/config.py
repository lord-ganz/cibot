# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from os import getenv
from distutils.util import strtobool

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH", "1f217c5d594a79ce7576802dfa0688f1"))
API_ID = int(getenv("API_ID", "14200817"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001687155877]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.2.0@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "CilikProject")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX3hyWUNTZmw3UzEyc0NzNnZkcVo0OFkzUzNWenJ5ZTFzOVNhWg==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "CilikSupport")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))

STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQAJEUEGCY3ZxtzUZRwfoDd0uOwmeMrUU_qTxQV6PvgS4Mqm-5medxJsuY4ee38_tNZnaN1SYgBTJ6hbAcIK3aZHDqSPtUozCSYS0Op9x1YABLt19bVr5ld409gcbnZIr1zDNm_LDOJQlbENDngmBKuUKt4GOeekxcjDL2uecTmd-4PshPISpAlf9TQBHLeSB5iWCqK_KmjJ5IpcLJSR7BMsINDQDqFFZpvkm5hwfkkUEaRjqCIAjLN1xWaSrsNAbQ4ZVOE2rNIw3awvMpPet7ZrC9kDgweqKw1jHXNk_OFv0b7YUHQezQAdmk_QxbnOyD_LesjqnyEv-CDD4J-lJtCggAAAAE968rKAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
