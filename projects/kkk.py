x = int(input('enter password:'))

if x == 8766:
    import winsound


    def play_explosion_sound():
        # Specify the path to the explosion sound file
        explosion_sound_file = "aaa.wav"

        # Play the explosion sound
        winsound.PlaySound(explosion_sound_file, winsound.SND_FILENAME)


    # Call the function to play the explosion sound
    play_explosion_sound()
else:
    print('you try to hack in!?')