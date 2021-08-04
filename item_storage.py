'''
Hello you fellow github surfer if you have just stumbled upon this project then hello. *Insert Wave*
This is just a fun little script I made for fun if you have some feedback my email is open to you're sudjections so feel free to email me

Email: zackery.smith@hsdgreenbush.org

This code will not have a licence on it because of it's small size and simplicicy making it not rally worth that GNU3 GPL stamp
With that being said enjoy the bumpy ride that is my code
'''

import difflib

store_items = ['apples', 'apricots', 'bananas', 'blueberries', 'grapefruits', 'honeydew', 'kiwifruit', 'limes', 'mandarins', 'mangoes', 'nectarines', 'oranges', 'passionfruit', 'peaches', 'pears', 'plums', 'raspberries', 'rockmelons', 'strawberries', 'watermelons']
store_items_dict = {'fruits':{'apples':2.99, 'apricots':1.99, 'bananas':4.99, 'blueberries':2.99, 'grapefruits':3.50, 'honeydew':.99, 'kiwi:fruit':2.50, 'limes':4.99, 'mandarins':6.9, 'mangoes':2.99, 'nectarines':2.50, 'oranges':5.00, 'passionfruit':1.99, 'peaches':3.99, 'pears':2.99, 'plums':2.99, 'raspberries':1.99, 'rockmelons':4.00, 'strawberries':4.99, 'watermelons':6.99}}

def search_for_item(search, store_items):
    index = -1
    search.lower()
    for i in store_items:
        index += 1
        if search == i:
            return 'Found {item} at index {index}'.format(item=search, index=index)
        elif bool(difflib.get_close_matches(search, store_items)) is True:
            return 'That item was not found, {close_match} is the closest match to {item}'.format(item=search, close_match=difflib.get_close_matches(search, store_items).pop())
    return 'Sorry, that item does not exist'

def search_for_catagory(search, store_items_dict):
    index = -1
    for i in list(store_items_dict.keys()):
        index += 1
        if list(store_items_dict.keys())[index] == search:
            return f'Found {search} at index {index}'
    if bool(difflib.get_close_matches(search, store_items_dict.keys())) is True:
        return 'Sorry the closest match to {search} is {close_match}'.format(search=search, close_match=difflib.get_close_matches(search, store_items_dict.keys()).pop())
    return 'Sorry, that catagory does not exist'

def check_value(search, store_items_dict):
    for group in store_items_dict.keys():
        if store_items_dict.get(group, {}).get(search):
            return '{item} are ${price} and are grouped in the {group} catagory'.format(price=store_items_dict.get(group, {}).get(search), group=group, item=search)
    return '{item} was not found in are food groups sorry :('.format(item=search)
#print(search_for_item(input(), store_items))
#print(search_for_catagory(input(), items_dict))
print(check_value(input(), store_items_dict))
