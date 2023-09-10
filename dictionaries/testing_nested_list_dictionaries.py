import json

data = [
    [
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
]

#print(data[1]['amount']['previous_price'])
print('Name: \t\t', data[0]['name'])
print('Amounts: \t', 'Current:',data[1]['amount']['previous_price'], '\n\t\t\t Previous:', data[1]['amount']['new_data'])
print('Daily\nVolume: \t', data[2]['Volume'])