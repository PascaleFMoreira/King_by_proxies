# KING colab


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

## On the entropy of ratings (goodreads)
- studies before have found that titles with a high number of ratings also have a more polarised reception (i.e., more 1s and 5s) - which would mean that the distribution would (supposedly) have a higher entropy. We see here though that entropy has a negative correlation to rating count (spearman 0.45, p<0.01) - so in the case of king, the more highly rated books also have a lower entropy, i.e., less disagreement between raters. 

You can see the distribution at: 'rating_entropy_vs_rating_counts.png' --- and have a look at the [interactive figure here](https://pascalefmoreira.github.io/pascalefeldkamp/show_stuff_page_2.html)

0.45 is a robust correlation, so let's make sure this is right before going further. 

We might also want to try out other correlations with entropy, where high entropy might indicate "contested titles", e.g. looking at whether these are less likely to win prizes etc.