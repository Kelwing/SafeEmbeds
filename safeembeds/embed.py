from discord import Embed
from .limits import field_name_limit, field_value_limit


old_add_field = Embed.add_field


def new_add_field(*args, **kwargs):
    if len(kwargs['name']) > field_name_limit:
        kwargs['name'] = (kwargs['name'][:field_name_limit-3] + '...')
    if len(kwargs['value']) > field_value_limit:
        kwargs['value'] = (kwargs['value'][:field_value_limit-3] + '...')

    old_add_field(*args, **kwargs)
