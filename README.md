# NaijaNetherlands

* # Introduction
    NaijaNetherlands is a full-stack framework project built using Django, Bootstrap,Python,Html, Css and Javascript
    This is a blog website designed for Nigerian expats living in Netherlands. They should find useful information that allows them to adjust to the lifestyle in the Netherlands.
    ![responsive image for the site](readme_img/mockup-image.png)

* ## Live Preview   
    * ### For a live preview click: [NaijaNetherlands](https://herokuapp.com/)

* ## Table of Contents
* [SiteGoals](#SiteGoals)
* [UX](#ux)
    * [Entity Relationship Model](#entity-relationship-model)
    * [Agile Methodology](#agile-methodology)
    * [Color Scheme](#color-scheme)
    * [User Stories](#user-stories)
    * [Admin Stories](#admin-stories)
    * [Wireframes](#wireframes)

* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)

* [Testing](#testing)

* [Bugs](#bugs)
    
    * [Fixed Bugs](#fixed-bugs)
    * [Unfixed Bugs](#unfixed-bugs)

* [Technologies Used](#technologies-used)

    * [Languages Used](#languages-used)
    * [Libraries/Framework Used](#librariesframework-used)
    * [Other Technologies](#other-technologies)

* [Deployments](#deployments)

    * [Heroku](#heroku)
    * [Github](#github)

* [Credits](#credits)


* # Site Goals
 The goal of the site is to give Nigerian expats the relevant information needed to live susutainably in the Netherlands through blog posts.
 Users of the site shold easily read blog posts and comment on the different posts.


* # UX

    * ## Entity Relationship Model
        * Before I started this project, I created a relationship entity for a Django app, which helped me determine what models fields are needed for this project.

        ![website's database diagram](readme_img/entity_rel.png)

    * ## Agile Methodology
        * This project was created using the agile methodology and github issue boards.

            ![agile methodology for the website](readme_img/agile_issues.png)

            ![github issue boards](readme_img/kaban_board.png)

    
    * ## Color Scheme
        * Based on the  goal of the website I decided to use a touch of Nigerian and Netherlands color green, red and white.
        ![Color Palette](readme_img/colorpallette.png)

    * ## User Stories
        * As a site user:
        * I want to read different posts on the site.
        * I want to comment on the post.
        * I want to like the comment.
        * I want to edit the comment.
        * I want to delete the comment.
        * I want to sign up, sign in as a user.
        * I want to login & logout
        

    * ## Admin Stories 
        * As a site admin:
        * I want to create drafts.
        * I want to create new post on the website.
        * I want to read new post.
        * I want to update a post.
        * I want to approve comments
        * I want to delete comments.

    * ## Wireframes
    * Project wireframe was created by using ![wireframe](readme_img/balsamiq_wireframe.png)
        


* # Features 

    * ## **Home Page**
    * ### **Navigation Bar** 
        * The navigation bar is featured on all the pages on the website. It includes the website name, link to the home page, about page, register and login page.
        * This allows users to move through the different pages.
        ![Navbar](readme_img/nav_bar.png)
            
    * ### **Landing Page**  
        * The landing page includes a photograph with a text attached to the left. It is fully responsive.
        * It has a read more button overlay which will work in the future. 
            ![home page image](readme_img/landing_page.png)  
            ![Responsive Navbar](readme_img/responsive_nav.png)


    * ### **Blog Posts**  
        * There are 6 different blog posts for the user to read through. 
        * Each post has a title, author and image attached to it with a link to another page. 
            ![Blog Post](readme_img/blog_posts.png)
 
         
    * ### **About Page**
        * Users will not have access to appointment form, they will be asked to `login/register` first.    
            ![About Page](readme_img/about_page.png)  

        
   * ### **Registration Page**
         * New users will be asked to sign in.
         * When users have successfully registered with the website, they will be directed to the home page and see successfully signed in.  
            ![Signup](readme_img/signup.png)

       
    * ### **Signin Page**
        * Guests and logged in users have access to the contact us page, so users don't need to register or login to send us a message.  

         * Upon confirming signing in , the user will be logged in the website, and a pop-up model will display the message `You have successfully signed in`, which will disappear after 3 seconds.
            ![image for signin form](readme_img/signin.png)
 

    * ### **Logout Page**
        * `django-allauth` library was used to handle all the messages and errors for `login`, `register` and `logout` page.
        * Logged in users will not see a registration or login button. Instead, they will see a logout button in the navbar, and clicking that will prompt them to confirm that they wish to logout.  

         * Upon confirming sign out, the user will be logged out from the website, and a pop-up model will display the message `You have signed out`, which will disappear after 3 seconds.
            ![image for sign out page](readme_img/signout_popup.png)


    * ### **Footer**  
        * All the users will have access to the footer section of the page, where they can find information on all the social media handles. 
            ![footer](readme_img/footer.png)

      * ### **Django admin** 
      * This is the django admin terminal that allows the admin/author to login with the superuser created.
       ![django](readme_img/django_interface.png)

        * ### **Django administration** 
      * This is the django admin terminal that allows the admin/author to create posts/drafts, approve and delete comments.
       ![django](readme_img/django_adminsite.png)



    * ## **Future Features**
        * A better login and registration form will be added in the future, and users will only be allowed to register if they verify their email address.  

        * To make signing up easier for new users, I would like to add an option of a one-click signup button where users who already have an account with Google or Facebook, can sign up by simply clicking on Google or facebook.  

        * In the future, I would like to prevent users from selecting the same treatment option twice. So users will not be able to choose the same treatment again in the booking form.

        * When a user has already booked an appointment, if the date has passed the current date, their appointment will automatically display as expired.

* # Testing

* You can check what testing has been performed for the website by clicking [Testing.md](testings.md)

* # Bugs

* Multiple bugs were encountered during the development stage.

    * ### Fixed Bugs
        * First issue encounterd was the `requested date` field on the `Book Appointment` form, where users entered their details in but as soon as they click on the submit button, the form wouldn't submit. This issue was caused by the UK format date I added to the form widget, because by default it was US notation, so I had remove it to fix the issue.  
            ![error in formate](static/images/r 
        
      

    * ### Unfixed Bugs
        * The issue was scrolling down, sometimes the page scrolled down smoothly on my laptop and sometimes the scrolling down panel was visible, but scrolling down wasn't smooth at all. Upon reaching out to tutor and mentor, both of them said their computers/laptops didn't have that sort of problem, so it's probably only my laptop that has this problem.  


* # Technologies Used

    * ## Languages Used
        * [HTML](https://www.w3schools.com/html/)
        * [CSS](https://www.w3schools.com/css/)
        * [Javascript](https://en.wikipedia.org/wiki/JavaScript)
        * [Python](https://www.python.org/)

    * ## Libraries/Framework Used
        * [Django](https://www.djangoproject.com/)
        * [Bootstrap](https://getbootstrap.com/)
        * [jQuery](https://jquery.com/)

    * ### Libraries/Module Installed
        * asgiref==3.5.2
        * cloudinary==1.29.0
        * dj-database-url==1.0.0
        * dj3-cloudinary-storage==0.0.6
        * Django==3.2.15
        * django-allauth==0.51.0
        * django-bootstrap-datepicker-plus==4.0.0
        * django-bootstrap4==22.2
        * django-crispy-forms==1.14.0
        * django-phonenumber-field==7.0.0
        * gunicorn==20.1.0
        * oauthlib==3.2.1
        * phonenumbers==8.12.56
        * psycopg2==2.9.3
        * PyJWT==2.5.0
        * pylint-plugin-utils==0.7
        * python3-openid==3.2.0
        * pytz==2022.2.1
        * requests-oauthlib==1.3.1
        * sqlparse==0.4.2
        * types-cryptography==3.3.23

    * ## Other Technologies
        * [Postgres Database](https://www.postgresql.org/)
        * [W3School](https://www.w3schools.com/)
        * [Stackoverflow](https://stackoverflow.com/)
        * [Git](https://git-scm.com/)
        * [Github](https://github.com/)
        * [Gitpod workspace](https://gitpod.io/workspaces)
        * [Heroku](https://dashboard.heroku.com/apps)
        * [Flowchart](https://lucid.app/documents#/documents?folder_id=home)
        * [coolors](https://coolors.co/)
        * [Balsamiq Wireframes](https://balsamiq.com/wireframes/)
        * [jshint](https://jshint.com/)
        * [HTML code validator](https://validator.w3.org/)
        * [CSS code validator](https://jigsaw.w3.org/css-validator/)
        * [Font Awsome](https://fontawesome.com/)
        * [Google Fonts](https://fonts.google.com/)
        * [Slack](https://slack.com/intl/en-gb/)
        * [geeksforgeeks](https://www.geeksforgeeks.org/)
        * [SNYK](https://security.snyk.io/package/npm/moment)

* # Deployments
* Git and GitHub are used for version control. Python is the backend language, and can't be displayed with GitHub alone, To live preview my project, I used Heroku.

* ## Heroku
    * ### Deployment Steps On Heroku.
        * In my project i've used Django v3.2, so I used this command `pip3 install 'django<4' gunicorn` to install django.
        * So inside the terminal added these libraries:  
        `pip3 install dj_database_url psycopg2`,  
        `pip3 install dj3-cloudinary-storage`
        * Created requirements.txt file where I can save all the libraries i've installed:  
        `pip3 freeze --local > requirements.txt`
        * To create my project typed this command:  
        `django-admin startproject naijanetherlands
        * To create my app:  
        `python3 manage.py startapp blog`

        * to make this app work, Into the setting.py file inside `INSTALLED_APPS` added `blog`
        * to migrate changes typed this command:  
        `python3 manage.py migrate`
        * to run the test if the project is working `python3 manage.py runserver`

        * When deploying for the first time on Heroku, you must first register with Heroku.
        * Create your project name and location.
        * To add Database into the app, Locate in the Resources Tab, Add-ons, search and add 'Heroku Postgres'
        * Copy DATABASE_URL value, by going into the Settings Tab, click reveal Config Vars, Copy Text
        * In your workspace Create new env.py file.
        * Import os library:  
            `import os`
        * Set environment variables:  
            `os.environ["DATABASE_URL"] = "Heroku DATABASE_URL"`
        * Add in secret key:  
            `os.environ["SECRET_KEY"] = "mysecretkey"`
        * Add Secret Key to Config Vars in Heroku settings:  
            `SECRET_KEY, "mysecretkey"`

        * Add env.py file to the settings.py file:  
            `import os`  
            `import dj_database_url`

            `if os.path.isfile("env.py"):`  
                `import env`
        * Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku:  
            `SECRET_KEY = os.environ.get('SECRET_KEY')`

        * Comment out the old DATABASES variable in setting.py file and add this instead:  
            `DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`

        * Save all files and Make Migrations:  
            `python3 manage.py migrate`

        * Make account with Cloudinary To get static and media files.
        * From Cloudinary Dashboard, Copy your `CLOUDINARY_URL`:  
        * Add Cloudinary URL to env.py file:  
            `os.environ["CLOUDINARY_URL"] = "cloudinary://************************"`

        * Add Cloudinary URL to Heroku Config Vars:  
            `"cloudinary://************************"`

        * Temperoily add DISABLE_COLLECTSTATIC inside the heroku config Vars:  
            `DISABLE_COLLECTSTATIC, 1`

        * Add Cloudinary Libraries to settings.py installed apps:  
            `INSTALLED_APPS = ['cloudinary_storage', 'django.contrib.staticfiles', 'cloudinary']`

        * in the settings.py file under the `STATIC_URL = 'static/'` add:  
            `STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'`  
            `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`  
            `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`  

            `MEDIA_URL = '/media/'`  
            `DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`  

        * Place under the BASE_DIR line in settings.py:  
            `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`

        * Change the templates directory to TEMPLATES_DIR Place within the TEMPLATES array:  
            `TEMPLATES = [{'DIRS': [TEMPLATES_DIR],],},},]`

        * Add Heroku Hostname to ALLOWED_HOSTS:  
            `ALLOWED_HOSTS = [".herokuapp.com", "localhost"]`

        * Create 3 new folders on top level directory:  
            media, static, templates

        * Create Procfile on the top level directory and inside the file add this:  
            `web: gunicorn dentist.wsgi`
        
        * before deploying on heroku make sure: 
            `DEBUG = False`
            Remove `DISABLE_COLLECTSTATIC` from the config vars.


* ## Github
    * ### Commit On Github:
        * To make my project I used gitpod worskspace, where first save all the files.
        * Then in the terminal type `git add .` to add all the changes inside the staging area.
        * The next step was `git commit -m "changes I made"` where I confirmed that what changes I want to make.
        * Last but not least, I have typed `git push` to save everything on Github.


    * ### Cloning A Repository:
        * On GitHub.com, navigate to the main page of the repository.
        * Above the list of files, click download icon which says `Code`.

            ![download repo](static/images/readme-

        * To clone the repository using HTTPS, under "HTTPS", click.
        * To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click.
        * To clone a repository using GitHub CLI, click GitHub CLI, then click.

            ![download repo](static/images/re

        * Open Git Bash.
        * Change the current working directory to the location where you want the cloned directory.
        * Type git clone, and then paste the URL you copied earlier.

            `$ git clone https://github.com/h

        * Press Enter to create your local clone.

* # Credits
    * ## Content
        * `Treatment page` title and description was taken from [dentalhealth.org](https:///) website.  
        * How to add images, title, description were done using the Django admin panel with help from the Code Institute's [Django blog walkthrough](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) project.
        * Display a message to a user using bootstrap, this was taken from the Code Institute's [Django blog walkthrough](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) project.
        * I have taken a little design inspiration from this Django [youtube  tutorial](https://www.) in preparation for this project.
        * By making this project I had plenty of help from the [Slack](https://slack.com/intl/en-gb/) Community and tutor support.
        * In order to find a solution to a problem, I often search [Stackoverflow](https://stackoverflow.com/) and [geeksforgeeks](https://www.geeksforgeeks.org/).
        * In order to give me an idea of how a readme file should look, I looked at some other students project readme files [ladybike](https://github.com/van-essa/ladybike#table-of-contents). 


    * ## Media
        * Site logo was created using [canva](https://www.canva.com/) website.
        * Site Images were taken from [pexels](https://www.pexels.com/) website.



**Bugs**

* I had this error in the process of developing File "/workspace/.pip-modules/lib/python3.8/site-packages/dj_database_url.py", line 80, in parse

**Credits**
Freepik
https://www.expatica.com/nl/living/household/recycling-in-the-netherlands-133948/
https://allaboutexpats.nl/citizen-service-number/
https://www.europeanbestdestinations.com/destinations/netherlands/best-places-to-visit-in-the-netherlands/
https://www.beatrizpaula.com/one-year-living-in-the-netherlands-a-retrospective/