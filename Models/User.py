from typing import List, Optional
from Lifestyle import Lifestyle
from AttachmentStyle import AttachmentStyle
from PersonalValue import PersonalValue
from Personality import Personality

class User:
    def __init__(self,
                 uid: int,
                 gender: str,
                 looking_for: str,
                 religion: str,
                 hobbies: List[str],
                 lifestyle: 'Lifestyle',
                 attachment_style: 'AttachmentStyle',
                 personal_value: 'PersonalValue',
                 personality: 'Personality'):
        """
        https://docs.google.com/document/u/0/d/1q7MQJj6M989IIZSUd7sNEfAGFgItbC5tmE_1qyNdtPo/mobilebasic

        """

        self.uid = uid

        if gender not in ['male', 'female']:
            raise ValueError("Gender not valid")
        self.gender = gender

        if looking_for not in ['male', 'female', 'both']:
            raise ValueError("Looking for not valid")
        self.looking_for = looking_for
        
        self.religion = religion
        self.hobbies = hobbies
        self.lifestyle = lifestyle
        self.attachment_style = attachment_style
        self.personal_value = personal_value
        self.personality = personality

    @staticmethod
    def fetch(uid: str) -> 'User':
        """
        Fetches the user with the given uid.

        Args:
            uid (str): The uid of the user to fetch.

        Returns:
            User: The user with the given uid.
        """
        raise NotImplementedError()

    def score(self, them: 'User') -> float:
        """
        Calculates the compatibility score between two users based on their attributes.

        Args:
            them (User): The other user to compare to.

        Returns:
            float: The compatibility score between the two users.
        """
        if (self.looking_for != 'both' and self.looking_for!=them.gender) \
                or (them.looking_for != 'both' and them.looking_for!=self.gender): return -999999

        religion_score = (1 if self.religion == them.religion else -1) * 0.2
        hobbies_score = 0.12 if len(set(self.hobbies).intersection(set(them.hobbies))) >= 1 else -0.12
        lifestyle_score = self.lifestyle.score(them.lifestyle) * 0.14
        attachment_style_score = self.attachment_style.score(them.attachment_style) * 0.18
        personal_value_score = self.personal_value.score(them.personal_value) * 0.2
        personality_score = self.personality.score(them.personality) * 0.16

        return religion_score + hobbies_score + lifestyle_score + attachment_style_score + personal_value_score + personality_score

