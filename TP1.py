#par khalil N.B. avec aide de Maxime
#Travail Personel 1

#variable(pour compter le nombre de mots)
def count_words(input_string):
    word_count = len(input_string.split())
    return word_count
    
#Demander la phrase
input_text = input("Écrivez votre phrase: ")
word_count = count_words(input_text)

#donner le nombre de mot total
print(f"nombre de mots:{word_count}")
