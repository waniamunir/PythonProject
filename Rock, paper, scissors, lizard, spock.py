
# Display the title
import random
print('================================')
print('ROCK PAPER SCISSORS LIZARD SPOCK')
print('================================')

# List of the choices (each choice has an index)
choices = ("✊","✋","✌️","🦎","🖖")
# Display the choices
print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')
# Users input
users_choice = int(input('Pick a number: 1, 2, 3, 4 or 5:')) -1
# CPU's input
CPU_choice = random.randint(0,4)
# Print users and CPU's choices
print(f"You chose: {choices[users_choice]}")
print(f"CPU chose: {choices[CPU_choice]}")

# Final output of the winner
if users_choice == CPU_choice:
     print('Tie!')
elif users_choice == 0 and CPU_choice == 2:
     print('You win, CPU loses!')
elif users_choice == 1 and CPU_choice == 0:
     print('You win, CPU loses!')
elif users_choice == 2 and CPU_choice == 1:
     print ('You win, CPU loses!')
elif users_choice == 3 and CPU_choice == 4:
     print ('You win, CPU loses!')
elif users_choice == 4 and CPU_choice == 2:
     print ('You win, CPU loses!')
elif users_choice == 2 and CPU_choice == 3:
     print ('You win, CPU loses!')
elif users_choice == 3 and CPU_choice == 1:
     print ('You win, CPU loses!')
elif users_choice == 1 and CPU_choice == 5:
     print ('You win, CPU loses!')
elif users_choice == 4 and CPU_choice == 0:
     print ('You win, CPU loses!')
else:
     print('CPU wins, You lose!')














