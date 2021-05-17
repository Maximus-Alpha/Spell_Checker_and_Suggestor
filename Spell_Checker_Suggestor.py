import re
import pkg_resources
from symspellpy import SymSpell, Verbosity


#Our input term
input_term='amaaziing'

#Setting up the symspell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt")

# term_index is the column of the term
# count_index is thecolumn of the term frequency
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)


[print(item) for item in sym_spell.lookup(input_term, Verbosity.ALL,
                               max_edit_distance=2, include_unknown=True)]



#Multiple Words
input_compound_term = 'i went to the amaazzing wefle house on the hiighway'

top_suggestion = str([*sym_spell.lookup_compound(input_compound_term,max_edit_distance=2)][0])



#Find the acutal commas
comma_locs = [m.start() for m in re.finditer(',',top_suggestion)]

#Extract the text
top_suggestion_text = top_suggestion[:comma_locs[-2]]

#if the suggestion equals the initial text, then everything was spelled correctly, else, write the suggestion

if input_compound_term.split()==top_suggestion_text.split():
    print(input_compound_term)
else:
    holding_list=[] #Holds the words from our initial search and the suggested terms
    for a,b in zip(input_compound_term.split(),top_suggestion_text.split()):
        if a==b:
            holding_list.append(a)
        else:
            holding_list.append("{0}{1}{0}".format("**",b))
    
    
    print("Did you mean: {}?".format(' '.join(holding_list)))

