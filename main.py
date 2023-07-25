from fastapi import FastAPI
from Models.User import User

app = FastAPI()

@app.post("/match")
async def match(uid: str):
    """
    Returns a list of users that are compatible with the user with the given uid.
    """
    raise NotImplementedError()

    user = User.fetch(uid)
    users_db = []
    top_matches = []
    for this_user_uid in users_db:
        this_score = user.score(User.fetch(this_user_uid))
        if this_score > 0.7:
            if len(top_matches) < 2:
                top_matches.append({'uid': this_user_uid, 'score': this_score})
            else:
                top_matches.sort(key=lambda x: x['score'], reverse=True)
                if this_score > top_matches[1]['score']:
                    top_matches[1] = {'uid': this_user_uid, 'score': this_score}
    return top_matches
                
