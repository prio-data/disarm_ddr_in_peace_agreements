from shiny import ui

def contact_page_details():
    ui_details = ui.div(ui.page_fluid(
            ui.p("We are interested in hearing from you. Contact Julia Palik for " 
                 "any questions about the DISARM project."
            , class_="custom-paragraph")
            , ui.p("E-mail: julpal@prio.org", class_="custom-paragraph")
            , class_="country-details-container"))

    return ui_details