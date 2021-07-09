# PWGenerator (Incomplete)

Fun little project creating a password generator. Idea from https://www.dataquest.io/blog/python-projects-for-beginners/ with the link https://www.101computing.net/random-password-generator/ providing some insight on the topic and approach.


In my variation of the password generator, there is a preset option of generating a password curated of 8 characters, including at least 1 uppercase, 1 lowercase, 1 number, 1 special, and 1 punctuation character. There is also another option of generating a password with user inputted variations of these values, being able to choose whether special and/or punctuation characters are in the password; choosing a minimum set amount of characters for each category; making the password length between 8 and 16 characters long.


Current bug: dealing with unicode issues where the unreadable sections of the password are cut out of whats written in the text file)
