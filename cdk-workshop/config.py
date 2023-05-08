from dotenv import load_dotenv
import os

load_dotenv()

AWS_ACCOUNT_ID = os.getenv('AWS_ACCOUNT_ID')
AWS_REGION = os.getenv('AWS_REGION')
