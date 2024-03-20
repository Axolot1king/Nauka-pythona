import random
from time import sleep
import winsound

random_code = ''.join(random.choices('0123456789', k=4))

ahh = input('do you want do see arm-bomb code (Y/N):')

if ahh == 'Y':
    print('arm-bomb code is:', random_code)

coded = input('enter arm-bomb password:')

if coded == random_code:
    for t in range(15, 0, -1):
        print('run! time left:', t, 'seconds')
        winsound.Beep(1000, 500)  # Beep with frequency 1000 Hz and duration 500 milliseconds
        sleep(1)
        if t == 1:
            print("\U0001F4A5\U0001F4A5\U0001F4A5 BOOM! \U0001F4A5\U0001F4A5\U0001F4A5")
            import winsound


            def play_explosion_sound():
                # Specify the path to the explosion sound file
                explosion_sound_file = "mixkit-explosion-and-glass-debris-1701.wav"

                # Play the explosion sound
                winsound.PlaySound(explosion_sound_file, winsound.SND_FILENAME)


            # Call the function to play the explosion sound
            play_explosion_sound()
else:
    print('wrong code=(')