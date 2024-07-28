# %%
from utils import *
from importlib import reload
import utils
reload(utils)

# %%
with open('data/king_books_w_data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data)
df.head()

# %%
df.columns
# %%
df_only_proxies = df[['TITLE', 
                      'RATING_COUNT', 'AVG_RATING', 'GR_NO_EDITIONS',
       'WC_EDITIONS', 'WC_LIBRARIES', 
       'STORYGR_RATING_COUNT', 'STORYGR_AVG_RATING', 
       'TRANSLATION_COUNT', 'OPEN_SYLLABUS_APPEARANCES',
       'LOCUS_SF', 'LOCUS_HORROR', 'LOCUS_FANTASY', 'WFA',
       'BFA', 'BRAM_STOKER', 'EDGAR_AWARD', 'DEUTSCHER_PHANTASTIK_PREIS']]
df_only_cont = df[['TITLE', 
                      'RATING_COUNT', 'AVG_RATING',
                      'STORYGR_RATING_COUNT', 'STORYGR_AVG_RATING', 
                      'GR_NO_EDITIONS',
       'WC_EDITIONS', 'WC_LIBRARIES', 
       'TRANSLATION_COUNT', 'OPEN_SYLLABUS_APPEARANCES']]
# %%
# Lets make a heatmap
sns.set_style('whitegrid')
plt.figure(figsize=(7, 4))
filter_df = df_only_cont.drop(columns=['TITLE'])
corr_df = filter_df.corr(method='spearman')
sns.heatmap(corr_df, annot=True, cbar=False)
plt.show()

# Lets make a clustermap
sns.set_style('whitegrid')
filter_df = df_only_cont.drop(columns=['TITLE'])
corr_df = filter_df.corr(method='spearman')
sns.clustermap(corr_df, annot=True, cbar=False, figsize=(9, 9))
plt.show()

# %%
# let's inlude the prizes in the heatmap
# we want to convert letters (W, N) to 1 in all columns
columns_to_replace = ['LOCUS_SF', 'LOCUS_HORROR', 'LOCUS_FANTASY', 'WFA',
       'BFA', 'BRAM_STOKER', 'EDGAR_AWARD', 'DEUTSCHER_PHANTASTIK_PREIS']
df_transformed = df_only_proxies.copy()
df_transformed[columns_to_replace] = df_transformed[columns_to_replace].replace({'W': 1, 'N': 1})
df_transformed[columns_to_replace] = df_transformed[columns_to_replace].fillna(0)

sns.set_style('whitegrid')
filter_df = df_transformed.drop(columns=['TITLE'])
corr_df = filter_df.corr(method='spearman')
sns.clustermap(corr_df, annot=True, cbar=False, figsize=(11, 11))
plt.show()

# %%
# let's see which won/was nominated for most prizes
# has most ratings
# has highest mean average rating

# Compute the row-wise sum
df_transformed['sum_prize_wins_noms'] = df_transformed[columns_to_replace].sum(axis=1)

rating_cols = ['RATING_COUNT', 'STORYGR_RATING_COUNT']
df_transformed['most_ratings'] = df_transformed[rating_cols].sum(axis=1)

avg_rating_cols = ['AVG_RATING', 'STORYGR_AVG_RATING']
df_transformed['highest_mean_avg_rating'] = df_transformed[avg_rating_cols].mean(axis=1)

things_to_sort_on = ['sum_prize_wins_noms', 'most_ratings', 'highest_mean_avg_rating']

lst_df_slices = []

for var in things_to_sort_on:
    top_10 = df_transformed.sort_values(var, ascending=False).head(10)
    lst_df_slices.append(top_10[['TITLE', 'WC_LIBRARIES', 'OPEN_SYLLABUS_APPEARANCES', 'TRANSLATION_COUNT', var]].to_string())
    print(top_10[['TITLE', 'WC_LIBRARIES', 'OPEN_SYLLABUS_APPEARANCES', 'TRANSLATION_COUNT', var]])

# Combine the strings
labels = ['Prize wins/noms', 'Most ratings', 'Highest mean avg rating']
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

# %%

# Let's have a look at rating distributions
print(list(df['GR_RATING_DICT']))

# %%
# we want to make sure we get everything in dictionary form
# Define a function to safely convert string to dictionary
def rating_dist_to_list(rating_str):
    # Convert the string to a dictionary
    rating_dict = json.loads(rating_str.replace("'", '"'))
    
    # Create a list of ratings based on the count
    rating_list = []
    for rating, count in rating_dict.items():
        rating_list.extend([int(rating)] * count)
    
    return rating_list

# Apply the function to the DataFrame column
df['RATING_DIST_LIST'] = df['GR_RATING_DICT'].apply(rating_dist_to_list)

df.head()


# %%
# We basically do what Maity et al. (2018) also did: https://arxiv.org/pdf/1809.07354.pdf
# Calculate the entropy of ditributions
df['RATING_DIST_ENTROPY'] = df['RATING_DIST_LIST'].apply(lambda x: nk.entropy_shannon([float(item) for item in x])[0]) # Just get the entropy [0] not the dict
df.head()
# %%
# is there a correlation between entropy and rating count?

stats.spearmanr(df['RATING_DIST_ENTROPY'], df['RATING_COUNT'])
# yes, so the higher the rating count, the lower the entropy (0.45 correlation)

# %%
# lets get an annotated plot with rating on y and entropy on x
cols = ['AVG_RATING', 'RATING_COUNT']
for col in cols:
    plt.figure(figsize=(15, 8))
    sns.scatterplot(data=df, x='RATING_DIST_ENTROPY', y=col, hue='TITLE', palette='rocket', s=100)
    for i in range(len(df)):
        plt.text(df['RATING_DIST_ENTROPY'][i], df[col][i], df['TITLE'][i], fontsize=8)
    plt.legend('')

# %%
plotly_viz_correlation_improved(df, 'RATING_DIST_ENTROPY', 'RATING_COUNT', '', 1000, 500, 'TITLE', color_canon=False, save=True)

# %%
df.head()
# %%
# dump to json and excel
# df.to_excel('data/king_w_data_updated.xlsx')

# df = pd.read_excel('data/king_w_data_updated.xlsx')
# df.head()
# df.to_json('data/king_books_w_data.json')
# %%
