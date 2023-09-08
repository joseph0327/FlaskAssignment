import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    #Converting the list to a set for faster membership tests and the removal of duplicate elements
    set_fave_numbers_1 = set(fave_numbers_1)
    
    # Use set intersection to check for matching elements
    intersection = set_fave_numbers_1.intersection(fave_numbers_2)
    
    # If the intersection is not empty, there are matching elements
    # In Python, an empty set is considered False, and a non-empty set is considered True.
    return bool(intersection)


