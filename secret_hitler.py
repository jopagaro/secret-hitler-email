import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SecretHitlerGame:
    def __init__(self):
        # Initialize email settings
        self.email_address = os.getenv('EMAIL_ADDRESS')
        self.email_password = os.getenv('EMAIL_APP_PASSWORD')
        self.smtp_server = "smtp.gmail.com"  # Default to Gmail, can be changed in .env
        self.smtp_port = 587  # Default TLS port
        
        # Game roles
        self.ROLES = {
            5: {'fascist': 1, 'hitler': 1, 'liberal': 3},
            6: {'fascist': 1, 'hitler': 1, 'liberal': 4},
            7: {'fascist': 2, 'hitler': 1, 'liberal': 4},
            8: {'fascist': 2, 'hitler': 1, 'liberal': 5},
            9: {'fascist': 3, 'hitler': 1, 'liberal': 5},
            10: {'fascist': 3, 'hitler': 1, 'liberal': 6}
        }
        
        self.players = {}  # Will store player emails and their roles
        
    def setup_game(self, player_emails):
        """
        Set up the game with the given player emails
        """
        num_players = len(player_emails)
        if num_players < 5 or num_players > 10:
            raise ValueError("Number of players must be between 5 and 10")
            
        # Get roles for the current number of players
        roles = []
        role_counts = self.ROLES[num_players]
        roles.extend(['fascist'] * role_counts['fascist'])
        roles.extend(['hitler'])
        roles.extend(['liberal'] * role_counts['liberal'])
        
        # Shuffle roles and assign to players
        random.shuffle(roles)
        self.players = dict(zip(player_emails, roles))
        
        # Send role emails to all players
        self.send_role_messages()
        
    def send_role_messages(self):
        """
        Send emails to all players with their roles
        """
        fascists = [email for email, role in self.players.items() if role == 'fascist']
        hitler = next(email for email, role in self.players.items() if role == 'hitler')
        
        # Connect to SMTP server
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.email_address, self.email_password)
            
            for email, role in self.players.items():
                message = self.create_email_message(email, role, fascists, hitler)
                server.send_message(message)
    
    def create_email_message(self, player_email, role, fascists, hitler):
        """
        Create appropriate email message for each player
        """
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = player_email
        msg['Subject'] = "Secret Hitler - Your Role"
        
        body = self.create_role_message(player_email, role, fascists, hitler)
        msg.attach(MIMEText(body, 'plain'))
        
        return msg
    
    def create_role_message(self, player_email, role, fascists, hitler):
        """
        Create appropriate role message content for each player
        """
        if role == 'liberal':
            return "You are a LIBERAL. Work with other liberals to stop the fascists!"
        elif role == 'hitler':
            if len(self.players) <= 6:  # In 5-6 player games, Hitler knows who the fascist is
                fascist = [f for f in fascists if f != player_email][0]
                return f"You are HITLER!\nYour fascist teammate is: {fascist}"
            return "You are HITLER! Try to keep your identity hidden from the liberals!"
        else:  # Fascist
            other_fascists = [f for f in fascists if f != player_email]
            hitler_info = f"Hitler is: {hitler}"
            other_fascists_info = "Other fascist(s): " + ", ".join(other_fascists) if other_fascists else "You are the only fascist besides Hitler"
            return f"You are a FASCIST!\n{hitler_info}\n{other_fascists_info}"

# Example usage
if __name__ == "__main__":
    game = SecretHitlerGame()
    
    print("\n=== Secret Hitler Game Setup ===")
    while True:
        try:
            num_players = int(input("\nHow many players? (5-10): "))
            if 5 <= num_players <= 10:
                break
            print("Please enter a number between 5 and 10.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"\nPlease enter {num_players} email addresses:")
    player_emails = []
    for i in range(num_players):
        while True:
            email = input(f"Player {i+1}'s email: ").strip()
            if '@' in email and '.' in email:  # Basic email validation
                player_emails.append(email)
                break
            print("Please enter a valid email address.")
    
    print("\nConfirm these email addresses are correct:")
    for i, email in enumerate(player_emails, 1):
        print(f"Player {i}: {email}")
    
    confirm = input("\nSend role assignments to these players? (yes/no): ").lower()
    if confirm.startswith('y'):
        try:
            game.setup_game(player_emails)
            print("\nRole assignments have been sent successfully!")
            print("Tell all players to check their email.")
        except Exception as e:
            print(f"\nError sending emails: {str(e)}")
    else:
        print("\nGame cancelled. Run the script again to start over.") 