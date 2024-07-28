
# Data

## The proxies

### Storygraph
all storygraph features begin with "STORYGR_xxx"
- STORYGR_RATING_COUNT
- STORYGR_AVG_RATING
- other features (e.g. pace, mood, flaws etc)

### Goodreads
- GR_EDITIONS (how many editions of a book were listed on goodreads)
- GR_RATING_COUNT (number of ratings)
- GR_AVG_RATING (avg rating)
- GR_RATING_DICT (rating distribution, i.e., how many ratings in each star (2,3,4) ect)

### Libraries
- WC_EDITIONS (how many editions of a book were listed on worldcat)
- WC_LIBRARIES (number libraries worldwide holding the book)
- WC_GENRE (note: i just noted this down while I a was at it, but these genre tags seem unreliable)

### Translations
- TRANSLATION_COUNT (how many translations of a book exist as listed in index translationum)
Note: the index stops listing books after 2006 - why all of our books after 2006 have 0 translations. A bit of a problem

### Open syllabus
- OPEN_SYLLABUS_APPEARANCES (how many times a book appears in syllabi of English Literature)

### Awards wins/nominatons
- LOCUS_SF (Locus Science Fiction Award)
- LOCUS_FANTASY (Locus Fantasy Award)
- LOCUS_HORROR (Locus Horror Award)
- WFA (World Fantasy Award)
- BFA (British Fantasy Award)
- BRAM_STOKER (Bram Stoker Award)
- DEUTSCHER_PHANTASTIK (Deutscher Phantastik Preis)
- EDGAR_AWARD (Edgar Award)

I had some more ideas here, like HUGO and NEBULA, as well as the National Book Award or Pulitzer but King doesnt seem to have won/been nominated (beyond lifetime award, e.g. for the National Book Award).

for all awards, I have put N for nomination and W for win - but we might just want to work with longlisted (so transforming both of instances to 1)

### ID rows
I just saved ids and links for the different pages so it's easy to reload scores (for example get the goodreads scores again in 1-2 years if we'd want to)
