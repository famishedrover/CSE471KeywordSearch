from youtube_transcript_api import YouTubeTranscriptApi



# links = [
# "https://www.youtube.com/watch?v=YvjxmzViVUQ&list=PLNONVE5W8PCSidtkzzeRbrFiC2CO8_uZe",
# "https://www.youtube.com/watch?v=IEoeiS7p_p8&list=PLNONVE5W8PCSidtkzzeRbrFiC2CO8_uZe&index=2",
# "https://www.youtube.com/watch?v=THOzEdkYeac&list=PLNONVE5W8PCSidtkzzeRbrFiC2CO8_uZe&index=3"
# "https://www.youtube.com/watch?v=bAj8Dt33Z90&list=PLNONVE5W8PCSidtkzzeRbrFiC2CO8_uZe&index=4",

# "https://www.youtube.com/watch?v=SMupjRvULU4&list=PLNONVE5W8PCQhLjuA5dHkYETzXcbvoIVX&index=1",




# ]





playlistLinks = [

"https://www.youtube.com/watch?v=h4epjAW_eAE&list=PLNONVE5W8PCT5IeGslE02deg7ZWvOX_rC",
"https://www.youtube.com/watch?v=u2bvxSHWALQ&list=PLNONVE5W8PCSE60w-ZJbix4PMzBsvZ7Ep",
"https://www.youtube.com/watch?v=ds6EK_P2EF8&list=PLNONVE5W8PCSRQBw3yzbtouueDXn0AKdG",
"https://www.youtube.com/watch?v=M87_xmCpY4o&list=PLNONVE5W8PCSBhlYuV0MDcCfdLidLxl8c",
"https://www.youtube.com/watch?v=d9oW_Z8Bzes&list=PLNONVE5W8PCQvJ_Ct8Q57wIvTAjZsh1W2",
"https://www.youtube.com/watch?v=Tzb49vKDnRQ&list=PLNONVE5W8PCTQ7dyOY0jb2bGALdDpMfPD",
"https://www.youtube.com/watch?v=ahhSv1gbVpM&list=PLNONVE5W8PCTUwzLk_iIYj2c0GpjdhFYd",
"https://www.youtube.com/watch?v=yS6kBZ000Ow&list=PLNONVE5W8PCRLh2YMsnlBcqiKYliT-frH",
"https://www.youtube.com/watch?v=10UVEjfTW0g&list=PLNONVE5W8PCSnhYfEtY6N2qdXjyTuX1H4",
"https://www.youtube.com/watch?v=lLKlucs599c&list=PLNONVE5W8PCRGfBsqFDImcUG_BbnWyW4S",
"https://www.youtube.com/watch?v=nwXHTaf-sjE&list=PLNONVE5W8PCQDuCUL3H5t2g8qe-dvC0vi",
"https://www.youtube.com/watch?v=6FwEHjHfr9Y&list=PLNONVE5W8PCQWSokrg-rIxWIA5TFyTgpP",
"https://www.youtube.com/watch?v=ETOOME0xT4c&list=PLNONVE5W8PCQf-uQbnU8VHDo3J2X66Qdv",
"https://www.youtube.com/watch?v=cidZDgl1Xpw&list=PLNONVE5W8PCR6eLXrh7tw64tI_XE6Ykpc",
"https://www.youtube.com/watch?v=fL_Rh_yqYmQ&list=PLNONVE5W8PCQH1Z0ZhhfqV7a-qtYS6Kpt",
"https://www.youtube.com/watch?v=YON9A2KvEA4&list=PLNONVE5W8PCSVSawbk1ARd5FrabmteaeV",
"https://www.youtube.com/watch?v=CQGmYZnxhTk&list=PLNONVE5W8PCSmrVO1bRRI9Npk4OEOpfWO",
"https://www.youtube.com/watch?v=d0NHHk_n7tc&list=PLNONVE5W8PCTN2taapDkmvD1khmCMlni9",
"https://www.youtube.com/watch?v=-jRucRAhOP0&list=PLNONVE5W8PCRYVdXAM7ClvKsCBfZLeXjx",
"https://www.youtube.com/watch?v=vbiA_z8-SK8&list=PLNONVE5W8PCSceKYK6fZO5hapnwcCRMQm",
"https://www.youtube.com/watch?v=Phz3CdF3BJM&list=PLNONVE5W8PCSUy-fMAuxXymhqRelQuTC7",
"https://www.youtube.com/watch?v=ie2Ko3RqOq4&list=PLNONVE5W8PCQfTVCZM_N4pIg2SpwYPV3Y",
"https://www.youtube.com/watch?v=LKMj9F8nNyM&list=PLNONVE5W8PCTe2LU50ktyR0dn58247YCa",
"https://www.youtube.com/watch?v=IzmZ-GiqXi4&list=PLNONVE5W8PCT6-rteE3hkFVshJnDLY8Do",
"https://www.youtube.com/watch?v=SMupjRvULU4&list=PLNONVE5W8PCQhLjuA5dHkYETzXcbvoIVX",
"https://www.youtube.com/watch?v=YvjxmzViVUQ&list=PLNONVE5W8PCSidtkzzeRbrFiC2CO8_uZe"


]


from pytube import YouTube
from pytube import Playlist
import pickle


# allLinks = []

# for links in playlistLinks :
# 	print (links)
# 	pl = Playlist(links)
# 	pl.populate_video_urls()

# 	allLinks += pl.video_urls

# print (allLinks)
# print (len(allLinks))


# with open('allLinks.pkl', 'wb') as f:
# 	pickle.dump(allLinks, f)

# ALL LINKS have all the video links 
# obtainign videoIDs 

allLinks = []

with open('allLinks.pkl', 'rb') as f:
	allLinks = pickle.load(f)

allLinkIds = []

for link in allLinks :
	alink = link.split("watch?v=")[1]
	allLinkIds.append(alink)

print (allLinkIds)



for t in range(len(allLinkIds)) : 
	print ('AT ',t)
	try : 
		file1 = open("./captions/tra"+str(t)+".txt","w") 
		ob = YouTubeTranscriptApi.get_transcript(allLinkIds[t])
		for k in range(len(ob)) :
			file1.write(ob[k]["text"])
	except : 
		print('FAILED :', allLinkIds[t])
	file1.close()

