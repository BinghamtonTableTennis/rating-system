# Table Tennis Club Website Template
This website template provides the following information to all users:
- A ladder that organizes users based on the USATT rating system
- Player information (wins, losses, match history)
- Club photos at past tournaments
- About us page
- The ITTF rules for table tennis
- Contact page
- Home page with club info, updates, and links to other social media
- Send an email to the organization email through the contact page

For admins only:
- Track attendances at each practice (including late members)
- Add new players to the database
- Add matches to the database
- View summary statistics (Average players per practice, total front page visits, and more)
- Display messages/updates/content on the front page
- Add new Google Slides to the photos page
- Customize images throughout the site
- Change E-Board members and club email displayed on the contact us page
- Add social media links in footer
- Update the organization information that is displayed throughout the site
- Change color scheme of navigation bar and footer
- Five login attempts. After five failed attempts, the user will be locked out for one hour.

## Sample Website
Check out the Binghamton University Table Tennis Club website at https://binghamtontabletennis.herokuapp.com/

## To access the admin panel
Go to /admin and enter admin credentials or click the Log In button in the navigation bar.

## How to use the admin panel
On the admin panel, you will see several tables available to modify with Add/Change options:
- Club Attendance
- Color Scheme
- EBoard
- Front Page Content
- Images
- Matches
- Organization Information
- Past Attendance
- Players
- Practices
- Slides
- Social Media
- Updates

### Club Attendance
To keep track of attendance for a practice, use the Club Attendance table. Simply ask members to enter their first and last name.

### Color Scheme
Change the colors for the header/footer and text throughout the site.

### EBoard
Here, you can update who the current EBoard members are. You can choose from several positions and assign them to specific people. This information will be displayed on the contact page.

### Front Page Content
This contains stable information that you want to display to users who visit your home page. This is different than news/updates (see Updates)

### Images
Select the page where you want to update the picture and provide the url containing the image to display.

### Matches
To record ranked matches, enter the winner and loser names and the score (best of 3 match). The same script for the Club Attendance will collect the match results and update the ladder page as well as individual match history pages.

### Organization Information
Fill in this section completely to have the correct information displayed throughout the site.

### Players
You can only modify or delete an existing player. A new Player entry will automatically be added after signing into Club Attendance.

##### Downloading Emails for G-Mail
- On the players admin panel, use the checkboxes to get the email addresses of the selected members. 
- In the action dropdown menu, select 'Download emails to a .txt file'. 
- Press 'Go'. 
- You will then automatically download a .txt file containing a list of emails formatted for pasting into Google Contacts. Only members you selected who provided an email address will be in this file.

##### Creating new contacts for G-Mail
- Open the .txt file from above and copy the entire content to your clipboard (Ctrl-A then Ctrl-C).
- Log into your G-Mail account
- Go to your Contacts page (Click Mail at the top left and select Contacts)
- If you want to create a new group, select 'New Group...' on the left navigation bar. Otherwise, select the existing group.
- Click the Add to Group button (Image of person and the + symbol)
- A blank textbox should appear
- Paste the contents of your clipboard into this textbox (Ctrl-V) and press enter
- All the emails you downloaded should now be in the new group. Duplicate entries will not be added.

### Practices
This table is automatically populated after the Club Attendance script finishes running. Only modify this table if there are errors or if you want to clear the practice history.

### Slides
This website only supports Google Slides at this time. To add a new slideshow to the photos page, first make sure the Google Slides is published (File -> Publish to the web -> Publish). Then, fill in the following fields:

- Date: Needed to organize slides to ascending order
- Title: Used to label a slideshow
- Slides ID: The ID of the slideshow (see below)

##### How to get the Slides ID
- In your browser, open up the Google Slides you want to share on the photos page
- Look for the slides ID in the URL.

For example, if the URL is:

      https://docs.google.com/presentation/d/1152Jzvxr-hDXlGE1zaT4_NuZf8sl-GAIvCUhhzMA800/edit#slide=id.g1b0ebe7be8_0_0
the Slides ID is:

      1152Jzvxr-hDXlGE1zaT4_NuZf8sl-GAIvCUhhzMA800
      
### Social Media
Displayed in the footer on each page. Provide the URL of your other social media's page and a URL containing an image of the social media's logo.

### Updates
To post an update on the front page, simply enter the date and the message you want to display.

## To run locally on Cloud9
First, create a new Python workspace. Then, enter the following commands in bash:

    $ git clone https://github.com/Binghamton-University-Table-Tennis/website-template
    $ cd website-template/
    $ sudo apt-get update
    $ sudo apt install libpq-dev python-dev
    $ sudo pip install -r requirements.txt
    $ sudo service postgresql start
    $ export DATABASE_URL=postgres:///"$(whoami)"
    $ export DEBUG=True
    $ export SECRET_KEY="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)"
    $ touch .env
    $ python manage.py migrate
    $ python manage.py collectstatic
    $ python worker.py
    $ heroku local

## To create a local admin
    $ python manage.py createsuperuser

## Deploying to Heroku from Cloud9
Make sure you have a local copy working as explained above. Next, create a Heroku account at https://www.heroku.com/. Then, run the following commands (enter credentials when prompted):

    $ heroku create
    $ heroku config:set DEBUG=False
    $ heroku config:set SECRET_KEY="$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)"
    $ git push heroku master
    $ heroku run python manage.py migrate
    % heroku run python worker.py

You can now navigate to your brand new URL hosted on Heroku.

### Additional steps required on Heroku
You must setup the following features on your Heroku app's dashboard
- Heroku Scheduler
- SendGrid
- Google reCAPTCHA API Keys

#### Heroku Scheduler
Create a daily job to update matches and practices, preferably right after practice (Note: Timezone for the scheduler is UTC). Use the following command for the job:

    $ python worker.py
    
#### SendGrid
- Go to Settings -> API Keys -> Create API Key (top right)
- Provide an API Key Name, allow Full Access, and click Create & View
- Copy the API Key provided on the screen (Note: This key will not be shown again)
- Go back to your application dashboard on Heroku and go to Settings -> Reveal Config Vars
- Add a new key-value pair:
       
      SENDGRID_API_KEY = your_sendgrid_api_key
     
#### Google reCAPTCHA API Keys
- Go to https://www.google.com/recaptcha/admin 
- Create a new reCAPTCHA V2, providing a label and your Heroku domain. You will be given a site key and a secret key
- Go to your application dashboard on Heroku and go to Settings -> Reveal Config Vars
- Add a two new key-value pairs:
        
      GOOGLE_RECAPTCHA_SITE_KEY = your_site_key
      GOOGLE_RECAPTCHA_SECRET_KEY = your_secret_key


## To create an admin on Heroku
    $ heroku run python manage.py createsuperuser
