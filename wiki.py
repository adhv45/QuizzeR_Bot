import wikipedia
import hunspell
#--------------------------------------------------------------------------------------

def check(keyword):
    try:
        search = wikipedia.page(keyword)

    except wikipedia.exceptions.PageError:
        return 1

    except wikipedia.exceptions.DisambiguationError:
       return 2

    except:
        return 3

    return 0

#--------------------------------------------------------------------------------------

def options(keyword):
    options = wikipedia.search(keyword)
    options.pop(0)
    return options  

#--------------------------------------------------------------------------------------

def check_spelling(word):
    hun_spell = hunspell.HunSpell('/usr/share/hunspell/en_US.dic',
        '/usr/share/hunspell/en_US.aff')
    correction = []
    if not hun_spell.spell(word):
        
        suggestion = hun_spell.suggest(word)
        
        if len(suggestion) == 0 :
            suggestion.append(word)

        correction += suggestion

    else:
        correction.append(word)

    return correction[0]

#----------------------------------------------------------------------------------------