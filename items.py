ITEMS = {
    1:{'name': 'Healing potion',
       'type': 'consumable',
       'stackable': True,
       'max_stack': 5,
       'stats': {'health_restore': 5},
       'value': 5},
}

def get_item(item_id):
    return ITEMS[item_id].copy() if item_id in ITEMS else None