from shiny import ui
from pathlib import Path

css_file = Path(__file__).parent / "css" / "styles.css"
js_file = Path(__file__).parent / "www" / "download_page.js"


app_ui = ui.page_fluid(
    # ui.head_content(ui.include_css("styles.css")), 
    ui.include_css(css_file),
    # ui.head_content(ui.include_js("www/download_page.js")),
    ui.include_js(js_file),
            ui.div(
                # ui.navset_pill( 
                ui.navset_bar( #ui.page_navbar 
                    ui.nav_spacer(),
                    ui.nav_panel("Main",
                        ui.output_ui("map_ui"),     
                        ui.output_ui("country_details_ui"), 
                        ui.output_ui("agreement_details_ui"),
                        value="map_ui_tab"
                    ),          
                    ui.nav_panel("About",
                        ui.output_ui("about_page_ui")
                    ),
                    ui.nav_panel("Dataset and Codebook",
                                 ui.output_ui("database_codebook_page_ui"),
                    ),
                    ui.nav_panel("Contact", 
                                 ui.output_ui("contact_page_ui")
                    ),
                    title=ui.h2("DISARM: Introducing the DDR Dataset (1975-2021)", class_="app-title"),
                    id="tab"
                ),
                class_="custom-nav-tabs",
            )
)