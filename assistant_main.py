from rule_based import *
from ml_brain import *

def get_response(text):
    response = handle_rule_based(text)
    if response:
        return response
    
    return predict_intent(text)