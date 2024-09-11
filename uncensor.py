
# todo C*ns*r*d Str*ngs
# ? Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

# ? Given a censored string and a string of the censored vowels, return the original uncensored string.

# ! Example
# * uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

# * uncensor("abcd", "") ➞ "abcd"

# * uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
# ! Notes
# ? The vowels are given in the correct order.
# ? The number of vowels will match the number of * characters in the censored string.




def uncensor(censored_str, vowels):
    vowel_iter = iter(vowels)  
    uncensored = []

    for char in censored_str:
        if char == '*':
            uncensored.append(next(vowel_iter))  
        else:
            uncensored.append(char) 

    return ''.join(uncensored)


print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))  
print(uncensor("abcd", ""))  
print(uncensor("*PP*RC*S*", "UEAE"))  

# ! ///////////////////////////////////////////////////////



def uncensor(txt, vowels):
    x = txt.replace("*", "{}")  # Replace each '*' with a placeholder '{}'
    return x.format(*vowels)  # Unpack the vowels so that each '{}' is replaced by a vowel

# Test cases
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))  # ➞ "Where did my vowels go?"
print(uncensor("*PP*RC*S*", "UEAE"))  # ➞ "UPPERCASE"

