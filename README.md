# KING colab

# Prelim. results

## Awards wins/nominations
Note that the majority of king's books have won or have been nominated for an award
38 books were nominated for at least 1 award 
4 books won at least 1 award
(of the awards we consider, there may be more)

23 books have not won/been nominated for any award


## On correlations between proxies

### Note on translations & editions numbers
So the strong correlation between e.g. Translations and GR_edtions as well as WC_editions might be explained by the fact that these also list translations as editions. So the number of editions is the sum of the number of translations and the number of editions in the original language. (see 'clustermap.png')

<img src="https://github.com/PascaleFMoreira/King_by_proxies/raw/main/figures/clustermap.png" width="50%" align="right" />


### Translations/libraries/opensyllabus
Interestingly, the editions counts, translations and opensyllabus appearances seem to form a cluster (top of the clustermap). So they kind of reflect what we also saw in the bigger corpus, that there is a sort of "canonicity" island here (vs. popularity on the lower part of the clustermap). (see 'clustermap.png')

See also 'libraries_vs_translations/opensyllabus.png' for a scatterplot

<img src="https://github.com/PascaleFMoreira/King_by_proxies/raw/main/figures/libraries_vs_transalations%3Aopensyllabus.png" width="100%" align="right" />



### Translations & crowd ratings // Open syllabus & crowd ratings // Libraries & crowd ratings
We see a correlation between translation numbers and crowd rating count (both storygraph & goodreads) but not with average ratings (see 'translations_vs_crowd_ratings.png')

There is the same tendency for Libraries & opensyllabus (as well as GR_EDITIONS and WC_EDITIONS) to correlate more strongly with rating count (goodreads and storygraph) than with average ratings (see 'clustermap.png')


### Expanded clustermap w. prizes
Lots of stuff here, just making some notes of things

The expanded clustermap with prizes shows that the prizes are not too strongly correlated with any of the other proxies (see 'expanded_clustermap.png') - somewhat like in our previous findings - though not entirely as some prizes seem to move across the "two islands" (?)
Some do show small-to-robust correlations: LOCUS_FANTASY, WFA and BFA notably, especially with translations, libraries, opensyllabus, editions, as well as the crowd-based (goodreads and storygraph) (see the "midisland" in 'expanded_clustermap.png') - actually, LOCUS_FANTASY and WFA seem to be clustered with the more "canonic" proxies (like libraries) over being clustered with the other prizes.

Some correlations of WFA, LOCUS_SF, BFA and BRAM_STOKER & DEUTSCHER PHANTASTIK with libraries, and some correlations with the rating and avg rating (storygraph and goodreads), as well as some with GR_EDITIONS and opensyllabus appearances

Strongest intercorrelations of prizes are between LOCUS_SF and BFA, and between BRAM_STOKER and DEUTSCHER PHANTASTIK, and BRAM_STOKER and LOCUS_HORROR (prob. genre-related). Note that negative correlation between LOCUS_SF and LOCUS_HORROR is prob. also because of genre. 

<img src="https://github.com/PascaleFMoreira/King_by_proxies/raw/main/figures/expanded_clustermap.png" width="100%" align="right" />

## On the entropy of ratings (goodreads)
- e.g. [Kovacs & Shakey (2014)](https://doi.org/10.1177/0001839214523602) have found that titles that win awards will get a lower GoodReads average score after the award because they get a more polarised reception (i.e., more 1s and 5s) – i.e., their rating distribution becomes more entropic. We can use entropy on the rating distributions to see if there is a polarised rating behaviour is the case for King's books. (also using *entropy* on rating distributions: Maity et al. 2018: [https://arxiv.org/pdf/1809.07354](https://arxiv.org/pdf/1809.07354)) 

We see here though that entropy has a negative correlation to rating count (spearman 0.45, p<0.01) - so in the case of king, the more highly rated books also have a lower entropy, i.e., less disagreement between raters. 0.45 is a robust correlation, and it does not seem to be as strong when looking at a larger corpus of books on GoodReads (did some cross-checking, where we see a correlation between entrpy/rating count at 0.22).

<img src="https://github.com/PascaleFMoreira/King_by_proxies/raw/main/figures/rating_entropy_vs_rating_count.png" width="70%" align="right" />
See the scatterplot of rating count/entropy above (also in figures: 'rating_entropy_vs_rating_counts.png') --- and have a look at the [interactive figure here](https://pascalefmoreira.github.io/pascalefeldkamp/show_stuff_page_2.html)

A few examples of the distributions of books with very high and very low entropy of their rating distributions:
<img src=!https://github.com/PascaleFMoreira/King_by_proxies/raw/main/figures/some_books.png" width="100%" align="right>

## We could do some more on comparing prizes/no prizes groups
I just did a little comparison with the GoodReads data (but could also be checked for translations, libraries, etc., trying to gauge the "importance" of the prize-winning books in terms of other proxies)
See e.g.:
<img src=!https://github.com/PascaleFMoreira/King_by_proxies/raw/main/figures/wins_noms_compared.png" width="100%" align="right>