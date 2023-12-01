a = len("""정부가 내년 1월부터 소주 등 국산 주류에 제조사의 국내 유통 판매관리비 등을 차감해 세금을 부과한다. 
국내 주류 제조사의 세 부담이 수입 주류사보다 높은 역차별을 해소하고, 동시에 국산 주류의 가격 인하를 유도하려는 목적이다.
기획재정부는 1일 국산 주류 과세 시 기준판매비율을 도입하는 내용의 주세법 시행령 및 주세법 시행규칙 개정안을 입법예고한다고 밝혔다.""")

print(f"이 기사의 글자 수는 {a}입니다.")  #띄어쓰기까지 포함.

article = """President Yoon Suk Yeol on Friday granted his approval for the resignation offered by the state broadcasting watchdog chief, effectively derailing the main opposition party's plans to proceed with an impeachment motion originally scheduled for later in the day.

Yoon's approval followed a surprising turn of events, when Korea Communications Commission Chairman Lee Dong-kwan reportedly submitted his resignation to Yoon late Thursday.

"President Yoon has approved KCC Chairman Lee Dong-kwan's resignation request," the president’s office said in a statement released at around noon, without disclosing the specifics behind Yoon’s decision.

The main opposition Democratic Party of Korea introduced a unilateral motion to impeach Lee earlier this week based on its longstanding criticism of him "cracking down on outlets for hostile coverage against the government" and aiding the president’s "efforts to control the press."""

articleLow = article.join(["start ", " end"]) #list 를 한 번 넣어줘야 한다.
print(articleLow)