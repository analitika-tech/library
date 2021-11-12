# User guide for the LMS

To start using the app you must go to the app website where it is deployed:
```url
https://mss-kljuc.herokuapp.com/
```

The first thing that opens is the home page where you can search for a book.
![alt home page](/documentation/images/home.jpg)

# Application setup
## Admin panel
To become the admin of the site you create the superuser in the terminal of the app container.
#### This tutorial is for Heroku
```bash
heroku login # login into your account
heroku run python manage.py createsuperuser
```
After you create the admin account go to:
```url
https://your-url/admin
```
and login with the account that you created above. You will be greated with the admin pannel like this:
![alt admin pannel](/documentation/images/admin.jpg)

### Creating user groups
The user groups define the premissions that a given user can use the specific site on the web app.

Each group need's to be named like in this tutorial otherwise the permissions will not work.

Click on the Groups and click ADD GROUP + , in the upper right corner of the screen, the screen below will appear:
![alt group adding page](/documentation/images/group-adding.jpg)

Add groups like this: (When you find the permission duble click on it and it will appear in the Chosen permissions box (right-box))
1. Group name: book-editing
    * Permissions:
        * backend | book | Can add book
        * backend | book | Can change book
        * backend | book | Can delete book
        * backend | book | Can view book
- This group allows users to add, change, delete and view books
2. Group name: class-editing
    * Permissions:
        * backend | class | Can add class
        * backend | class | Can change class
        * backend | class | Can delete class
        * backend | class | Can view class
- This group allows users to add, change, delete and view classes
3. Group name: issue-editing
    * Permissions:
        * backend | issue | Can add issue
        * backend | issue | Can change issue
        * backend | issue | Can delete issue
        * backend | issue | Can view issue
- This group allows users to add, change, delete and view issues
4. Group name: reservation-editing
    * Permissions:
        * backend | reservation | Can add reservation
        * backend | reservation | Can change reservation
        * backend | reservation | Can delete reservation
        * backend | reservation | Can view reservation
- This group allows users to add, change, delete and view reservation
5. Group name: student-editing
    * Permissions:
        * backend | student | Can add student
        * backend | student | Can change student
        * backend | student | Can delete student
        * backend | student | Can view student
- This group allows users to add, change, delete and view students

Once you done adding these groups you should have 5 user permission groups like this: 
![alt group adding page](/documentation/images/permission-list.jpg)

## Adding users
To add users go to the link on the left navigation panel and click Users, then click ADD USER + in the upper right corner of the screen.
![alt group adding page](/documentation/images/add-user.jpg)
Fill the fields, after you save the user this screen will appear:
![alt group adding page](/documentation/images/user-creation.jpg)

Fill the remaining information it is crucial to fill the first name and last name fields because later when the users log in and create book reservations the reservations will take their full name as a reference to display them the reservations. (This will change in the future)
Then add permission group to a given user so he/she can do their job.

Then you can go to the login page and login to do your job:
![alt group adding page](/documentation/images/login.jpg)


The Reservation view allows professors to reservate a book for a given time, and the issues view, issues book's to the students and tracks the return date. If the students returns a book to late the system will automatically calculate the debt which is 0.50 KM per day.

If you have data in a data structure you can convert it to json which you can pass to our API for which the documentation is comming soon and the link will be in the description. The language support is also comming in the comming week's as we release the software for beta testing.