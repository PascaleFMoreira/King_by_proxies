# %%
from utils import *
from importlib import reload
import utils
reload(utils)

# %%
# Load the data
with open('data/king_books_w_data.json', 'r') as f:
    data = json.load(f)

# Create a DataFrame
df = pd.DataFrame.from_dict(data)
df.head()


# %%
# make some dataframes with selected columns
df_only_proxies = df[['TITLE', 
                      'RATING_COUNT', 'AVG_RATING', 'GR_NO_EDITIONS',
       'WC_EDITIONS', 'WC_LIBRARIES', 
       'STORYGR_RATING_COUNT', 'STORYGR_AVG_RATING', 
       'TRANSLATION_COUNT', 'OPEN_SYLLABUS_APPEARANCES',
       'LOCUS_SF', 'LOCUS_HORROR', 'LOCUS_FANTASY', 'WFA',
       'BFA', 'BRAM_STOKER', 'EDGAR_AWARD', 'DEUTSCHER_PHANTASTIK_PREIS']]

# and one only with the continuous (scaled) variables
df_only_cont = df[['TITLE', 
                      'RATING_COUNT', 'AVG_RATING',
                      'STORYGR_RATING_COUNT', 'STORYGR_AVG_RATING', 
                      'GR_NO_EDITIONS',
       'WC_EDITIONS', 'WC_LIBRARIES', 
       'TRANSLATION_COUNT', 'OPEN_SYLLABUS_APPEARANCES']]
# %%
# PART 1: CORRELATIONS

# Lets make a heatmap to get the correlation between the continuous variables
sns.set_style('whitegrid')
plt.figure(figsize=(7, 4))
filter_df = df_only_cont.drop(columns=['TITLE'])
corr_df = filter_df.corr(method='spearman')
sns.heatmap(corr_df, annot=True, cbar=False)
plt.show()

# Lets make a clustermap of the same
sns.set_style('whitegrid')
filter_df = df_only_cont.drop(columns=['TITLE'])
corr_df = filter_df.corr(method='spearman')
sns.clustermap(corr_df, annot=True, cbar=False, figsize=(12, 12))
plt.show()

# %%
# let's inlude the prizes in the heatmap
# we want to convert letters (W, N) to 1 in all columns
columns_to_replace_prizes = ['LOCUS_SF', 'LOCUS_HORROR', 'LOCUS_FANTASY', 'WFA',
       'BFA', 'BRAM_STOKER', 'EDGAR_AWARD', 'DEUTSCHER_PHANTASTIK_PREIS']
df_transformed = df_only_proxies.copy()
df_transformed[columns_to_replace_prizes] = df_transformed[columns_to_replace_prizes].replace({'W': 1, 'N': 1})
df_transformed[columns_to_replace_prizes] = df_transformed[columns_to_replace_prizes].fillna(0)

# then we can make a clustermap
sns.set_style('whitegrid')
filter_df = df_transformed.drop(columns=['TITLE'])
corr_df = filter_df.corr(method='spearman')
sns.clustermap(corr_df, annot=True, cbar=False, figsize=(12, 12))
plt.show()

# %%
# let's see which won/was nominated for most prizes
# has most ratings
# has highest mean average rating,
# etc.

# Compute the row-wise sum of the prizes columns that we already converted from letters to 1s
df_transformed['sum_prize_wins_noms'] = df_transformed[columns_to_replace_prizes].sum(axis=1)

# Compute the row-wise sum of the ratings columns
rating_cols = ['RATING_COUNT', 'STORYGR_RATING_COUNT']
df_transformed['most_ratings'] = df_transformed[rating_cols].sum(axis=1)

# Compute the row-wise MEAN of the average rating columns
avg_rating_cols = ['AVG_RATING', 'STORYGR_AVG_RATING']
df_transformed['highest_mean_avg_rating'] = df_transformed[avg_rating_cols].mean(axis=1)

# also include the number of translations, libraries and open syllabus appearances
things_to_sort_on = ['sum_prize_wins_noms', 'most_ratings', 'highest_mean_avg_rating', 'OPEN_SYLLABUS_APPEARANCES', 'WC_LIBRARIES', 'TRANSLATION_COUNT']


# we make a loop to get the top10 titles in each of these categories
lst_df_slices = []

for var in things_to_sort_on:
    top_10 = df_transformed.sort_values(var, ascending=False).head(10)
    lst_df_slices.append(top_10[['TITLE', 'WC_LIBRARIES', 'OPEN_SYLLABUS_APPEARANCES', 'TRANSLATION_COUNT', var]].to_string())
    print(top_10[['TITLE', 'WC_LIBRARIES', 'OPEN_SYLLABUS_APPEARANCES', 'TRANSLATION_COUNT', var]])

