### Sample 1 for Fester: Sinai manuscripts model

For paginated collections migrated from DLCS, there may be one CSV that contains all **Work** and **ChildWork** rows for one or more given items.
* `collection.csv` (this csv includes at least one Work row and all ChildWork rows for each paginated object)

*See the CSV example in this folder.*

OR

If a collection is large it may be broken into multiple CSVs for processing. In this case, the first in the series will likely also have a **Collection** row)
* `collection_batch1.csv`
* `collection_batch2.csv`

A real example: https://github.com/UCLALibrary/eureka/tree/master/metadata_reload/ethiopian_mss
