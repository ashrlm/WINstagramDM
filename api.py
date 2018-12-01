import json

from InstagramAPI import InstagramAPI

class User: #Setup custom user class
    def __init__(self, usr_name, password):
        self.name = usr_name
        self.api = InstagramAPI(usr_name, password)
        if not self.api.login():
            raise ValueError("Couldn't login")

        InstagramAPI.USER_AGENT = 'Instagram 39.0.0.19.93 Android (5000/5000.0; 1dpi; 1x1; noname; noname; noname; noname)'
        #Setup custom UA to ensure reading dms allowed

    def sendMessage(self, target_user, msgText):
        if type(target_user[0]) != 'int':
            target_user = self.api.searchUsername(target_user)
            try:
                target_user = self.api.LastJson["user"]["pk"]
            except:
                return ValueError("Invalid User")

        target_user = str(target_user)

        target_user = '[[{}]]'.format(','.join([target_user]))
        url = 'direct_v2/threads/broadcast/text/'

        data = {
            'text': msgText,
            '_uuid': self.api.uuid,
            '_csrftoken': self.api.token,
            'recipient_users': target_user,
            '_uid': self.api.username_id,
            'action': 'send_item',
            'client_context': self.api.generateUUID(True)}

        return self.api.SendRequest(url, data)

    def getChats(self):
        self.api.getv2Inbox()
        content = json.loads(self.api.LastResponse.content)
        return content['inbox']['threads']

    def getMessages(self, chat_id):
        pass