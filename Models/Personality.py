class Personality:
    def __init__(self,
                 openness: int,
                 agreeableness: int,
                 conscientiousness: int,
                 neuroticism: int,
                 extroversion: int):
        """
        https://docs.google.com/document/d/19SebWZ9cIqXi0okSGv2QFq0OIXZA3-qN7i6_47m8yGU/edit
        :param openness: to experience
        :param agreeableness:
        :param conscientiousness:
        :param neuroticism:
        :param extroversion:
        """
        self.openness = openness
        self.agreeableness = agreeableness
        self.conscientiousness = conscientiousness
        self.neuroticism = neuroticism
        self.extroversion = extroversion

    @staticmethod
    def fetch(uid: str) -> 'Personality':
        """
        Fetches the personality for a user.
        :param uid: str
        :return: Personality
        """
        raise NotImplementedError()

    def score(self, them: 'Personality') -> float:
        """
        https://docs.google.com/document/d/19SebWZ9cIqXi0okSGv2QFq0OIXZA3-qN7i6_47m8yGU/edit
        Within 20% similarity for each factor +1 (per factor); otherwise -1
        """
        score = 0
        for factor in ['openness', 'agreeableness', 'conscientiousness', 'neuroticism', 'extroversion']:
            our_score = getattr(self, factor)
            their_score = getattr(them, factor)
            similarity = min(our_score, their_score) / max(our_score, their_score)
            if similarity >= 0.8:
                score += 1
            else:
                score -= 1
        return score