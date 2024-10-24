###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively

#Answer

class Patient:
    """
    A class to represent a patient in the hospital system.
    
    Attributes:
    -----------
    name : str
        The name of the patient.
    symptoms : list of str
        The list of symptoms that the patient has.
    """
    
    def __init__(self, name, symptoms):
        """
        Initialize the Patient with a name and list of symptoms.
        
        Parameters:
        -----------
        name : str
            The patient's name.
        symptoms : list of str
            A list of symptoms the patient is experiencing.
        """
        self.name = name
        self.symptoms = symptoms
        self.tests = {}  # Store test results as a dictionary


#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

#Answer

class Patient:
    """
    A class to represent a patient in the hospital system.
    
    Attributes:
    -----------
    name : str
        The name of the patient.
    symptoms : list of str
        The list of symptoms that the patient has.
    """
    
    def __init__(self, name, symptoms):
        """
        Initialize the Patient with a name and list of symptoms.
        
        Parameters:
        -----------
        name : str
            The patient's name.
        symptoms : list of str
            A list of symptoms the patient is experiencing.
        """
        self.name = name
        self.symptoms = symptoms
        self.tests = {}  # Store test results as a dictionary


#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

#Answer

    def has_covid(self):
        """
        Calculate the probability of the patient having Covid-19.
        
        Returns:
        --------
        float
            The probability that the patient has Covid-19, as a value between 0.0 and 1.0.
        """
        # Special case for "covid" test, keeping it simple and readable
        if "covid" in self.tests:
            return 0.99 if self.tests["covid"] else 0.01

        # Default probability if no covid test is present
        probability = 0.05
        # List of symptoms that increase probability
        risk_symptoms = ['fever', 'cough', 'anosmia']
        
        # Increase probability for each risk symptom present
        for symptom in risk_symptoms:
            if symptom in self.symptoms:
                probability += 0.1

        return min(probability, 1.0)  # Ensure probability doesn't exceed 1.0


######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

#Answer

class Card:
    """
    A class to represent a playing card.
    
    Attributes:
    -----------
    suit : str
        The suit of the card (e.g., 'Hearts', 'Diamonds').
    value : str
        The value of the card (e.g., 'A', '2', 'K').
    """
    
    def __init__(self, suit, value):
        """
        Initialize the card with a suit and a value.
        
        Parameters:
        -----------
        suit : str
            The suit of the card (e.g., 'Hearts', 'Diamonds').
        value : str
            The value of the card (e.g., 'A', '2', '3', 'K').
        """
        self.suit = suit
        self.value = value


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

#Answer

import random

class Deck:
    """
    A class to represent a deck of cards.
    
    Attributes:
    -----------
    cards : list of Card
        The list of cards in the deck.
    """
    
    def __init__(self):
        """
        Initialize the deck with a full set of English playing cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # Create the deck by generating all possible card combinations
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        """
        Shuffle the deck of cards.
        """
        random.shuffle(self.cards)  # Use Python's built-in shuffle method

    def draw(self):
        """
        Draw a card from the top of the deck and remove it from the deck.
        
        Returns:
        --------
        Card or None:
            The drawn card, or None if the deck is empty.
        """
        if len(self.cards) == 0:
            print("No more cards to draw.")
            return None
        card = self.cards.pop(0)  # Remove the top card
        print(f"Drawn card: {card.value} of {card.suit}")
        return card



###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

#Answer

from abc import ABC, abstractmethod

class PlaneFigure(ABC):
    """
    Abstract base class for plane figures, defining a template for perimeter
    and surface calculations.
    """
    
    @abstractmethod
    def compute_perimeter(self):
        """
        Abstract method to compute the perimeter of the figure.
        """
        pass

    @abstractmethod
    def compute_surface(self):
        """
        Abstract method to compute the surface area of the figure.
        """
        pass

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

#Answer

class Triangle(PlaneFigure):
    """
    A class to represent a triangle, inheriting from PlaneFigure.
    
    Attributes:
    -----------
    base : float
        The base of the triangle.
    c1 : float
        The first side of the triangle.
    c2 : float
        The second side of the triangle.
    h : float
        The height of the triangle.
    """
    
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self):
        """
        Compute the perimeter of the triangle.
        
        Returns:
        --------
        float:
            The perimeter of the triangle.
        """
        return self.base + self.c1 + self.c2

    def compute_surface(self):
        """
        Compute the surface area of the triangle.
        
        Returns:
        --------
        float:
            The surface area of the triangle.
        """
        return 0.5 * self.base * self.h

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

#Answer

class Rectangle(PlaneFigure):
    """
    A class to represent a rectangle, inheriting from PlaneFigure.
    
    Attributes:
    -----------
    a : float
        The length of side a.
    b : float
        The length of side b.
    """
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_perimeter(self):
        """
        Compute the perimeter of the rectangle.
        
        Returns:
        --------
        float:
            The perimeter of the rectangle.
        """
        return 2 * (self.a + self.b)

    def compute_surface(self):
        """
        Compute the surface area of the rectangle.
        
        Returns:
        --------
        float:
            The surface area of the rectangle.
        """
        return self.a * self.b

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

#Answer

import math

class Circle(PlaneFigure):
    """
    A class to represent a circle, inheriting from PlaneFigure.
    
    Attributes:
    -----------
    radius : float
        The radius of the circle.
    """
    
    def __init__(

