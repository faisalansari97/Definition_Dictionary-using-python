# Definition_Dictionary-using-python

Enter your word and find the definition of it. 
If you enter mismatch query, the program will automatically find the word you are searching for and suggest you with the word you are looking for just like google search.

-How it is programmed?

1) First the user is prompted for the word he want to search for?

2) As soon as the word is entered it converts it into lowercase. 
  (Some user will enter MatHematics or some will MATHEMATICS so it is necessarry to convert the string to lowercase as in your .json file)
  
3) After which the program searches for the matches in the data.json. Here conditionl statements are used in program to return output for
   different matches.
   
4) difflib library of python is used in this program to match the sequence ratio of input word and suggest the related word to the user.

5) User can enter query in different ways. This Program is capable of handling any type of input and deliver the best possible related word user is searching for.
