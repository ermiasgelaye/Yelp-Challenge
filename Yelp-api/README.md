Yelp Search Tool
================

A tool for searching business listings on Yelp and exporting it to a CSV file.

Pre-Requisites
--------------

### Getting a Yelp API Key

1. Go to <https://www.yelp.com/fusion>
1. At the bottom, click on **Get Started**.
1. Sign up or log in.
1. Type in the required fields (you can enter anything it doesn't really matter), then click **Create New App**.
1. Click on the **Join the Developer Beta** button (this is required for using the new GraphQL API).
1. The value in the field **API Key** is what you will need later.


### Getting a text editor (e.g. Sublime Text)
1. Go to <https://www.sublimetext.com/>.
1. Click on **Download** and install the application.


First Time Installation (Mac OS)
---------------------------------

1. Open up your **Terminal**.
1. Install `pip` and `virtualenv` by entering the following commands (if you don't already have it):
    
        curl -X GET https://bootstrap.pypa.io/get-pip.py -O
        python get-pip.py
        
        pip install virtualenv

1. Navigate to the folder containing the code.
        
        # For example, if you have it on your Desktop:
        cd ~/Desktop/yelp-search

1. Create a virtualenv by entering the following commands:

        virtualenv env
        . env/bin/activate
        pip install -r requirements.txt


Usage Instructions (Mac OS)
----------------------------

1. Open `config.py` in Finder (right click `config.py` > Open With > Sublime Text).
1. Modify the values in there as needed (specifically the **Yelp API Key**).
1. Open up your **Terminal**.
1. Navigate to the folder containing the code.
        
        # For example, if you have it on your Desktop:
        cd ~/Desktop/yelp-search

1. Activate the virtulenv.

        . env/bin/activate

1. Run the script.
    
        python search.py

1. Open Finder and navigate to the code and you should see the results in a csv folder.

1. If you get a Yelp API Error such as "internal error" or "time out", these are usually temporary. Just try again after 30 seconds.
