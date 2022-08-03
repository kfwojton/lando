# Lando

L - Lazy (least amount of work )  
A - Austere (simple)  
N - Naked (vanilla JS only!)  
D - Dandy (is fun! )  
O - Optimized (is fast! )  



## What is LANDO

Lando isn't a javascript library rather it is a framework to keep apps simple, straight forward, and easy to develop on. Land uses vanilla JS to deliver blazing fast apps, without the need for web pack, other libraries or any sort of complexity. LANDO apps live directly in the back end app , and are compiled in the browser only when the user needs it .

### 1. LANDO in action

LANDO can integrate with any backend frameworks. This example is in django. Say, we want to dynamically change the prices on a products page. With LANDO you can just write:

```
{% for object in object_list %}


function increasePrice_{{object.pk}}() {

  document.getElementById("product_{{object.pk}}").innerHTML = parseInt(document.getElementById("product_{{object.pk}}").innerHTML) + 2;

}
{% endfor %}
```

Which when the browser loads turns into:

```

    function increasePrice_1() {

      document.getElementById("product_1").innerHTML = parseInt(document.getElementById("product_1").innerHTML) + 2;

    }



    function increasePrice_2() {

      document.getElementById("product_2").innerHTML = parseInt(document.getElementById("product_2").innerHTML) + 2;

    }
.....
```

Which in two lines of code handles all of hte changing of any product pricing on the whole app. This is much simpler than react.js, svelte.js, or angular which requires massive bundling of dependancies and usage of n-th degrees of unknown libraries. LANDO is just javascript and as a result doesn't need any of that.     

### 2. Create a virtual environment in your preferred way
```bash
# using virtualenv
virtualenv myenv -p python3

# using python
python3 -m venv myenv
```

### 3. Activate the virtual environment
```bash
# using virtualenv
virtualenv myenv/bin/activate

# linux/Mac
source myenv/bin/activate
```

### 4. Install PIP requirements in virtualenv
```bash
make install
# or explicitly run
pip install -r requirements.txt
```

### 5. Create a local .env file for local environmental variables
Create a .env file for local environment variables. The only required variable to run
the app locally is `SERVER_ENV`. Quickly create the minimal file using,
```bash
echo 'SERVER_ENV=LOCAL' > .env
```
### 6. Run migrations
Locally a SQLite3 database found in the file `db.sqlite3` is used to run the app against.
```bash
make migrate
# or explicitly run
python manage.py migrate
```

### 7. Create a superuser
```bash
make super
# or explicitly run
python manage.py createsuperuser
```

### 8. Run the server
```bash
make serve
# or explicitly run
python manage.py runserver
```

That's it! The app will be available on your local machine at `http://127.0.0.1:8000` or `http://localhost:8000`


## Using `django-mailbox`

### 1. Google Cloud Platform Account then OAuth2 Client

Follow step 4 from this guide: https://www.section.io/engineering-education/django-google-oauth/

**OAuth consent screen setup**
- User type: External
- Add the scope `https://mail.google.com/`.
- Test users: Allie AI email address (the one we're authenticating to read emails from)

**Credentials / OAuth client ID:**
- The application type needs to be `Desktop app` to grab emails via cmdline `getmail` cmd.

Set the client ID and secret in the environmental variables (.env file locally)
`GOOGLE_OAUTH2_CLIENT_ID`
`GOOGLE_OAUTH2_CLIENT_SECRET`

Docs:
- https://developers.google.com/identity/protocols/oauth2/scopes?authuser=2#gmail
- https://developers.google.com/gmail/api/auth/scopes

### 2. Connect gmail account via Oauth2

Visit http://localhost:8000/social/login/google-oauth2/ and sign in with Allie AI gmail. The Oauth2 credentials will now be in the DB.

### 3. Add Allie AI Mailbox

In admin site, under django-mailbox (http://localhost:8000/admin/django_mailbox/mailbox/), add a new mail for Allie AI account in the format described
here: https://www.section.io/engineering-education/django-google-oauth/

### 4. Import mail

You can now send real emails to this inbox, then import them into our system from the admin site
or by running `make getmail` or `python manage.py getmail`.

### Debugging
If you have issues authentication issues when retrieving mail with `make getmail`, you can use this
utility tool to test oauth2 authentication. https://github.com/google/gmail-oauth2-tools/wiki/OAuth2DotPyRunThrough


### [Deprecated] Importing Ethereal emails
1. Create account with https://ethereal.email/create
2. Download `credentials.csv` file
3. Import into system with `python manage.py import_ethereal credentials.csv`


### Contributing
```bash
git checkout -b 'MY_BRANCH'
git status
git add .
git commit -m 'MY_COMMIT_NAME'
git push MY_BRANCH origin
```

A link will be displayed in the console. Use that link to open a pull request on github.
