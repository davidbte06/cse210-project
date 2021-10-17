import arcade

from nephiHunting.my_second_game import MyGame

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()