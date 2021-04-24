Lisa started reviewing the CSRC CSVs to make sure the name.repository value was correct in preparation for reingesting in order to have the repository facet and link work as expected. 

We had added the name.repository field as a facet and as a clickable link in early april 2021 (i think). In order for that new functionality to work, the collections that have that value need to be reindexed (or at least that was a theory at one point during the process of adding this feature to californica/ursus.)

When I clicked on the link in a record for CRSC, I did get a "0 results" search response on ursus (2021-04-23). Assuming that the problem was needing to reindex these collections, I planned to reingest and re-synch californica and ursus. 

However, when I started reviewing the tovar.csv file I notice that about 10 rows looked like cells had been shifted left so that the metadata values were not in the right columns. In trying to correct the error, I decided to compare with a fresh export, and I saw the differences were so great that I had to start from scratch. 

I then did a DLCS export of all the edited items since tovar was first added to the repository and found that Martha Steele had since made edits to this collection on several items. 

I have cleaned up the CSV and I think it is looking good in terms of metadata. Now I am waiting for bucketeer to process the csv.  
