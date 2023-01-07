import spacy
nlp = spacy.load('en_core_web_md')

file = open("movies.txt", "r+")
movie_desc = file.readlines() 
file.close()

watched = "Planet Hulk"
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk landed on planet Sakaar where he is sold into salvery and trained as a gladiator."
nlp_watched = nlp(watched)
nlp_description = nlp(description)

similarities = []
movie_similarities = []
def find_similarity(movie_description):
    for line in movie_desc:
        line = line.strip()
        similarity = nlp(line).similarity(movie_description)
        similarities.append(f"{similarity}") #add similarity values to similarities list
        movie_similarities.append(f"{line} - {similarity}") #adds movies + similarity values to list

def which_movie(movie):
    money = "".join(movie).split(":") #splits movie and description up
    return money[0] #prints only movie name
    
find_similarity(nlp_description)
most_similar = max(similarities) #finds most similar movie
recommendation = [i for i in movie_similarities if most_similar in i] #highlights which movie this could be
print(which_movie(recommendation))






    

