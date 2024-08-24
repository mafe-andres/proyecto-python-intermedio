import os
import json
import random
from data import Data

def shuffle(data):
    media = data.songs + data.podcast_episodes
    random.shuffle(media)
    for m in media:
        m.play()

def playlists():
    pass

def search():
    pass

def menu():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    data_dir = os.path.join(project_root, 'data')

    # Login de usuario
    users_path = os.path.join(data_dir, 'users.json')
    with open(users_path) as file:
        user_data = json.load(file)
        users = user_data["users"]
    while True:
        valid_user = False
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                valid_user = True
                break
        if valid_user:
            break
        else:
            print('Invalid username or password.')
    
    # Cargar datos en un objeto
    podcasts_path = os.path.join(data_dir, 'podcast_data.json')
    music_path = os.path.join(data_dir, 'music_data.json')
    data = Data()
    data.load_podcasts(podcasts_path)
    data.load_music(music_path)
    
    # Menu principal
    while True:
        print("\nMenu:")
        print("1. Shuffle")
        print("2. Playlists")
        print("3. Search")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            shuffle(data)
        elif choice == '2':
            playlists()
        elif choice == '3':
            search()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()