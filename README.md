


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


![Landing page photo](https://github.com/12moi/pichure-world/pictures/master/media/images/screenshot.png)

## User Stories
As a user of the application I should be able to:

1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
3. Search for different categories of photos. (ie. Travel, Food)
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

## Installation / Setup instruction
The application requires the following installations to operate
Django
python3.8
pip
Cloudinary
Bootstrap
Virtual Enviroment


## Cloning
Open Terminal {Ctrl+Alt+T}

git clone https://github.com/CynthiaOuma12673/mygallery.git

cd mygallery

code . or atom . based on the text editor you have.

## Running the Application
1. To run the application, open the cloned file in terminal and run the following commands:

  $ python3.8 manage.py runserver

2. To run test for the application $ python3.8 manage.py test gallery

## BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display picture-share Images | page loads | pichure-share images are displayed with their locaion and category|
| See picture-share | user clicks on the image from the page | user is directed to either save...|
| Display Images in category | user clicks on category link | Images  in that category are displayed |
| Images are displayed in each location  | user clicks on location link | Images in that location are displayed  |

#### Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug
Contact Information
If you have any question or contributions, please email me at [moimshadrack@student.moringaschoolgmail.com]

#### License
License
Copyright (c) 2022 Moi Shadrack