_requests = {}


def get_request(request_id):
    if request_id not in _requests:
        raise ValueError("request not found")
    return dict(_requests[request_id])

def update_request(request_id,new_status, approved_by=None):
    get_request(request_id)
    _requests[request_id]["status"] = new_status
    if approved_by is not None:
        _requests[request_id]["approved_by"] = approved_by 

def create_request(fellow_id, card_type):
    if not isinstance(fellow_id, str):
        raise ValueError("fellow_id must be text")
    if fellow_id.strip() == "":
        raise ValueError("fellow_id cannot be blank")

    if card_type not in ("visitor", "student", "staff"):
        raise ValueError("card_type must be visitor, student, staff")

    request_id = "A" + str(len(_requests) + 1).zfill(3)
    _requests [request_id] = {
        "id": request_id,
        "fellow_id": fellow_id.strip(),
        "card_type": card_type,
        "status": "requested",
        "approved_by": None,
    }

    return dict(_requests[request_id])
    






