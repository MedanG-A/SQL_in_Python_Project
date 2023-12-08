import loading_species as ls
from loading_species import species_to_txt


ls.iris_df = ls.iris_df.rename(columns={0: 'Species'})
str_of_df = str(ls.iris_df)



species_to_txt("species.txt", str_of_df)

