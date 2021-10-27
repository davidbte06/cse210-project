"""
Entrypoint of the application. Calls Director and arcade run
"""

import arcade
from game.director import Director
import os

def main():
    """Main function"""
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    window = Director()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()