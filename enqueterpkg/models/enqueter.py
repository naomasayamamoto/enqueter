"""Defined a enqueter model"""
from enqueterpkg.models import data_rw
from enqueterpkg.views import output


class Enqueter(object):
    """Base model for Enqueter"""
    
    def __init__(self, enquete_topic='', user_name='', speak_color='green'):
        self.enquete_topic = enquete_topic
        self.user_name = user_name
        self.speak_color = speak_color
        self.data_rw = data_rw.DataRW(self.enquete_topic + '_enquete.csv')
        
    def hello(self):
        while True:
            template = output.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute())
        
            if user_name:
                self.user_name = user_name.title()
                break
    
    def recommend_to_user(self):
        """Show recommended and ask whether user like it or not."""
        template = output.get_template('recommending.txt', self.speak_color)

        for data in self.data_rw.stored_data():
            if not data:
                break
            recommend = data['RECOMMEND']

            is_yes = input(template.substitute({
                'enquete_topic': self.enquete_topic,
                'recommend': recommend
                }))
            if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
               self.data_rw.update(recommend)

    def ask_user_recommend(self):
        """Collect user's recommend."""
        while True:
            template = output.get_template('which_recommend.txt', self.speak_color)

            users_recommend = input(template.substitute({
                'user_name': self.user_name,
                'enquete_topic': self.enquete_topic
            }))
            if users_recommend:
                break
        
        self.data_rw.write_data(users_recommend)

    def bye(self):
        template = output.get_template('bye.txt', self.speak_color)
        print(template.substitute({'user_name': self.user_name}))
        