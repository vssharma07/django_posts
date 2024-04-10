Step 1: After cloning and going into the directory, execute the following command to install the python3 dependencies for this project.
pip3 install -r requirements.txt


Step 2: Perform the database migrations
python3 manage.py makemigrations
python3 manage.py migrate


Step 3: Create a superuser to access the django admin and creating some posts and comments
python3 manage.py createsuperuser


Step 4: Run the server
python manage.py runserver


Interacting with the APIs:


Post Model with columns like id, title, content, author, published_date, created_at, updated_at
Comment Model with columns like id, post, author, text, created_at, updated_at
Posts API: Access and manage blog posts.

List/Create Posts: GET /api/posts/, POST /api/posts/
Retrieve/Update/Delete Post: GET /api/posts/<post_id>/, PUT /api/posts/<post_id>/, DELETE /api/posts/<post_id>/
Comments API: Access and manage comments on blog posts.
List/Create Comments: GET /api/posts/<post_id>/comments/, POST /api/posts/<post_id>/comments/



Authentication:

To access write operations (creating, updating, deleting), authentication is required.
Obtain an authentication token by making a POST request to /api/token/ with your username and password.
Include the obtained token in the Authorization header of subsequent requests.

Example:

curl -X POST http://localhost:8000/api/token/ -d "username=<your_username>&password=<your_password>"

curl -X POST http://localhost:8000/api/posts/ -H "Authorization: Token <your_token>" -d "title=FirstPost&content=FirstPostContent&author=1&published_date=2024-04-10"




NOTE: This documentation provides you with a clear understanding of how to set up, run, interact with the Django Blog Application. Make sure to replace placeholders such as <your_username>, <your_password>, and <your_token> with actual values specific to your project. As, I am still learning django and am fluent with Ruby On Rails, please take this into consideration while looking at the project. I am a quick learner and can be of good use to your company.
