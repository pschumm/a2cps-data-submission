# Generate IDs for use in testing

from dataforge.ids import generate_ids
import uuid

# Locally-assigned IDs
ids = generate_ids(n=250, prefix='A2CPS', offset=100, length=3, check_digit=True)
with open('ids/ids.csv', 'w') as file:
    file.write('participant_id\n')
    file.write('\n'.join(ids))

# Pseudo-GUIDs
guids = ['record_id,guid']
for id in ids:
    guids.append(f'{id},{str(uuid.uuid4())}')
with open('ids/guids.csv', 'w') as file:
    file.write('\n'.join(guids))
