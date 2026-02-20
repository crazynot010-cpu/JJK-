import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        # Connects to Mongo using your .env URI
        self.uri = os.getenv("MONGO_URI")
        self.client = AsyncIOMotorClient(self.uri)
        self.db = self.client["jjk_rpg_db"]

    # Collection Shortcuts
    @property
    def players(self): return self.db["players"]
    
    @property
    def npcs(self): return self.db["npcs"]
    
    @property
    def items(self): return self.db["items"]
    
    @property
    def techniques(self): return self.db["techniques"]
    
    @property
    def market(self): return self.db["market"]

# One instance to rule them all
db = Database()
