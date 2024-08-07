from card import Card
from constants import Constants
from data_structures.stack_adt import ArrayStack
from enum import IntEnum


class Player:
    """
    Player class to store the player details
    """
    def __init__(self, name: str, position: int) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.name = name
        self.position = position
        self.hand: ArrayStack[Card] = ArrayStack(Constants.DECK_SIZE)
    
    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        # If the hand is empty, there is no sorting required.
        if self.hand.is_empty():
            self.hand.push(card)
            # Assume that the hand will never be full, as the size of the stack reaches the deck size. 
        else:
            # Must sort through the stack to determine where to add the card.
            # As the hand is a stack, this removes cards until it reaches the desired position, and then re-inserts everything back into the hand. 
            
            # Creating a temporary stack to hold cards that are before the desired position. 
            temp_stack = ArrayStack(Constants.DECK_SIZE)

            # For loop to cycle through the whole hand (in the worst-case scenario).
            for i in range(len(self.hand)):
                # Peeks at the card at the top of the stack.
                temp = self.hand.peek()
                # Checks if the card on top of the stack should be above or below the card to be inserted. 
                if temp.color > card.color or temp.label > card.label:
                    # If it is, put it in the temporary stack. 
                    temp_stack.push(self.hand.pop())
                else:
                    # Else, the card should be placed here, and the temporary stack should be emptied back into the hand. 
                    self.hand.push(card)
                    break
            # Temporary stack emptied back into the hand.
            while not temp_stack.is_empty():
                self.hand.push(temp_stack.pop)
                

    def play_card(self, index: int) -> Card:
        """
        Method to play a card from the player's hand

        Args:
            index (int): The index of the card to be played

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        temp_stack = ArrayStack(Constants.DECK_SIZE)
        for _ in range(len(self.hand) - 1):
            temp_stack.push(self.hand.pop())
        card = self.hand.pop()
        while not temp_stack.is_empty:
            self.hand.push(temp_stack.pop())
        return card
    
    def __len__(self) -> int:
        """
        Method to get the number of cards in the player's hand

        Args:
            None

        Returns:
            int: The number of cards in the player's hand

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return len(self.hand)

    def __getitem__(self, index: int) -> Card:
        """
        Method to get the card at the given index from the player's hand

        Args:
            index (int): The index of the card to be fetched

        Returns:
            Card: The card at the given index from the player's hand

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        temp_stack = ArrayStack(Constants.DECK_SIZE)
        for _ in range(len(self.hand) - 1):
            temp_stack.push(self.hand.pop())
        card = self.hand.peek()
        while not temp_stack.is_empty:
            self.hand.push(temp_stack.pop())
        return card

