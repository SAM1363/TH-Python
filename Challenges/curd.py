models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)
    
  
def search_challenges(name, language):
    challenges = Challenge.select()
    challenges = challenges.where( (Challenge.name==name) | (Challenge.language==language))
    return challenges