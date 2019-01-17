""" format taken from ./manage.py dumpdata

fixture for app_spells Spell model

{
    "model": "app_spells.spell",
    "pk": 1,
    "fields": {
        "owner": 1,
        "casting_time": "1_ACTION",
        "casting_time_other": null,
        "component_material": null,
        "description": "You throw a bubble of acid at a creature you can see, or at two creatures within 5 feet of each other, and force them to pass a Dexterity save or take 1d6 acid damage.\r\n\r\nLeveling\r\nThis cantrip's damage die increases at levels 5, 11, and 17.",
        "duration": "INSTANTANEOUS",
        "duration_other": null,
        "level": 0,
        "name": "Acid Splash",
        "range": "60 feet",
        "component_verbal": true,
        "component_somatic": true,
        "concentration": false,
        "ritual": false,
        "school": "CON",
        "source_book": "PHB",
        "source_book_other": null,
        "source_page_number": 211,
        "spell_list": [
            1,
            2
        ]
    }
},
...
"""

import csv
import json

def get_boolean(row, key):
    if row.get(key) is None:
        print('row.get({}) is none'.format(key))
        print(row)
        return False

    if row.get(key) == '1':
        return True
    if row.get(key) == '0' or row.get(key) == '':
        return False

    print('row.get({}) has invalid value'.format(key))
    print(row)
    return False


def get_casting_time(row):
    ct = row.get('cast-time')
    if ct is not None:
        ct = ct.lower()

        if ct == '1 action':
            return '1_ACTION'
        elif ct == '1 bonus action':
            return '1_BONUS'
        elif ct == '1 reaction':
            return '1_REACTION'
        elif ct == '1 minute':
            return '1_MINUTE'
        elif ct == '10 minutes':
            return '10_MINUTES'
        elif ct == '1 hour':
            return '1_HOUR'
        elif ct == '8 hours':
            return '8_HOURS'
        elif ct == '12 hours':
            return '12_HOURS'
        elif ct == '24 hours':
            return '24_HOURS'

    return 'OTHER'


def get_duration(row):
    d = row.get('duration')
    if d is not None:
        d = d.lower()

        if d == 'instantaneous':
            return 'INSTANTANEOUS'

        elif d == '1 round':
            return '1_ROUND'

        elif d == '1 minute':
            return '1_MINUTE'

        elif d == '10 minutes':
            return '10_MINUTES'

        elif d == '1 hour':
            return '1_HOUR'

        elif d == '2 hours':
            return '2_HOURS'

        elif d == '8 hours':
            return '8_HOURS'

        elif d == '24 hours':
            return '24_HOURS'

        elif d == '1 day':
            return '24_HOURS'

        elif d == '7 days':
            return '7_DAYS'

        elif d == '10 days':
            return '10_DAYS'

        elif d == '30 days':
            return '30_DAYS'
        elif d == 'until dispelled':
            return 'UNTIL_DISPELLED'

    return 'OTHER'


def get_school(row):
    s = row.get('school')
    if s is not None:
        s = s[:3].upper()

        if s not in ['ABJ','CON','DIV','ENC','EVO','ILL','NEC','TRA',]:
            print("Row with invalid SCHOOL")
            print(row)
            return 'ERROR'

        return s


def get_source_book(row):
    s = row.get('source')
    if s is not None:
        s = s.upper()

        if s == '':
            return 'PHB'

        if s not in ['PHB','EE','SCAG','XGE','OTHER']:
            print("Row with invalid Source Book")
            print(row)
            return 'ERROR'

        return s
    return None

def get_spell_list(row):
    sl = []
    if get_boolean(row, 'bard-list'):
        sl.append(2)
    if get_boolean(row, 'cleric-list'):
        sl.append(3)
    if get_boolean(row, 'druid-list'):
        sl.append(4)
    if get_boolean(row, 'paladin-list'):
        sl.append(5)
    if get_boolean(row, 'ranger-list'):
        sl.append(6)
    if get_boolean(row, 'sorcerer-list'):
        sl.append(8)
    if get_boolean(row, 'warlock-list'):
        sl.append(9)
    if get_boolean(row, 'wizard-list'):
        sl.append(10)
    return sl


#open the csv file
f_csv = open('/home/damianocaprari/Downloads/DeD_5e_DB - Sheet4.csv', 'rU')

#read the csv
reader = csv.DictReader(f_csv)

# Parse the CSV into JSON
spells = []
for row in reader:
    pk = int(row.get('pk'))
    casting_time = get_casting_time(row)
    casting_time_other = row.get('cast-time') if casting_time == 'OTHER' else None
    component_material = row.get('material')
    description = row.get('description')
    duration = get_duration(row)
    duration_other = row.get('duration') if duration == 'OTHER' else None
    level = int(row.get('level'))
    name = row.get('name')
    range = row.get('range')
    component_verbal = get_boolean(row, 'verbal')
    component_somatic = get_boolean(row, 'somatic')
    concentration = get_boolean(row, 'conc')
    ritual = get_boolean(row, 'ritual')
    school = get_school(row)
    source_book = get_source_book(row)
    source_book_other = row.get('source') if source_book == 'OTHER' else None
    source_page_number = int(row.get('page')) if row.get('page') != '' else None
    spell_list = get_spell_list(row)

    spell = {
        "model": "app_spells.spell",
        "pk": pk,
        "fields": {
            "owner": 1,
            "casting_time": casting_time,
            "casting_time_other": casting_time_other,
            "component_material": component_material,
            "description": description,
            "duration": duration,
            "duration_other": duration_other,
            "level": level,
            "name": name,
            "range": range,
            "component_verbal": component_verbal,
            "component_somatic": component_somatic,
            "concentration": concentration,
            "ritual": ritual,
            "school": school,
            "source_book": source_book,
            "source_book_other": source_book_other,
            "source_page_number": source_page_number,
            "spell_list": spell_list
        }
    }

    spells.append(spell)

out = json.dumps(spells)
print("JSON parsed!")

# Save the JSON
f = open( '/home/damianocaprari/Desktop/AWMproject/spells_fixture.json', 'w')
f.write(out)
print("JSON saved!")
