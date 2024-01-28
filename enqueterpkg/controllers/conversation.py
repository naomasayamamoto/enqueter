"""Controller for speaking with enqueter"""
from enqueterpkg.models import enqueter

def enquete(enquete_topic=''):
    """Function to speak with enqueter"""
    enqueter_object = enqueter.Enqueter(enquete_topic)
    
    enqueter_object.hello()
    enqueter_object.recommend_to_user()
    enqueter_object.ask_user_recommend()
    enqueter_object.bye()

    