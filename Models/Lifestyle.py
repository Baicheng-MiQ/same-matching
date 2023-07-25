class Lifestyle:
    def __init__(self,
                 routine: str,
                 smoking: bool,
                 drinking: bool,
                 drugs: bool,):
        
        """
        Life style
        https://docs.google.com/document/u/0/d/1q7MQJj6M989IIZSUd7sNEfAGFgItbC5tmE_1qyNdtPo/mobilebasic
        """
        if routine not in ['Night Owl', 'Early bird']:
            raise ValueError("Routain not valid")
        self.routine = routine
        self.smoking = smoking
        self.drinking = drinking
        self.drugs = drugs

    @staticmethod
    def fetch(uid: str) -> 'Lifestyle':
        """
        Fetches the lifestyle for a user.
        :param uid: str
        :return: Lifestyle
        """
        raise NotImplementedError()
    
    def score(self, them: 'Lifestyle') -> float:
        """
        Calculates the compatibility score between two lifestyles based on their routine, smoking, drinking, and drug habits.
        If both parties have the same habit, the score increases by 1, otherwise it decreases by 1.
        :param them: Another instance of the Lifestyle class to compare with.
        :return: A float representing the compatibility score between two lifestyles.
        https://docs.google.com/document/u/0/d/1q7MQJj6M989IIZSUd7sNEfAGFgItbC5tmE_1qyNdtPo/mobilebasic
        """
        score = 0
        if self.routine == them.routine:
            score += 1
        else:
            score -= 1

        if self.smoking == them.smoking:
            score += 1
        else:
            score -= 1

        if self.drinking == them.drinking:
            score += 1
        else:
            score -= 1

        if self.drugs == them.drugs:
            score += 1
        else:
            score -= 1
            
        return score