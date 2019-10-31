# Max Base
# https://github.com/BaseMax
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://en-maktoob.yahoo.com/?p=us')

items = browser.find_elements_by_css_selector('#Stream > li')
for item in items:
	title = item.find_element_by_css_selector('h3 a span').get_attribute('innerHTML')
	text = item.find_element_by_css_selector('p').get_attribute('innerHTML')
	print(title)
	print(text)
	print("--------------")

browser.quit()

# Output Result
'''
US releases footage, provides more detail on al-Baghdadi raid
The general who oversaw the United States raid on the compound of the Islamic State of Iraq and the Levant (ISIL or ISIS) leader provided the most detailed account yet of the operation and said the US was on alert for possible "retribution attacks". General Frank McKenzie, head of US Central Command, said on Wednesday Abu Bakr al-Baghdadi's remains were buried at sea within 24 hours of his death inside an underground tunnel where he fled as special operations soldiers closed in on him.
--------------
Iranian general flies into Baghdad to chair top security meeting amid protests
Iranian General Qassem Soleimani, the commander of the Islamic Revolutionary Guard Corps - Quds Force, had visited Baghdad and took a helicopter to the heavily fortified Green Zone where he secretly met with a group of top security officials, the Associated Press reported citing two senior officials familiar with the meeting. According to the two sources, the visit came on the day after anti-government protests first erupted in Iraq more than a month ago. Soleimani is said to have surprised a group of top security officials by chairing a meeting in place of the prime minister. The arrival of Soleimani, the head of Iran's elite Quds Force and the architect of its regional security apparatus, signaled
--------------
Saudi Aramco shares to start trading in December: report
RIYADH, Saudi Arabia (AP) - The long-planned initial public offering of a sliver of Saudi Arabia's state-run oil giant Saudi Aramco will see shares traded on Riyadh's stock exchange in December, a Saudi-owned satellite news channel reported Tuesday as the kingdom's marquee investment forum got underway. The report by Dubai-based Al-Arabiya offered a crackle of life to the Future Investment Initiative in the kingdom's capital of Riyadh, an event created by Saudi Crown Prince Mohammed bin Salman. Initial panels at the forum offered a pessimistic look at a world as participants described the global economy as a teetering on a 1930s-level crisis. Prince Mohammed, however, hopes for a very-optimistic
--------------
Malaysian queen's food gift spices up soured relations with Singapore
ISLAMABAD: Pakistan Prime Minister Imran Khan faces the first major challenge to his leadership this week as a grey-bearded, orange-turbaned rival he calls “Maulana Diesel” marches to Islamabad with thousands of supporters hoping to bring down the government. Maulana Fazlur Rehman - one of the country's most seasoned political operators - has dominated the airwaves in recent days with his calls to unseat his old adversary Khan. The prime minister, he says, did not win last year's election, but was “selected” by the powerful security establishment - a suggestion denied by Khan, but spread widely by Pakistan's opposition since even before the July 2018 election. “This movement will continue until
--------------
Work set to start on $3.5bn King Hamad Causeway mega project
The King Fahad Causeway Authority on Tuesday signed a consultancy agreement worth around $8.9 million to start work on the $3.5 billion project linking Bahrain and Saudi Arabia. A winning consortium of KPMG, AECOM and CMS, a mix of financial, technical, and legal companies, will work on developing the financing model, design, of the mega project as well as the helping with the assement and selection of the main developers. Running parallel to the existing King Fahad Causeway, the causeway is expected to be about 25km long and will carry passenger trains, freight trains and vehicles to reduce the traffic on the King Fahad Causeway. Kamal bin Ahmed Mohammed, Bahrai's Minister of Transportation and Telecommunications, said: “We are pleased to announce the appointment of the main consultancy consortium to start developing all necessary requirements and the financial model required for the construction of the new King Hamad Causeway.
--------------
Tamiur asks Paparazzi to stop!
Ever since Saif Ali Khan, Kareena Kapoor and yes - Taimur Ali Khan's neighbours complained about the constant presence and interference of the shutterbugs outside their house - dur to the posse of paparazzi outside their building - Taimur's parents have taught him to say no to the paps. And the little one used the opportunity on Diwali to tell the paparazzi to keep their lens off him. While he did tell the paparazzi once with courtesy - “No pictures please” -&nbsp; this time around he was clear that he did not want to be clicked. “Taimur waddled across the building compound with his mother oblivious of the fact that we were there. As we saw him there was a commotion as we got ready to click his pictures.
--------------
North Korea fires unidentified projectiles as nuke talks stalled
North Korea fired two projectiles towards its eastern sea on Thursday as nuclear talks between Pyongyang and Washington remain at a deadlock. South Korea's Joint Chiefs of Staff did not immediately confirm whether the weapons were rockets, artillery or ballistic missiles, or how far they flew. "We are maintaining readiness and monitoring in case of additional launches," it said in a statement. Japan's coast guard said the projectiles appeared to be missiles and landed outside Japan's Exclusive Economic Zone (EEZ), which extends 200 nautical miles (370km) from land. The North's latest launch follows statements of displeasure over the slow pace of nuclear negotiations with the United States and
--------------
'''
