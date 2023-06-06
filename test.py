import json
import urllib.request

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

#result_create_deck = invoke("createDeck", deck="Programming::vim")
result_list_of_decks = invoke("deckNames")
result_add_note = invoke("addNotes", notes=[{"deckName":"Programming::vim", "modelName":"Programming::vim", "fields": {"command":"dd", "action":"delete a line"}, "tags":[]}])

                            
#result_delete_deck = invoke("deleteDecks", decks=["Programming::vim"], cardsToo=True)
#result_delete_deck = invoke("deleteDecks", decks=["Programming"], cardsToo=True)

#print('after creating a deck: {}'.format(result_create_deck))
#print("after adding a note: {}".format(result_add_note))
#print("after deleting a deck: {}".format(result_delete_deck))
print('got list of decks: {}'.format(result_list_of_decks))
