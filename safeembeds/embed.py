from discord import Embed
from .limits import field_name_limit, field_value_limit, footer_text_limit, author_name_limit


old_add_field = Embed.add_field
old_set_footer = Embed.set_footer
old_set_author = Embed.set_author


def new_add_field(*args, **kwargs):
    if len(kwargs['name']) > field_name_limit:
        kwargs['name'] = (kwargs['name'][:field_name_limit-3] + '...')
    if len(kwargs['value']) > field_value_limit:
        kwargs['value'] = (kwargs['value'][:field_value_limit-3] + '...')

    old_add_field(*args, **kwargs)


def new_set_footer(*args, **kwargs):
    if len(kwargs['text']) > footer_text_limit:
        kwargs['text'] = (kwargs['text'][:footer_text_limit - 3] + '...')

    old_set_footer(*args, **kwargs)


def new_set_author(*args, **kwargs):
    if len(kwargs['name']) > author_name_limit:
        kwargs['name'] = (kwargs['name'][:author_name_limit - 3] + '...')

    old_set_author(*args, **kwargs)
