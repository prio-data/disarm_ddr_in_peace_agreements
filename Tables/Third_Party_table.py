def ThirdParty_table(agreement, df, country):
 
    df_new = df[(df['pa_name'] == agreement) & (df['ISO3'] == country)][['3rd_party']]
    df_new = df_new.rename(columns={'3rd_party': 'Third-party'})


    return df_new