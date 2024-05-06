# Jellybean Journal

JellyBean Journal is a simple web application built with Django that allows users to keep track of jellybean flavors they have eaten.
Features

    CRUD Functionality: Users can perform CRUD operations (Create, Read, Update, Delete) on jellybean flavors.
    User-friendly Interface: The interface is designed to be intuitive and easy to use.

Installation

    Clone the repository:

    git clone https://github.com/yourusername/jellybean-journal.git
    cd jellybean-journal

Create a virtual environment (optional but recommended):

    python3 -m venv env
    source env/bin/activate # For Unix/Linux

Install dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

Run the development server:

    python manage.py runserver

Access the application:

    Open your web browser and go to http://localhost:8000/ to access the JellyBean Journal.

Usage

    Adding a Flavor: Click on "Add Flavor" to add a new jellybean flavor. Enter the flavor name, color, description, and rating, then click "Add Flavor".
    Viewing Flavors: The homepage displays all the added jellybean flavors. Each flavor entry shows its name, color, description, and rating.
    Editing a Flavor: Click on the "Edit" button next to a flavor to edit its details. Update the information and click "Save Changes".
    Deleting a Flavor: Click on the "Delete" button next to a flavor to delete it from the journal.
