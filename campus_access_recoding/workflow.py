from requests_store import get_request, update_request

def approve_request( request_id, approved_by):
    request = get_request(request_id)
    
    if not isinstance(approved_by, str):
        raise ValueError("approved_by must be string")
    if approved_by.strip() == "":
        raise ValueError("approve_by cannot be blank")
        
    if request["status"].strip() != "requested":
        raise ValueError("only a requested request can be approved")

    update_request(request_id, "approved", approved_by.strip())
    return get_request(request_id)

def issue_card(request_id):
    request = get_request(request_id)

    if request["status"] != "approved":
        raise ValueError("only an approved request can be issued ")
    if not request["approved_by"] or request["approved_by"].strip() == "":
        raise ValueError("cannot issue a card without an approver")                   
    
    update_request(request_id, "issued")
    return get_request(request_id)    

def return_card(request_id):
    request = get_request(request_id)

    if request["status"] != "issued":
        raise ValueError("only an issued card can be returned")

        update_request(request_id, "returned")
        return get_request(request_id)
        
