# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(text):
    first_letter= text[0]
    inbetwn_letter = text[1:3]
    fourth_letter = text[3]
    rest = text[4:]
    return first_letter.capitalize() + inbetwn_letter + fourth_letter.capitalize() + rest
    
print(old_macdonald('macdonald'))