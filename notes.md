
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

# Prelim. results

## On correlations between proxies

### Note on translations & editions numbers
So the strong correlation between e.g. Translations and GR_edtions as well as WC_editions might be explained by the fact that these also list translations as editions. So the number of editions is the sum of the number of translations and the number of editions in the original language. (see 'clustermap.png')

### Translations/libraries/opensyllabus
Interestingly, the editions counts, translations and opensyllabus appearances seem to form a cluster (top of the clustermap). So they kind of reflect what we also saw in the bigger corpus, that there is a sort of "canonicity" island here (vs. popularity on the lower part of the clustermap). (see 'clustermap.png')

See also 'libraries_vs_translations/opensyllabus.png' for a scatterplot

### Translations & crowd ratings // Open syllabus & crowd ratings // Libraries & crowd ratings
We see a correlation between translation numbers and crowd rating count (both storygraph & goodreads) but not with average ratings (see 'translations_vs_crowd_ratings.png')

There is the same tendency for Libraries & opensyllabus (as well as GR_EDITIONS and WC_EDITIONS) to correlate more strongly with rating count (goodreads and storygraph) than with average ratings (see 'clustermap.png')

### Expanded clustermap w. prizes
Lots of stuff here, just making some notes of things

The expanded clustermap with prizes shows that the prizes are not too strongly correlated with any of the other proxies (see 'expanded_clustermap.png') - somewhat like in our previous findings - though not entirely as some prizes seem to move across the "two islands" (?)
Some do show small-to-robust correlations: LOCUS_FANTASY, WFA and BFA notably, especially with translations, libraries, opensyllabus, editions, as well as the crowd-based (goodreads and storygraph) (see the "midisland" in 'expanded_clustermap.png') - actually, LOCUS_FANTASY and WFA seem to be clustered with the more "canonic" proxies (like libraries) over being clustered with the other prizes.

Some correlations of WFA, LOCUS_SF, BFA and BRAM_STOKER & DEUTSCHER PHANTASTIK with libraries, and some correlations with the rating and avg rating (storygraph and goodreads), as well as some with GR_EDITIONS and opensyllabus appearances

Strongest intercorrelations of prizes are between LOCUS_SF and BFA, and between BRAM_STOKER and DEUTSCHER PHANTASTIK, and BRAM_STOKER and LOCUS_HORROR (prob. genre-related). Note that negative correlation between LOCUS_SF and LOCUS_HORROR is prob. also because of genre. 

