import sys

import json
import requests

from postamat import Postamat


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print()
        print('The query must contain at least one argument', '\n')
        print('Examples: "python run.py 10(id number)" or lists of ids: "python run.py 106,10,116"', '\n')
        sys.exit()
    else:
        ids = [i.strip() for i in sys.argv[1].split(',')]

    for id_num in ids:
        url = 'https://api.tport.online/v2/public-stations/' + str(id_num)
        response = requests.get(url)
        data = json.loads(response.text)

        if data.get('detail'):  # If id was not defined, dict has only one key 'detail' with value "Не найдено."
            print(f'Undefined ID {id_num} Please enter correct ID number')

        else:
            instance = Postamat(data['id'], data['address'], data['is_automated'], data['accept_cash'], data['accept_card'],
                                name=data['name'], status=data['status'], working_hours=data["working_hours"])
            print(f'Postamat id = {instance.id}, Name = {instance.name}, status = {instance.status}, {instance.is_working()}')


