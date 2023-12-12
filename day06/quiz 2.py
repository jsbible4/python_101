article1 = """A legislative move to ban the consumption of dog meat is losing steam as rival parties have yet to reach a consensus over the issue amid fierce opposition from dog meat traders.

According to political circles and animal activists, Sunday, the anti-dog meat bill is still pending at the National Assembly, as the main opposition Democratic Party of Korea (DPK) is refusing to cooperate with the ruling People Power Party (PPP) over the legislation at the Agriculture, Food, Rural Affairs, Oceans and Fisheries Committee.

For the bill to pass in the 21st Assembly as promised by both parties, it needs to pass the standing committee and the Legislation and Judiciary Committee before finally winning a majority of votes by present lawmakers at the extra plenary sessions, slated for Dec. 20, 28 and Jan. 9 next year.

The ruling party stressed that the legislation must pass during the extra plenary sessions next week.

“The ban on dog meat consumption needs to be finalized in the 21st National Assembly. The subject has been controversial for decades and went through long debates, so the Assembly must achieve a fruitful result,” the PPP’s chief policymaker Rep. Yu Eui-dong said, Friday, as the Assembly's regular annual session concluded without a result."""

article2 = """According to a survey whose results were released on Sunday by the Kyosu Sinmun, a weekly newspaper for scholars, 396 out of 1,315 respondents (30.1 percent) voted for the expression as this year’s idiom.

Kim Byung-ki, a Jeonbuk National University professor emeritus who had recommended the idiom, said an every-man-for-himself attitude prevailed in the country where virtues were largely forgotten and forsaken as a result.

“Due to selfish thoughts and the pervasive tendency to justify (what is wrong), many fraud cases have occurred,” Kim wrote. “Gyeon-li-mang-ui might bring gains (to individuals), but it will eventually lead to destruction.”

As examples of the concerning trend, he pointed to the widespread rental housing scams and the frequent violations of teachers’ rights and authority at schools.

One of the professors who had voted for the idiom called on political leaders to do more to set good examples, saying they appear to be interested mostly in political gain instead of their responsibilities, particularly in recent years."""

article1_list = article1.split()
article2_list = article2.split()
article1_list_set = set(article1_list)
article2_list_set = set(article2_list)
a = article1_list_set.intersection(article2_list_set)
list = list(a)
list.sort()
print(list)

print(len(list)) #len은 리스트안의 요소 개수 셀 때도 사용할 수 있다. 