


# Picture-World
## Author
Moi-Shadrack

### Description
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.



### User Story
1. View different photos that interest them<br>
2. Click a single image to expand it and view the details of that photo
3. Search for different categories
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

### Setup and Installation
To get the project .......<br>

##### Cloning the repository:
https://github.com/12moi/picture-world.git 

##### Navigate into the folder and install requirements
cd picture-world pip install -r requirements.txt 

##### Install and activate Virtual
- python3 -m venv virtual - source virtual/bin/activate 

##### Install Dependencies
pip install -r requirements.txt 

##### Setup Database
SetUp your database User,Password, Host then make migrate<br>

python manage.py makemigrations pictures 

##### Now Migrate

python manage.py migrate 

##### Run the application
python manage.py runserver 

##### Running the application
python manage.py server 

##### Testing the application
python manage.py test <br>

Open the application on your browser 127.0.0.1:8000.

### Technology used
Python3.8<br>
Django 3.2.10<br>
Heroku<br>


#### Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug
Contact Information
If you have any question or contributions, please email me at [moimshadrack@student.moringaschoolgmail.com]

#### License
MIT License:
Copyright (c) 2022 picture-world
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.