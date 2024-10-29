from shiny import ui

def db_codebook_page_details():
    ui_details = ui.div(ui.page_fluid(
            ui.p("On this page, you can download the DDR Dataset (1975-2021) "
                 ", and the codebook."
            , class_="custom-paragraph"),
            ui.div(
            ui.download_button("Excel_file", "disarm_2022-03-11.xlsx", class_= 'country-details-btn'),
            ui.download_button("codebook", "Codebook.pdf", class_= 'country-details-btn')
            , class_="DBandCodebook-button-container")
            , class_="country-details-container"))

    return ui_details
