from typing import List
import string
class PersonalValue:
    def __init__(self,
                 q1:str,
                 q2:str,
                 q3:str,
                 q4:str,
                 q5:str,
                 q6:str,
                 q7:List[str],
                 q8:List[str]):
        """
        https://docs.google.com/document/d/1ATTIU-eJ7FP26li9UubxoWAN19z_T3OZw2ce_rdQoPg/edit
        :param q1: In order for a long-lasting relationship, which do you think is most important?
        :param q2: Which of the following descriptions about having sex do you agree with the most??
        :param q3: You have just received your monthly salary from your company. You choose to:
        :param q4: What do you think is more important for happiness?
        :param q5: Which of the following friendship situations do you prefer?
        :param q6: Which of the following descriptions about marriage do you agree with the most?
        :param q7: What do you think is the most important factor for a partner? Please choose top 3
        :param q8: Select values that resonate with you most (Please select your Top 5 values from the list below)
        """
        if q1 not in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            raise ValueError('Invalid answer to question 1')
        if q2 not in ['a', 'b', 'c', 'd', 'e']:
            raise ValueError('Invalid answer to question 2')
        if q3 not in ['a', 'b', 'c', 'd']:
            raise ValueError('Invalid answer to question 3')
        if q4 not in ['a', 'b', 'c']:
            raise ValueError('Invalid answer to question 4')
        if q5 not in ['a', 'b', 'c']:
            raise ValueError('Invalid answer to question 5')
        if q6 not in ['a', 'b', 'c', 'd']:
            raise ValueError('Invalid answer to question 6')

        if len(q7) != 3:
            raise ValueError('Invalid answer to question 7, must be a list of 3 strings')
        if not all(q in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] for q in q7):
            raise ValueError('Invalid answer to question 7')

        if len(q8) != 5:
            raise ValueError('Invalid answer to question 8, must be a list of 5 strings')
        if not all(q in list(string.ascii_lowercase)+['aa','bb','cc','dd','ee','ff'] for q in q8):
            raise ValueError('Invalid answer to question 8')

        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8

    @staticmethod
    def fetch(uid: str) -> 'PersonalValue':
        """
        Fetches the personal value for a user.
        :param uid: str
        :return: PersonalValue
        """
        raise NotImplementedError()

    def score(self, them: 'PersonalValue') -> float:
        """
        https://docs.google.com/document/d/1ATTIU-eJ7FP26li9UubxoWAN19z_T3OZw2ce_rdQoPg/edit
        |      | Same (each answer) | Different (each answer) |
        |------|--------------------|-------------------------|
        | Q1-6 | +1                 | -1                      |

        | Same answer | 0  | 1 | 2 | 3+ |
        |-------------|----|---|---|----|
        | Q7          | -1 | 1 | 2 | 3  |
        | Q8          | -1 | 1 | 2 | 3  |
        
        :param them: Another instance of the PersonalValue class to compare with.
        :return: A float representing the compatibility score between two PersonalValue.

        """
        score = 0
        for i in range(1, 7):
            if getattr(self, f'q{i}') == getattr(them, f'q{i}'):
                score += 1
            else:
                score -= 1

        q7_same = len(set(self.q7) & set(them.q7))
        if q7_same == 0:
            score -= 1
        elif q7_same == 1:
            score += 1
        elif q7_same == 2:
            score += 2
        else:
            score += 3

        q8_same = len(set(self.q8) & set(them.q8))
        if q8_same == 0:
            score -= 1
        elif q8_same == 1:
            score += 1
        elif q8_same == 2:
            score += 2
        else:
            score += 3

        return score

        