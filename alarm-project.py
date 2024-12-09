#alarm clock project

import time
import datetime
import pygame

#this function allows the user to stop the alarm by typing "yes
def stop_alarm():
 while  pygame.mixer.music.get_busy():
     user_input = input("Enter 'yes' to stop the alarm: ")

     if user_input =="yes":
         pygame.mixer.music.stop()
         break

#this function allows the user to set the alarm
def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    sound_file = "my.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("the current time is: " + current_time)
        if current_time == alarm_time:
            print("WAKE UP!!!!!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            stop_alarm()


            is_running = False
        time.sleep(1)

#this is the main part of the program
if __name__ == "__main__":
    while True:
      alarm_time = input("Enter the alarm time (HH:MM:SS): ")
      try:
          time.strptime(alarm_time, "%H:%M:%S")
          break
      except ValueError:
          print("Invalid time format please try again")
    set_alarm(alarm_time)