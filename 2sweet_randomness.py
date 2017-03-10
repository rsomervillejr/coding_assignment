#sweet randomness
#
#approach:
#1. read in list of ad ids
#2. randomly select an ad id index
#3. for each select ad id, create a dict entry to mark it "shown"
#4. if key of randomly selected ad id exists, then try another randomly selected id until enough ads have been selected
import sys
from random import randint

ad_file = sys.argv[1]
num_ads_to_print = int(sys.argv[2])
ad_list = []
with open(ad_file) as fp:
    for ad_id in fp:
        ad_list.append(ad_id)
ad_hist = {}
i=0
cycles=0
while i < num_ads_to_print:
    selected_ad = ad_list[randint(0,len(ad_list)-1)]
    try:
        if ad_hist[selected_ad] == 'shown':
            pass
    except:
        print 'showing ad id:%s' % str(selected_ad)
        ad_hist[selected_ad] = 'shown'
        i += 1
    cycles += 1
print 'it took %s cycles' % cycles