# Combine the strings
labels = ['Prize wins/noms', 'Most ratings (GoodReads/StoryGraph combined)', 'Highest mean avg rating (GoodReads/StoryGraph combined)', 'Open Syllabus appearances', 'WorldCat libraries', 'Translations']
for i, label in enumerate(labels):
    lst_df_slices[i] = f'\n\nTop 10 books with {label}:\n\n' + lst_df_slices[i]

result_str = '\n\n'.join(lst_df_slices)

# Print the combined result string
print(result_str)

# Save the combined result string to a text file
with open('top_books.txt', 'w') as file:
    file.write(result_str)

# %%
# just a load of scatterplots below
cols = ['RATING_COUNT', 'STORYGR_RATING_COUNT', 'STORYGR_AVG_RATING']
cols2 = ['GR_NO_EDITIONS', 'WC_EDITIONS', 
        'WC_LIBRARIES', 'TRANSLATION_COUNT', 'OPEN_SYLLABUS_APPEARANCES']

sns.set_style('whitegrid')
plot_scatters(df_only_proxies, cols, 'AVG_RATING', 'red', 15, 4, remove_outliers=False, outlier_percentile=100, show_corr_values=True)
plot_scatters(df_only_proxies, cols2, 'AVG_RATING', 'red', 18, 4, remove_outliers=False, outlier_percentile=100, show_corr_values=True)

# %%
cols = ['RATING_COUNT', 'AVG_RATING', 'STORYGR_RATING_COUNT', 'STORYGR_AVG_RATING']
cols2 = ['GR_NO_EDITIONS', 'WC_EDITIONS', 
        'TRANSLATION_COUNT', 'OPEN_SYLLABUS_APPEARANCES']

sns.set_style('whitegrid')
plot_scatters(df_only_proxies, cols, 'WC_LIBRARIES', 'red', 15, 4, remove_outliers=False, outlier_percentile=100, show_corr_values=True)
plot_scatters(df_only_proxies, cols2, 'WC_LIBRARIES', 'red', 18, 4, remove_outliers=False, outlier_percentile=100, show_corr_values=True)

# We could do some more things here, like plotting the correlation between the different prizes and the ratings
# but I think we have enough for now





# %%

# PART 2: RATING DISTRIBUTIONS
# (something i was curious about)

# Let's have a look at rating distributions
print(list(df['GR_RATING_DICT']))

# %%
# we want to make sure we get everything in dictionary form
# Define a function to safely convert string to dictionary
def rating_dist_to_dict(rating_str):
    # Convert the string to a dictionary
    rating_dict = json.loads(rating_str.replace("'", '"'))
    return rating_dict

# then a function to convert the dictionary to a list (so if in the dictionary 5:100, we get a hundred 5s, for example)
def rating_dict_to_list(rating_dict):
    rating_list = []
    for rating, count in rating_dict.items():
        # Create a list of ratings based on the count
        rating_list.extend([int(rating)] * count)
    print(list(set(rating_list)))
    return rating_list

# Apply the function to the DataFrame column (in two steps)
df['RATING_DIST_DICT'] = df['GR_RATING_DICT'].apply(rating_dist_to_dict)
df['RATING_DIST_LIST'] = df['RATING_DIST_DICT'].apply(rating_dict_to_list)
df.head()

# %%
# Function to compute entropy from a list of ratings
# We basically do what Maity et al. (2018) also did: https://arxiv.org/pdf/1809.07354.pdf
# Calculate the entropy of ditributions

# we could also use this function from the nk package, but let's use scipy as below
#df['RATING_DIST_ENTROPY'] = df['RATING_DIST_LIST'].apply(lambda x: nk.entropy_shannon([float(item) for item in x])[0]) # Just get the entropy [0] not the dict

def compute_entropy(rating_list):
    # Calculate the frequency of each rating
    values, counts = np.unique(rating_list, return_counts=True)
    probabilities = counts / counts.sum()
    
    # Compute the entropy
    ent = stats.entropy(probabilities, base=2)  # base 2 for entropy in bits
    return ent

# And to calculate the skew/kurtosis
def check_skew(l):
    s = stats.skew(l)
    return s

def check_kurt(l):
    k = stats.kurtosis(l)
    return k

# apply the functions to the rating distributions
df['RATING_DIST_ENTROPY'] = df['RATING_DIST_LIST'].apply(compute_entropy)
df['RATING_DIST_KURTOSIS'] = df['RATING_DIST_LIST'].apply(check_kurt)
df['RATING_DIST_SKEW'] = df['RATING_DIST_LIST'].apply(check_skew)
df['RATING_DIST_STD'] = df['RATING_DIST_LIST'].apply(lambda x: np.std([float(item) for item in x]))
df.head()


