import json

data = [
    {
        "name": "Bitcoin (BTC)"
    },
    {
        "amount": {
            "previous_price": "$56k",
            "new_data": "$23k"
        }
    },
    {
        "Volume": "$657B"
    }
]


#print(data[1]['amount']['previous_price'])
print('Name: ', data[0]['name'])
print('Amounts: ', data[1]['amount']['previous_price'], data[1]['amount']['new_data'])
print('Daily Volume: ', data[2]['Volume'])