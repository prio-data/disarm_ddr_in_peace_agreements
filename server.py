from shiny import ui, render, reactive
from legend import create_legend
from world_map import create_map
from country_details_ui import country_details
from agreement_details_ui import agreement_details
from Tables.DDR_table import agreement_table
from Tables.Women_Children_table import WomenChildren_table
from Tables.Third_Party_table import ThirdParty_table
from data.data_cleaning import new_df_disarm 
from data.http_to_hhtps import replace_http
from data.mapping import mapping
from data.polygon_data import data_json
from about_ui import about_page_details
from contact_ui import contact_page_details
from dataset_codebook_ui import db_codebook_page_details
from shinywidgets import output_widget, render_widget 
from pathlib import Path


########################################
##### Server function 

def server(input, output, session):

    page = reactive.Value("map")
    selected_country = reactive.Value(None)
    selected_agreement = reactive.Value(None)

    # Reactive value to track which tab is active
    active_tab = reactive.Value(None) 


    # Switch to map page when clicking the map button
    @reactive.Effect
    @reactive.event(input.show_map_page)
    def show_map_page():
        page.set("map")



    # @reactive.Effect
    # @reactive.event(input.page)
    # def update_map_ui():
    #     if input.page() == "Map":
    #         active_tab.set("map_ui")

    # Switch to country_details page from map page
    @reactive.Effect
    def update_to_country_details_page():
        if selected_country.get():
            page.set("country_details")


    # switch to agreement details page
    @reactive.Effect
    def update_to_agreemnet_details_page():
        country = selected_country.get()

        if country: 
            pa_name = new_df_disarm[new_df_disarm['ISO3']==country]['pa_name']
            for d in range(len(pa_name)):
                button_id = f"{d}"
                if input[button_id]():  # Detects if this button was clicked
                    selected_agreement.set(pa_name.iloc[d])
                    page.set("agreement_details")

    # switch to country details page from the agreement page
    @reactive.Effect
    @reactive.event(input.show_country_details_page)
    def show_country_details_from_agreement_page():
        page.set("country_details")

    
    # Go to page to download the entire text for the peace agreement
    @reactive.Effect
    @reactive.event(input.Download_entire_agreement)
    async def test_message():
        # print("Download button clicked!")
        agreement = selected_agreement.get()
        country = selected_country.get()
        # print(agreement)
        download = new_df_disarm[(new_df_disarm['ISO3']==country) & (new_df_disarm['pa_name']==agreement)]['linktofulltextagreement']
        download = download.apply(replace_http)
        # print(download)
        download_link = download.iloc[0]
        await session.send_custom_message('test_message', f"{download_link}")

    
    # # Going back to map page when clicking on Data tab
    # @reactive.Effect
    # @reactive.event(input.tab)  
    # def handle_tab_change():
    #     if input.tab() == "Data": 
    #         print("Data tab selected, displaying map.")
    #         session.send_input_message("map_ui", "")
    #         # ui.update_ui("map_ui")



    


    # @render.download(
    #     filename=lambda: f"新型-{date.today().isoformat()}-{random.randint(100, 999)}.csv"
    # )
    # async def downloadData():
    #     await asyncio.sleep(0.25)
    #     yield "one,two,three\n"
    #     yield "新,1,2\n"
    #     yield "型,4,5\n"
        
    ##########################################
    ### Agreement details ui

    @output
    # @render.data_frame
    @render.ui
    def agreement_details_ui():
        df = new_df_disarm
        if page.get() == "agreement_details":
            agreement = selected_agreement.get()
            return agreement_details(agreement, df)

    #########################################
    ### DDR table

    @output
    @render.data_frame
    def DDRtable():
        agreement = selected_agreement.get()
        df = new_df_disarm
        country = selected_country.get()
        return agreement_table(agreement, df, country)
    
    #########################################
    ### Women/Children table

    @output
    @render.data_frame
    def WoChtable():
        agreement = selected_agreement.get()
        df = new_df_disarm
        country = selected_country.get()
        return WomenChildren_table(agreement, df, country)
    
    #########################################
    ### Women/Children table

    @output
    @render.data_frame
    def ThiPartable():
        agreement = selected_agreement.get()
        df = new_df_disarm
        country = selected_country.get()
        return ThirdParty_table(agreement, df, country)

    
    ##########################################
    ### Country details ui

    @output
    @render.ui
    def country_details_ui():
        if page.get() == "country_details":
            country = selected_country.get()
            df = new_df_disarm
            pa_count = mapping[country]
            return country_details(country, df, pa_count)

       
    ##########################################
    ### Map function 

    @output
    @render_widget
    def map():
        polygon_data = data_json
        mapping_data = mapping
        map = create_map(selected_country, polygon_data, mapping_data, country_text)
        return map
        # return create_map()

    ##########################################
    ### Map ui

    @output
    @render.ui
    def map_ui():
        if page.get() == "map":
            return ui.page_fluid(
                output_widget("map"), 
                ui.div(ui.HTML(create_legend(mapping)), class_="legend"), 
                ui.div(
                    ui.output_text("country_tooltip"),
                    class_="custom-tooltip") 
            )
        
    # Switch to map page when clicking on the Main tap
    @reactive.Effect
    @reactive.event(input.tab_clicked)
    def update_map_ui_from_tab():
        # print(f"Tab clicked: {input.tab_clicked()}")
        # print(f"Active tab before update: {active_tab.get()}")
        if input.tab_clicked() == "map_ui_tab":
            # active_tab.set("map_ui_tab") 
            # print(page.get())
            page.set("map")


    #### Tooltips ####
    # country_text = reactive.Value("Hover over a country")
    country_text = reactive.Value("")

    @output
    @render.text
    def country_tooltip():
        return country_text.get()
    

    ### About Page ###
    @output
    @render.text
    def about_page_ui():
        return about_page_details()
    
    ### Contact Page ###
    @output
    @render.text
    def contact_page_ui():
        return contact_page_details()
    

    ### db & codebook Page ###
    @output
    @render.text
    def database_codebook_page_ui():
        return db_codebook_page_details()
    
    ## codebook download button
    @render.download(filename="Codebook DDR dataset Sept2024.pdf")
    def codebook():
        codebook_path = Path(__file__).parent / "data" / "Codebook DDR dataset Sept2024.pdf"

        return str(codebook_path)
    
    ## Excel download button
    @render.download(filename="disarm_2022-03-11.xlsx")
    def Excel_file():
        Excel_path = Path(__file__).parent / "data" / "disarm_2022-03-11.xlsx"

        return str(Excel_path)
    




    
    
    

    