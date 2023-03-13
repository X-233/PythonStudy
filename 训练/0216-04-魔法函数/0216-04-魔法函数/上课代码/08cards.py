""""""
"""
    ♠ ♥ ♣ ◆
    2 - 11 - J Q K A
"""
import random
list

# 封装一张牌
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'<{self.suit}-{self.rank}>'


class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = ['♠', '♥', '♣', '◆']

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def __repr__(self):
        return ' '.join([str(card) for card in self._cards])

    def __getitem__(self, position):  # 把列表取值,列表切片的功能暴露出来了 []
        # __getitem__ 里面的逻辑有自己定义
        return self._cards[position]


# card1 = Card('♥', 'A')
# print(card1)
fd = FrenchDeck()
print(fd)
