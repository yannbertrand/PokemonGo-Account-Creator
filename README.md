# [DEAD] PokemonGo-Account-Creator
Create a list of Pokémon Go accounts

# Notice
## DUE TO NIANTIC IMPLEMENTING RECAPTCHA IN THE SIGN-UP PROCESS, THIS SCRIPT IS NOT WORKING ANYMORE

**Unfortunately, we cannot find a way to bypass the captcha. We are very sorry, and we hope you enjoyed the script while it worked. Thank you for all the support.**

### Please check https://github.com/skvvv/pikapy which is way better than this by now 😄

**Stability: 1 - Experimental**

## What do I need to do?
1. Create a Gmail account
2. Create an `accounts.txt` file (template `username:password:email`, email should be aliases of the newly created account)
3. Launch `python ptc-creator.py accounts.txt`
4. Wait for it to finish
5. Launch `python tos-validator.py accounts.txt`
6. Validate your email adress using `email-validator.js` in [Google Apps Script](https://www.google.com/script/start/)
7. That's it

## What does it do? How does it work?
- Pokémon Go doesn't check for aliases in email adresses, it's then possible to create multiple accounts using one Gmail address.
- `ptc-creator.py` create your Pokémon Trainer Club accounts using the data inside the `accounts.txt` file.
- Each account need to validate the TOS and verify their email, all mails go to the same Gmail address.
- `tos-validator.py` loop on the same `accounts.txt` file to validate the TOS.
- The `email-validator.js` script click on each validation link and delete the mail.

## What are the other files?
I wanted to improve the scripts but The Pokémon Company added a Captcha to the
Pokémon Trainer Club signup page.
