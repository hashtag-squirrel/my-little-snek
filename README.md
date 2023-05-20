# my little Snek

## Features/Gameplay

- start game (new/load existing)
- display game
    - display Snek
        - Snek name
        - Snek age
        - Sadness
        - Hunger
        - Poop
    - display Input options
        - snek functions
        - quit with q
- run over time and accept input without pausing
- functions for the Snek
    - feed 
    - pet
    - clean
    - die on specified conditions
- autosave with every tick




To read:
https://medium.com/vaidikkapoor/understanding-non-blocking-i-o-with-python-part-1-ec31a2e2db9b
https://stackoverflow.com/questions/5404068/how-to-read-keyboard-input/53344690#53344690

Libraries to checkout:
- time
- queue
- threading
- 

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
