import csv
import sys

import requests

import config


YELP_API_PATH = 'https://api.yelp.com'

SEARCH_API_PATH = '/v3/graphql'

FIELDS = [
    'id',
    'name',
    'phone',
    'location.address1',
    'location.address2',
    'location.city',
    'location.country',
    'price',
    'rating',
    'state',
    'review_count',
    'url',
    'longitude',
    'latitude',
]

QUERY = """{{
    search(term: "{term}",
        categories: "{categories}",
        location: "{location}",
        radius: {radius},
        locale: "{locale}",
        limit: {limit},
        offset: {offset}) {{
        total
        business {{
            id
            name
            phone
            location {{
                address1
                address2
                city
                state
                country
            }}
            price
            rating
            review_count
            url


        }}
    }}
}}
"""


class YelpAPIError(Exception):
    pass

def make_search_request(term, category, location, limit=50, offset=0):
    params = {
        "term": term,
        "categories": category,
        "location": location,
        "radius": 6000,
        "locale": "en_US",
        "limit": limit,
        "offset": offset,
    }
    data = QUERY.format(**params)
    headers = {
        "Authorization": "Bearer {}".format(config.YELP_API_KEY),
        "Content-Type": "application/graphql",
    }
    response = requests.post('{}{}'.format(
        YELP_API_PATH, SEARCH_API_PATH), data=data, headers=headers)
    if response.status_code != 200:
        raise YelpAPIError(response.text)
    return response.json()



def search(term, category, location):
    offset = 0
    limit = 50
    total = 5000
    entries = []
    call_count = 0
    while offset < min(1000, total):
        call_count += 1
        print("Page #{}".format(call_count))
        json_output = make_search_request(
            term=term,
            category=category,
            location=location,
            limit=min(total - offset, limit),
            offset=offset
        )
        result = json_output['data']['search']
        total = result['total']
        entries += result['business']
        offset += limit
    return entries


def entry_to_row(entry, fields):
    values = []
    for field_path in fields:
        value = get_field_for_path(entry, field_path)
        values.append(value)
    return values


def get_field_for_path(entry, field_path):
    result = entry
    for part in field_path.split('.'):
        result = result.get(part, '')
        if not result:
            break
    return result


def get_neighborhoods(self, response):
    result = ["", ""]
    neighborhoods = response.business.location.neighborhoods
    if neighborhoods is not None:
        result[0] = neighborhoods[0]
        if len(neighborhoods) > 1:
            result[1] = neighborhoods[1]
        return result

def get_categories(self, response):
        result = ["", ""]
        categories = response.business.categories
        if categories is not None:
            result[0] = categories[0][1]
            if len(categories) > 1:
                result[1] = categories[1][1]
        return result


def get_business_dict(self, response):
        business = response.business

        try:
            if business.location.coordinate.latitude:
                latitude = business.location.coordinate.latitude
        except:
            latitude = None

        try:
            if business.location.coordinate.longitude:
                longitude = business.location.coordinate.longitude
        except:
            longitude = None

def run():
    id_cache = set()
    count = 0

    print('Starting search ...')

    with open(config.OUTPUT_FILENAME, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(FIELDS)

        for location in config.SEARCH_LOCATIONS:
            print("Searching for {} ({}) in '{}'".format(
                config.SEARCH_TERM, config.SEARCH_CATERGORIES, location))
            entries = search(config.SEARCH_TERM,
                             config.SEARCH_CATERGORIES, location)
            print("Found {} results in {}".format(len(entries), location))
            for entry in entries:
                if entry['id'] not in id_cache:
                    id_cache.add(entry['id'])
                    values = entry_to_row(entry, FIELDS)
                    if sys.version_info[0] < 3:
                        values = [unicode(val).encode('utf-8')
                                  for val in values]
                    writer.writerow(values)
                    count += 1
    print('-----------------------')
    print('Done! A total of {} entries written to {}'.format(count, config.OUTPUT_FILENAME))


if __name__ == "__main__":
    run()
