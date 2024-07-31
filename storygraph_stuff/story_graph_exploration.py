# %%
# %%
with open('data/king_books_w_data.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data)
df.head()

# %%
[x for x in df.columns if 'STORYGR' in x]
# %%
df['STORYGR_LOVABLE_CHARACTERS']
# %%
import ast

def process_entry(entry):
    if isinstance(entry, str):
        try:
            # Convert the string representation of the list to an actual list
            entry = ast.literal_eval(entry)
        except (ValueError, SyntaxError):
            # Handle the error by returning an empty list or any default value
            return []
    if isinstance(entry, list):
        try:
            # Convert the percentage strings to float values
            return [(desc, float(perc.strip('%'))) for desc, perc in entry]
        except (ValueError, TypeError):
            # Handle any conversion errors
            return []
    return []

# Apply the function to the data column
df['STORYGR_LOVABLE_CHARACTERS'] = df['STORYGR_LOVABLE_CHARACTERS'].apply(process_entry)
df['STORYGR_LOVABLE_CHARACTERS'].head()
# %%

# Function to expand processed ratings into separate columns
def expand_processed_ratings(processed_ratings):
    return pd.Series(dict(processed_ratings))

# Expand the processed ratings
df['STORYGR_LOVABLE_CHARACTERS'] = df['STORYGR_LOVABLE_CHARACTERS'].apply(expand_processed_ratings)

df['STORYGR_LOVABLE_CHARACTERS']
# %%