# %%
# # is it possible to get the average rating from the dictionary for each row and does it match with the AVG_RATING?
# df['RATING_FROM_DICT'] = df['RATING_DIST_LIST'].apply(lambda x: np.mean([float(item) for item in x]))
# df['RATING_FROM_DICT']
# yes it does, good.

# %%
# is there a correlation between these features of the rating distribution and the rating count?

# rating count?
cols = ['RATING_DIST_ENTROPY', 'RATING_DIST_KURTOSIS', 'RATING_DIST_SKEW', 'RATING_DIST_STD']
plot_scatters(df, cols, 'RATING_COUNT', 'red', 18, 4, remove_outliers=False, outlier_percentile=100, show_corr_values=True)

# what about AVG_RATING?
plot_scatters(df, cols, 'AVG_RATING', 'red', 18, 4, remove_outliers=False, outlier_percentile=100, show_corr_values=True)
# %%
# lets get an annotated plot with rating on y and entropy on x
cols = ['AVG_RATING', 'RATING_COUNT']
for col in cols:
    plt.figure(figsize=(18, 8))
    sns.scatterplot(data=df, x='RATING_DIST_ENTROPY', y=col, hue='TITLE', palette='rocket', s=100)
    for i in range(len(df)):
        plt.text(df['RATING_DIST_ENTROPY'][i], df[col][i], df['TITLE'][i], fontsize=8)
    plt.legend('')

# %%
# make it interactive
x = plotly_viz_correlation_improved(df, 'RATING_DIST_ENTROPY', 'RATING_COUNT', '', 1000, 500, 'TITLE', color_canon=False, save=True)
#plotly_viz_correlation_improved(df, 'RATING_DIST_ENTROPY', 'AVG_RATING', '', 1000, 500, 'TITLE', color_canon=False, save=False)

# %%
# plot the rating distributions of individual books
# We need to flatten
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

book_ids = ['978-0-752-86433-4', '978-0-385-12168-2', '978-0-670-81302-5', '978-1-78909-649-1','978-0-399-13314-5', '978-0-670-84650-4']

dist_list = []

for id in book_ids:
    title = df['TITLE'].loc[df['ISBN'] == id]
    row = df.loc[df['ISBN'] == id]
    dists = flatten_list(row['RATING_DIST_LIST'])
    dist_list.append(dists)


fig, ax = plt.subplots(1, len(dist_list), figsize=(13, 5), sharey=True)

for i, dist in enumerate(dist_list):
    counts = np.bincount(dist, minlength=6)[1:6]
    
    total_ratings = len(dist)
    percentages = (counts / total_ratings) * 100

    # Extract book title
    title = df['TITLE'].loc[df['ISBN'] == book_ids[i]].values[0]
    rating = df['AVG_RATING'].loc[df['ISBN'] == book_ids[i]].values[0]
    entropy = df['RATING_DIST_ENTROPY'].loc[df['ISBN'] == book_ids[i]].values[0]
    std = df['RATING_DIST_STD'].loc[df['ISBN'] == book_ids[i]].values[0]

    if entropy > 1.7:
        ax[i].bar(np.arange(1, 6), percentages, width=0.7, alpha=0.7, color='lightcoral')
    else:
        ax[i].bar(np.arange(1, 6), percentages, width=0.7, alpha=0.7, color='steelblue')

    # Add annotation
    for p in ax[i].patches:
        ax[i].annotate(format(p.get_height(), '.1f'),
                    (p.get_x() + p.get_width() / 2,
                        p.get_height()), ha='center', va='center',
                    size=12)

    # Set title for each subplot
    ax[i].set_title(f'{title} \n avg. rating: {rating} \n H = {entropy:.2f} / $\\sigma$ = {std:.2f}')

ax[0].set_ylabel('Percentage')

plt.tight_layout()
plt.show()

# %%
# see if the prize-winning books have higher entropy
# Compute the row-wise sum
df_prizes = df.copy()
df_prizes[columns_to_replace_prizes] = df[columns_to_replace_prizes].replace({'W': 1,'N': 1})
df_prizes['prize_wins'] = df_prizes[columns_to_replace_prizes].fillna(0).astype(int).max(axis=1)
wins_df = df_prizes[df_prizes['prize_wins'] == 1]
no_wins_df = df_prizes[df_prizes['prize_wins'] == 0]

measures = ['RATING_DIST_ENTROPY', 'RATING_COUNT', 'AVG_RATING']
histplot_two_groups(no_wins_df, wins_df, measures, measures, ['no_wins/noms', 'wins/noms'], 25, 6, 'comparing groups', density=False, save=False, save_title=False)

print(len(wins_df), len(no_wins_df))

# %%
print("done for now!:)")

# # dump to json and excel
# df.to_excel('data/king_w_data_updated.xlsx')

# df = pd.read_excel('data/king_w_data_updated.xlsx')
# df.head()

# # %%
# df.to_json('data/king_books_w_data.json')
# %%

