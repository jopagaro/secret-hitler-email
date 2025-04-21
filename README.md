# Secret Hitler Email Game

A simple implementation of Secret Hitler that sends role assignments to players via email.

## Gmail Setup Instructions

1. **Enable 2-Step Verification**:
   - Go to your [Google Account Security settings](https://myaccount.google.com/security)
   - Click on "2-Step Verification" and follow the steps to enable it

2. **Generate App Password**:
   - Go back to [Security settings](https://myaccount.google.com/security)
   - Click on "App passwords" (you'll need 2-Step Verification enabled to see this)
   - Select "Other (Custom name)" from the dropdown
   - Name it "Secret Hitler Game"
   - Click "Generate"
   - Copy the 16-character password that appears

3. **Create Environment File**:
   - Create a file named `.env` in the same directory as the game
   - Add these lines to the file:
     ```
     EMAIL_ADDRESS=your.gmail@gmail.com
     EMAIL_APP_PASSWORD=your_16_character_app_password
     ```
   - Replace `your.gmail@gmail.com` with your Gmail address
   - Replace `your_16_character_app_password` with the App Password you generated
   - Save the file

## Installation

1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd secret-hitler-game
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

1. Make sure you've completed the Gmail setup above
2. Run the game:
   ```bash
   python3 secret_hitler.py
   ```
3. Follow the prompts to:
   - Enter number of players (5-10)
   - Enter each player's email address
   - Confirm the addresses
   - Send out the role assignments

## Testing Tips

- You can test the game by yourself using Gmail's plus addressing:
  - If your email is `example@gmail.com`, you can use:
    - `example+player1@gmail.com`
    - `example+player2@gmail.com`
    - etc.
  - All emails will go to your main inbox but will appear as different players

## Security Notes

- Never share your App Password
- Don't commit the `.env` file to version control
- The `.gitignore` file is set up to prevent accidentally sharing sensitive information

## Role Distribution

- 5 players: 3 Liberals, 1 Fascist, 1 Hitler
- 6 players: 4 Liberals, 1 Fascist, 1 Hitler
- 7 players: 4 Liberals, 2 Fascists, 1 Hitler
- 8 players: 5 Liberals, 2 Fascists, 1 Hitler
- 9 players: 5 Liberals, 3 Fascists, 1 Hitler
- 10 players: 6 Liberals, 3 Fascists, 1 Hitler

## Notes

- In 5-6 player games, Hitler knows who the Fascist is
- Fascists know who Hitler is and who other Fascists are
- Liberals only know their own role
- For security, make sure to use an App Password and not your main account password
- The script uses Gmail's SMTP server by default. To use a different email provider, modify the SMTP settings in the code 