# Background 
How many Eugenes are there in Singapore? For some reason, "Eugene" is an unusually popular name in the country, especially considering the bad rep Eugenes get in the media - think Eugene Krabbs from Spongebob or Eugene Porter from the Walking Dead. It has pretty uncool connotations. Even Flynn Rider from Tangled swapped his name out from Eugene out of embarrassment. In any case, I needed to confirm whether Eugene really was particularly popular in Singapore.

# Process
## Dead Ends
First, I needed a sample of names. However, there isn't a readily available database on Singstats or data.gov.sg and my email request was understandably turned down. Using [university commencement lists](https://courses.nus.edu.sg/course/elltankw/names.pdf) was out since universities started restricting access a couple years ago. Facebook graph search was limited and scraping graph search data would've been a violation of TOS. Plus Graph API didn't have the data I wanted.

## SGDI
Luckily, the Singapore government has a [great civil service database](https://www.gov.sg/sgdi/ministries) with well-structured sitemaps (e.g. a name div). I was able to scrape about 14,000 names using the database. I also estimated gender using salutations (e.g. Mr vs Ms). While the SGDI has a fairly regular format ([Salutation] LASTNAME Firstname [Title]), the vagaries of Singaporean names (e.g. Malay last names, Chinese first names vary significantly from standard American formats) as well as plain bad formatting (check the forbidden list) led to a couple of misses.

# Results
Approximately 0.431% of males in the samples had Eugene in their first names. In comparison, 0.230% of males are named Eugene in the U.S. Looking at baby name statistics for more recent years (Eugene is kind of a grandpa name; it was most popular in the US in 1929), the disparity is wider - 0.005% in the UK (1996) and 0.022% in the US (2000).

# Conclusions
It's hard to determine the statistical significance of the sample, but it doesn't disconfirm my suspicion that there is a disproportionate number of Eugenes in Singapore. A far-fetched theory is that the prevalence of "eugenics" as an actual acceptable term in public discourse [from the 1970s](http://www.jstor.org/stable/40230009?seq=1#page_scan_tab_contents) up till around then-PM Lee Kuan Yew's [1983 National Day Rally Speech](http://www.straitstimes.com/singapore/from-babies-to-casinos-10-memorable-national-day-rally-speeches) (for some reason, the full text isn't available on the official NAS online archive) embedded the name in the public consciousness. In any case, until more public data (tied to birth year) is found, it's inconclusive.

# SGDI Terms of Use
SGDI [Terms of Use](https://www.gov.sg/terms-of-use)
