import discord
from .embed import new_add_field


def patch_discord():
    discord.Embed.add_field = new_add_field
