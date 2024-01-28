import configparser

from enqueterpkg.controllers import conversation

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

enquete_topic = config_ini.get('DEFAULT', 'Enquete_topic')
conversation.enquete(enquete_topic)
