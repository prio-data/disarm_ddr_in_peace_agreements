def WomenChildren_table(agreement, df, country):
 
    df_new = df[(df['pa_name'] == agreement) & (df['ISO3'] == country)][['women', 'children']]
    df_new = df_new.rename(columns={'women': 'Women', 'children': 'Children'})


    return df_new