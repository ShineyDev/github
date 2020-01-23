"""
/github/enums/reaction.py

    Copyright (c) 2019-2020 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class Reaction:
    """
    Represents a GitHub reaction.

    https://developer.github.com/v4/enum/reactioncontent/
    """

    _dict = {
        "CONFUSED": "\U0001f615",
        "EYES": "\U0001f440",
        "HEART": "\U00002764",
        "HOORAY": "\U0001f389",
        "LAUGH": "\U0001f604",
        "ROCKET": "\U0001f680",
        "THUMBS_DOWN": "\U0001f44e",
        "THUMBS_UP": "\U0001f44d",
    }

    _dict_flipped = dict()

for (name, emoji) in Reaction._dict.items():
    setattr(Reaction, name, emoji)
    Reaction._dict_flipped[emoji] = name
