# fathah
Lightweight NLP preprocessing package for Arabic language

## Installation
```sh
pip install fathah
```
## Usage
```python
from Fathah import TextClean
```

## Methods 

 ### Clean the text 
`clean_text` function includes all these functions:   
  >      1. remove_emails  
  >      2. remove_URLs  
  >      3. remove_mentions   
  >      4. hashtags_to_words     
  >      5. remove_punctuations  
  >      6. normalize_arabic   
  >      7. remove_diacritics   
  >      8. remove_repeating_char   
  >      9. remove_stop_words   
  >      10. remove_emojis

 In other words, `clean_text` includes all functions except `remove_hashtags` 
```
text_cleaned1 = TextClean.clean_text(text)
print(text_cleaned1)
```

 ### Remove repeating character
`remove_repeating_char` function
```
text_cleaned2 = TextClean.remove_repeating_char(text)
print(text_cleaned2)
```

 ### Remove punctuations
`remove_punctuations` function
```
text_cleaned3 = TextClean.remove_punctuations(text)
print(text_cleaned3)
```

 ### Normalize Arabic
`normalize_arabic` function

```
text_cleaned4 = TextClean.normalize_arabic(text)
print(text_cleaned4)
```

 ### Remove diacritics
`remove_diacritics` function
```
text_cleaned5= TextClean.remove_diacritics(text)
print(text_cleaned5)
```

 ### Remove stop words
`remove_stop_words` function
```
text_cleaned6 = TextClean.remove_stop_words(text)
print(text_cleaned6)
```

 ### Remove emojis
`remove_emojis` function
```
text_cleaned7 = TextClean.remove_emojis(text)
print(text_cleaned7)
```

 ### Remove mentions
`remove_mentions` function
```
text_cleaned8 = TextClean.remove_mentions(text)
print(text_cleaned8)
```

 ### Convert any hashtags to words
`hashtags_to_words` function
```
text_cleaned9 = TextClean.hashtags_to_words(text)
print(text_cleaned9)
```

 ### Remove hashtags
`remove_hashtags` function
```
text_cleaned10 = TextClean.remove_hashtags(text)
print(text_cleaned10)
```

 ### Remove emails
`remove_emails` function
```
text_cleaned11 = TextClean.remove_emails(text)
print(text_cleaned11)
```

 ### Remove URLs
`remove_URLs` function
```
text_cleaned12 = TextClean.remove_URLs(text)
print(text_cleaned12)
```


## Example
```python
from fathah import TextClean

cleaner = TextClean(text)
cleaner.remove_diacritics()

# Outputs: السلام عليكم ورحمة الله وبركاته
```


*This package is under development. Contributions are highly welcome*

[Github](https://github.com/fathah) | [IG](https://instagram.com/fatha_cr)