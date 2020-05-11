# .lower()- returns a string with lowercase characters

favorite_song = "SmooTH Operator"
favorite_song_lowercase = favorite_song.lower()
#print(favorite_song_lowercase)

# .upper()- returns a string with uppercase characters

favorite_song_uppercase = favorite_song.upper()
#print(favorite_song_uppercase)

# .title()- returns a string where the first letter in each word is capitalized 

favorite_song_title = favorite_song.title()
#print(favorite_song_title)

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

#print(poem_title)
#print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
#print(poem_author)
#print(poem_author_fixed)

# split()- turns a string into a list and each word becomes an element in a list
line_one = "The sky has given over"
line_one_words = line_one.split()

#print(line_one_words)

favorite_food = "My favorite food will always be enchiladas."

split_food = favorite_food.split()

#print(split_food)

favorite_quote = "The          flower that blooms in adversity is the most rare and beautiful of all"

break_down = favorite_quote.split()

#print(break_down)

# split() will turn every word in the string into its own element in a list

greatest_guitarist = "santana"
# save the method to a new variable because strings are immutable
# every encounter of that specified character/substring start a new index
new_stuff = greatest_guitarist.split('a')

# output / ['s', 'nt', 'n', '']

#print(new_stuff)

twitch_name = "cyberbarbie"
split_name = twitch_name.split('b')

#print(split_name)

favorite_food = "sushi"
new_food = favorite_food.split('s')

#print(new_food)

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')

#print(author_names)

author_last_names = []

for name in author_names:
    author_last_names.append(name.split()[-1])

# print(author_last_names)

# Escape sequences- another way to escape/split a string
# \n newline- create a line break

# use the split method to turn the string into a list
# we used the delimter \n to separate each line into its own element

smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

# print(chorus_lines)

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')

#print(spring_storm_lines)

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

#print(reapers_line_one)

# example of .join()
# add a white space between each element in a list

quote = ["I", "like", "to", "sleep", "all", "the", "time"]

combined_quote = " ".join(quote)

#print(combined_quote)

# comma separated variables - join strings with a comma

favorite_places = ["San Diego", "Toronto", "San Francisco", "Amsterdam"]

# create a common and a whitespace between each string in a list
favorite_places_csv = ', '.join(favorite_places)

#print(favorite_places_csv) 

# .join()- to combine list of strings and create a new line break between each

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

new_paragraph = '\n'.join(winter_trees_lines)

print(new_paragraph)
