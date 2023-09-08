from flask import Blueprint, request, jsonify

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    query_params = request.args.to_dict()
    matching_users = filter_users(query_params)
    sorted_users = sort_users(matching_users, query_params)
    return jsonify({"results": sorted_users}), 200

def filter_users(query_params):
    filtered_users = []

    for user in USERS:
        match = False

        if "id" in query_params and user["id"] == query_params["id"]:
            match = True
        if "name" in query_params:
            if query_params["name"].lower() in user["name"].lower():
                match = True
        if "age" in query_params and str(user["age"]) == query_params["age"]:
            match = True
        if "occupation" in query_params:
            if query_params["occupation"].lower() in user["occupation"].lower():
                match = True

        if match:
            filtered_users.append(user)

    return filtered_users



def sort_users(users, query_params):
    priority_order = ["id", "name", "age", "occupation"]

    def matching_priority(user):
        priority_values = [-priority_order.index(field) if query_params.get(field) == user.get(field) else len(priority_order) for field in priority_order]
        return priority_values

    sorted_users = sorted(users, key=matching_priority)

    return sorted_users

