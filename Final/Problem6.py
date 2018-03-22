# Problem 6-1
# 10.0/10.0 points (graded)
# This question has 3 parts

# Consider the following hierarchy of classes:

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return 'It is obvious that ' + self.say(stuff)
        
# As written, this code leads to an infinite loop when using the Arrogant Professor class.

# Change the definition of ArrogantProfessor so that the following behavior is achieved:

# e = Person('eric')
# le = Lecturer('eric')
# pe = Professor('eric')
# ae = ArrogantProfessor('eric')

# >>> e.say('the sky is blue')
# eric says: the sky is blue

# >>> le.say('the sky is blue')
# eric says: the sky is blue

# >>> le.lecture('the sky is blue')
# I believe that eric says: the sky is blue

# >>> pe.say('the sky is blue')
# eric says: I believe that eric says: the sky is blue

# >>> pe.lecture('the sky is blue')
# I believe that eric says: the sky is blue

# >>> ae.say('the sky is blue')
# eric says: It is obvious that eric says: the sky is blue

# >>> ae.lecture('the sky is blue')
# It is obvious that eric says: the sky is blue

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own
# test cases.

# -------------------------------CODE-------------------------------#

class ArrogantProfessor(Person):
    def say(self, stuff):
        return self.name + ' says: ' + 'It is obvious that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff

# -------------------------------Result-------------------------------#
# Correct



# Problem 6-2
# 10.0/10.0 points (graded)
# You change your mind, and now want the behavior as described in Part 1, except that you want:

# >>> ae.say('the sky is blue')
# eric says: It is obvious that I believe that eric says: the sky is blue

# >>> ae.lecture('the sky is blue')
# It is obvious that I believe that eric says: the sky is blue

# Change the definition of ArrogantProfessor so that the behavior described above is achieved.

# Paste ONLY your ArrogantProfessor class in the box below. Do not leave any debugging print statements.

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test
# cases.


# -------------------------------CODE-------------------------------#

class ArrogantProfessor(Person):
    def say(self, stuff):
        return self.name + ' says: ' + 'It is obvious that I believe that ' + self.name + ' says: ' + stuff
    def lecture(self, stuff):
        return 'It is obvious that I believe that ' + self.name + ' says: ' + stuff
        
# -------------------------------Result-------------------------------#
# Correct



# Problem 6-3
# 15.0/15.0 points (graded)
# You change your mind once more. You want to keep the behavior from Part 2, but now you would like:

# >>> pe.say('the sky is blue')
# Prof. eric says: I believe that eric says: the sky is blue

# >>> ae.say('the sky is blue')
# Prof. eric says: It is obvious that I believe that eric says: the sky is blue

# Change the Professor class definition in order to achieve this. You may have to modify your implmentation for a previous part to get
# this to work.

# Paste ONLY the Professor class in the box below. Do not leave any debugging print statements.

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test
# cases.


# -------------------------------CODE-------------------------------#

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

# -------------------------------Result-------------------------------#
# Correct