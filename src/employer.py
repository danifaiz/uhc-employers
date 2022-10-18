from flask import Blueprint
from flask import request

from src.services.uhc_service import fetch_uhc_employers, search_uhc_employers

employer = Blueprint("employer", __name__ , url_prefix="/api/v1/employer")

@employer.get('sync')
def sync_data():
    fetch_uhc_employers()
    return { "message" : 'success' }

@employer.get('/')
def search():
    searchString = request.args.get('search')
    searchType = request.args.get('type')
    data = search_uhc_employers(searchType, searchString)
    return { "data" : data }
