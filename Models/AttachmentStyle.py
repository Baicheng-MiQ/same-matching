class AttachmentStyle:
    def __init__(self, style: str):
        """
        https://docs.google.com/document/d/1f9Vml8HGMrAxAXFmA_wsN1QyoOwCQbsTzlGbWkq5MV0/edit
        secure = low avoidance and low anxiety
        fearful-avoidant = high avoidance and high anxiety
        dismissing-avoidant  = high avoidance and low anxiety
        preoccupied  = low avoidance and high anxiety

        :param style: str
        """

        if style not in ["secure", "fearful-avoidant", "dismissing-avoidant", "preoccupied"]:
            raise ValueError(f"Attachment style {style} is not valid")
        self.style = style

    @staticmethod
    def fetch(uid: str) -> 'AttachmentStyle':
        """
        Fetches the attachment style for a user.

        :param uid: str
        :return: AttachmentStyle
        """
        raise NotImplementedError()

    def score(self, them: 'AttachmentStyle') -> float:
        """
        Calculates the compatibility score between two attachment styles.
        https://docs.google.com/document/d/1sU_YjiYJsIpN7oQe2DJxVzI-hQ_9KafH/edit

        :param them: AttachmentStyle
        :return: float
        """
        scores = {
            ("secure", "secure"): 1.0,
            ("secure", "preoccupied"): 0.5,
            ("secure", "dismissing-avoidant"): -1.0,
            ("secure", "fearful-avoidant"): 0.5,
            ("preoccupied", "secure"): 0.5,
            ("preoccupied", "anxious-preoccupied"): -0.5,
            ("preoccupied", "dismissing-avoidant"): -1.0,
            ("preoccupied", "fearful-avoidant"): -0.5,
            ("dismissing-avoidant", "secure"): -1.0,
            ("dismissing-avoidant", "preoccupied"): -1.0,
            ("dismissing-avoidant", "dismissing-avoidant"): 0.0,
            ("dismissing-avoidant", "fearful-avoidant"): -0.5,
            ("fearful-avoidant", "secure"): 0.5,
            ("fearful-avoidant", "preoccupied"): -0.5,
            ("fearful-avoidant", "dismissing-avoidant"): -0.5,
            ("fearful-avoidant", "fearful-avoidant"): 0.5,
        }
        try:
            return scores[(self.style, them.style)] # type: ignore
        except KeyError:
            raise ValueError(f"Cannot calculate compatibility score between {self.style} and {them.style}")
