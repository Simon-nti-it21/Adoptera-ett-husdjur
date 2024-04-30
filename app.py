"""
This file contains the implementation of a Flask application for the Adopt a Pet website.

The application allows users to browse and adopt pets of different types, such as cats, dogs, and rabbits.
It provides routes for the index page, which displays links to different pet types, and for individual pet pages,
which display detailed information about a specific pet.

The file also imports a helper module that provides a dictionary of pets categorized by type.

To run the application, the Flask app is created and routes are defined using the `@app.route` decorator.
The index route returns the HTML content for the index page, while the `/animals/<pet_type>` route
returns a list of pets of the specified type. The `/animals/<pet_type>/<int:pet_id>` route returns
detailed information about a specific pet.

The application is run using the `app.run()` method, with debug mode enabled and the host set to "0.0.0.0".
"""

from flask import Flask

import helper

app = Flask(__name__)


@app.route('/animals')
@app.route('/')
def index():
  """
  This function returns the HTML content for the index page of the Adopt a Pet application.

  Returns:
    str: The HTML content for the index page.
  """
  return '''<h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
  <li><a href="/animals/cats">Cats</a></li>
  <li><a href="/animals/dogs">Dogs</a></li>
  <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>'''


@app.route('/animals/<pet_type>')
def animals(pet_type):
  """
  Returns a list of animals of the specified pet type.

  Args:
      pet_type (str): The type of pet to retrieve.

  Returns:
      str: A string containing HTML markup representing a list of animals of the specified pet type.
  """  
  content_list = helper.pets[pet_type]
  content_items = ''.join([f"<li><a href='/animals/{pet_type}/{content_list.index(item)}'>{item['name']}</a></li>" for item in content_list])
  return f'''<h1>List of {pet_type}:</h1>
  <ul>
    {content_items}
  </ul>
  '''




@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  """
  Display information about a specific pet.

  Args:
    pet_type (str): The type of pet (e.g., 'dog', 'cat').
    pet_id (int): The ID of the pet in the list.

  Returns:
    str: HTML content displaying information about the pet.
  """
  content_list = helper.pets[pet_type]
  pet_url = content_list[pet_id]['url']
  return f'''<h1>List of {pet_type}:</h1>
  <p> Name: {content_list[pet_id]['name']}</p>
  <p> Age: {content_list[pet_id]['age']}</p>
  <p> Breed: {content_list[pet_id]['breed']}</p>
  <p> Description: {content_list[pet_id]['description']}</p>
  <img src="{pet_url}" alt="{content_list[pet_id]['name']}">
'''


app.run(debug=True, host="0.0.0.0")
