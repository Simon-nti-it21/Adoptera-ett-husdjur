"""
    This module contains a dictionary of pets, categorized by type (dogs, cats, rabbits).
    Each pet is represented as a dictionary with the following attributes:
    - name: The name of the pet.
    - age: The age of the pet.
    - breed: The breed of the pet.
    - description: A brief description of the pet.
    - url: The URL of an image representing the pet.

    Example usage:
    pets['dogs'][0]['name']  # Returns the name of the first dog in the list.
    pets['cats'][0]['age']   # Returns the age of the first cat in the list.
    """
"""_summary_
    """
pets = {  
    'dogs': [{
        'name':
        'Spot',
        'age':
        2,
        'breed':
        'Dalmatian',
        'description':
        'Spot is an energetic puppy who seeks fun and adventure!',
        'url':
        'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-spot.jpeg'
    }, {
        'name':
        'Shadow',
        'age':
        4,
        'breed':
        'Border Collie',
        'description':
        'Eager and curious, Shadow enjoys company and can always be found tagging along at your heels!',
        'url':
        'https://content.codecademy.com/programs/flask/introduction-to-flask/dog-shadow.jpeg'
    }],
    'cats': [{
        'name':
        'Snowflake',
        'age':
        1,
        'breed':
        'Tabby',
        'description':
        'Snowflake is a playful kitten who loves roaming the house and exploring.',
        'url':
        'https://content.codecademy.com/programs/flask/introduction-to-flask/cat-snowflake.jpeg'
    }],
    'rabbits': [{
        'name':
        'Easter',
        'age':
        4,
        'breed':
        'Mini Rex',
        'description':
        'Easter is a sweet, gentle rabbit who likes spending most of the day sleeping.',
        'url':
        'https://content.codecademy.com/programs/flask/introduction-to-flask/rabbit-easter.jpeg'        
    }]
}
