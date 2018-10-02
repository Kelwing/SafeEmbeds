import discord
from .embed import new_add_field, new_set_footer, new_set_author


def patch_discord():
    discord.Embed.add_field = new_add_field
    discord.Embed.set_footer = new_set_footer
    discord.Embed.set_author = new_set_author
