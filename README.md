SPAM MESSAGE DETECTOR - SETUP GUIDE (for a fresh college PC)
================================================================

FILES IN THIS FOLDER:
- train_spam_classifier.py  -> trains the ML model
- app.py                    -> backend server (Flask API)
- index.html                -> frontend web page
- spam.csv                  -> dataset (YOU must add this, see below)
- spam_model.pkl            -> trained model (created after Step 3)
- vectorizer.pkl            -> trained vectorizer (created after Step 3)

IMPORTANT: This college PC needs Python and internet access (to install
packages) at least once before you can run this. Do this setup a day
before your presentation if possible, in case the lab PC has restrictions.

--------------------------------------------------------------
STEP 1: Get the dataset (do this BEFORE college, at home, and copy
it onto the pendrive)
--------------------------------------------------------------
1. Go to Kaggle and search "SMS Spam Collection Dataset"
   (or search: kaggle sms spam collection dataset)
2. Download it and find the file usually named "spam.csv"
3. Copy that spam.csv file into this same project folder, alongside
   app.py and the other files, BEFORE copying the folder to the
   pendrive.

--------------------------------------------------------------
STEP 2: Copy this whole folder onto your pendrive
--------------------------------------------------------------
Copy the entire "spam-detector-project" folder (with spam.csv inside
it) onto your pendrive. Do this at home so everything is ready.

--------------------------------------------------------------
STEP 3: At college - install requirements (needs internet once)
--------------------------------------------------------------
Plug in the pendrive, open a terminal/command prompt INSIDE this
folder, and run:

    pip install pandas scikit-learn matplotlib seaborn flask flask-cors

(If the lab PC blocks pip installs, ask a lab assistant, or try to
do this step at home on a laptop you can borrow, then bring your
pendrive with everything pre-installed is not possible for pip
packages - packages install to the PC, not the pendrive. So this
step must happen on whichever PC you will actually run the demo on.)

--------------------------------------------------------------
STEP 4: Train the model (only needs to be done once per PC)
--------------------------------------------------------------
In the terminal, inside this folder, run:

    python train_spam_classifier.py

Wait for it to finish. You will see accuracy/precision/recall
numbers printed, and two new files will appear:
    spam_model.pkl
    vectorizer.pkl

TIP: If you already trained it once on your own laptop, you can just
copy spam_model.pkl and vectorizer.pkl onto the pendrive too, and
SKIP this step at college entirely - saves time and avoids any
issues with training on a strange PC.

--------------------------------------------------------------
STEP 5: Start the backend server
--------------------------------------------------------------
In the same terminal, run:

    python app.py

You should see a message like "Running on http://127.0.0.1:5000".
LEAVE THIS TERMINAL WINDOW OPEN - do not close it during your demo.

--------------------------------------------------------------
STEP 6: Open the frontend
--------------------------------------------------------------
Open index.html by double-clicking it (it will open in the default
browser).

--------------------------------------------------------------
STEP 7: Test it
--------------------------------------------------------------
Type a message like:
    WIN a free iPhone now!! Click here to claim your prize
Click "Check" and you should see "Spam" with a confidence percentage.

Try a normal message like:
    Hey, are we still meeting at 5pm today?
This should show "Not Spam".

================================================================
BEST PRACTICE: Pre-train at home, carry the .pkl files
================================================================
The safest plan is to run Steps 1, 3, and 4 at home on your own
laptop BEFORE college, so spam_model.pkl and vectorizer.pkl are
already sitting in this folder. Then copy the WHOLE folder
(including those .pkl files) to the pendrive. At college, you will
only need to do Steps 3 (pip install, if not already on that PC),
5, 6, and 7 - much faster and fewer things can go wrong live.

================================================================
TROUBLESHOOTING
================================================================
"Error connecting to server" in browser
    -> Make sure app.py is still running in the terminal.

ModuleNotFoundError
    -> Re-run the pip install command from Step 3.

spam_model.pkl not found
    -> You skipped Step 4, or forgot to copy the .pkl files.
    -> Run train_spam_classifier.py first.

pip install fails / no internet on college PC
    -> Ask if there's an offline package cache, or try a different
       PC, or do this step at home before leaving.
