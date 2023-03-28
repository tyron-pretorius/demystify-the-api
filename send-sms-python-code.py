import requests
import json

#Enter your information here
friends_numbers = ['+15743269202' ,  '+18582147182', '+12243880071']
friends_name = ['Tyron', 'Jana', 'Tarik' ]
your_name = 'Tyron'
your_telnyx_number = '+15743758096'
your_telnyx_key = 'KEYxxxx'

############ You don't need to change anything from here on down #################################

#Request Information
url = "https://api.telnyx.com/v2/messages"

headers = {
  'Authorization': 'Bearer ' + your_telnyx_key,
  'Content-Type': 'application/json'
}


for i in range(0, len(friends_numbers)):

    message = 'Hey ' + friends_name[i] + ', ' + your_name + ' here, not my usual number I know! I just sent my first SMS message via API using this new number and this awesome course: https://theworkflowpro.com/demystify-the-api/'

    payload = json.dumps({
        "from": your_telnyx_number,
        "to": friends_numbers[i],
        "text": message
    })
    response = requests.request("POST", url, headers=headers, data=payload)

    print('The value of i is: ', i)
    print('The value of friends_name[i] is: ', friends_name[i])
    print('The value of friends_numbers[i] is: ', friends_numbers[i])
    print('The value of your_name is: ', your_name)
    print('The value of your_telnyx_number is: ', your_telnyx_number)
    print('The value of message is: ', message)
    print(response.text)
