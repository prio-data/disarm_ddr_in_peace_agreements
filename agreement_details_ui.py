from shiny import ui




def agreement_details(agreement, df):

    #df = new_df_disarm
    pa_3rd = df[df['pa_name'] == agreement]['pa_3rd'].iloc[0]
    # table = agreement_table(agreement, df)

    ui_details = ui.div(ui.page_fluid(
        ui.div(
            ui.input_action_button("show_country_details_page", "Agreement page", class_= 'country-details-btn'),
            ui.div(ui.input_action_button("Download_entire_agreement", "", class_= "Download_btn"))
        , class_="header-container"),

        ui.h2(f'DDR components in agreement"{agreement}"', class_="agreement-details-title"),
        ui.div(ui.output_data_frame("DDRtable"), class_="table"),

        ui.h2("Reference to women and children ex-combatants in DDR provisions", class_="agreement-details-title"),
        ui.div(ui.output_data_frame("WoChtable"), class_="table"),

        ui.h2("Third-party involvement in DDR provision implementation", class_="agreement-details-title"),
        ui.div(ui.output_data_frame("ThiPartable"), class_="table")

        ), class_="country-details-container")

    return ui_details 