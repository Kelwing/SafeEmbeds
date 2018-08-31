# Safe Embeds
Provides 400 safety to embeds in Discord.  It works by monkey patching the add_field method of the Embed class to truncate the inputs down to 1024 characters.

## Example
```python
import discord
from safeembeds import patch_discord

patch_discord()

bot = discord.Bot()
```

Thats all there is to it.  After calling patch_discord, all future Embeds that are created with automatically truncate inputs to fit within the Discord API limits.