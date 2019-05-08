# Images

## A sample environment for engineers to practice integrating Mixpanel identity management, events, and people properties

- Images app with basic login, signup, and logout flow
- Allows a user to continuously get more images

## Setup

### Download the sample app
- Visit https://gitlab.com/mpsupport/server-side-training to download the source code directly or using ssh if you have a gitlab account

### Set up the Python environment for the app to use
- Install [homebrew](https://brew.sh/) if you haven't already. Homebrew is the standard way to install many command line programs on Macs.
- Install [pipenv](https://pipenv.readthedocs.io/en/latest/) with `brew install pipenv`
- Add the directory where pipenv was installed to your $PATH so your terminal can find the new "pipenv" program you just installed. Probably "/usr/local/bin/". Depending on your setup try this command: `echo "export PATH=$PATH:/usr/local/bin" >> $HOME/.bashrc`
- Run `pipenv install` in the directory where the "Pipfile" file is located
  - If pipenv complains about a missing Python version, install it with homebrew (do a quick google search)
- Run `pipenv shell` to activate the Python environment

### Run the local server!
- In the directory with the "manage.py" file:
  - Run `python manage.py migrate` (this sets up the database tables)
  - Then, run `python manage.py runserver`
- Go to your web browser and type in localhost:8000. You should see the local web app!
- You can stop the server with ctrl-c


## Mixpanel Practice (Practical)
- Initialize / insert Mixpanel into the sample app (make sure you have downloaded this app and that it runs)
- Track events with event properties client-side (follow the chart below, and add any other event and event properties as you deem necessary. Do not use Autotrack)
- Track events with event properties server-side (follow the chart below, and add any other event and event properties as you deem necessary)
- Track people profiles with people properties (follow the chart below, and add any other people property you deem necessary)
- Reset the distinct_id upon logout
- Integrate identity management with server-side alias and identify client-side, and alias the username to the client-side distinct_id
- Pass the distinct_id from the client to the server and vice versa

## Tes