article = """HONG KONG — In an alarming trend, millennials, born between 1981 and 1996, 
have become the subject of a paradox: they are facing a faster decline in health compared to older generations despite a heightened awareness of fitness among younger people.

This perplexing phenomenon, initially identified in the United States, is now resonating across major Asian countries,
 including Korea, Hong Kong and Singapore, countering conventional expectations that the health-savvy younger generation would enjoy increased longevity.

According to a 2020 study by medical insurer Blue Cross Blue Shield in the United States, 
millennials face an accelerated deterioration in both physical and mental health, with conditions such as hypertension, high cholesterol, depression, and anxiety disorders appearing at an earlier age compared to older generations.

For example, Korean millennials are positioned to outpace their parents in aging, Hong Kong is observing an alarming rise in age-related ailments, 
and the younger generation in Singapore finds itself susceptible to an accelerated decline in health."""

words = article.split() # list()는 음절단위로 리스트화 시킴, str.split()는 어절 단위로 리스트화 됨.(띄어쓰기 기준)
words.sort()#여기까지 공백 기준으로 찢고 단어 리스트 만들고 오름차순으로 정렬함.
setWords = set(words) #단어 리스트를 set 화 시킴. # 대신 순서가 없음
listedWords = list(setWords) # 중복 제거된 setWords를 리스트화 해서 순서를 생성한다.
listedWords.sort() # a 부터 오름차순으로 정렬함. #순서가 있는 상태에서 정렬해야 한다. 

print(setWords)


