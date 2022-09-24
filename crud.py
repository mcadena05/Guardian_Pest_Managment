from model import db, User, connect_to_db
import requests
import json

api_clean = []

response = requests.get(f'https://api.yelp.com/v3/businesses/search/+19155000159')
api_clean = json.loads(str(response.content, 'UTF-8'))

def get_users():
    """Return all users."""

    return User.query.all()

# def create_review():
#     """Create and return a new user."""
#     # response = requests.get('https://api.yelp.com/v3/businesses/search/+19155000159' +'.json')
#     # print(response.json())
#     # yelp_api_response = response.json()

#     # review = yelp_api_response["review"]

#     response =requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&key=AIzaSyDlEGh9epUzeXpwE6GVKM28Lg8zrHWUvxs'+'.json')
#     print(response.json())
#     places_api_response = response.json()

#     review = places_api_response["review"]

    
#     return review

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
