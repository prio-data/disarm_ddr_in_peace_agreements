from shiny import ui

def about_page_details():

    ui_details = ui.div(ui.page_fluid(

        ui.h2("The DISARM project", class_="country-details-title"),
        ui.div(
            ui.p("Since the 1990s, the international community " 
                 "has invested heavily in disarmament programs, which involve " 
                 "the collection, documentation, and destruction of weapons and " 
                 "ammunition from combatants following the conclusion of civil " 
                 "wars. These programs are typically a component of broader " 
                 "disarmament, demobilization, and reintegration (DDR) efforts " 
                 "and are considered crucial in post-accord countries to promote " 
                 "peace. However, in reality, there is a limited understanding among " 
                 "scholars and policymakers of the distinctions between these " 
                 "programs in terms of their design and impact. The DISARM project " 
                 "addresses this knowledge gap.", class_="custom-paragraph"
                 ),
            ui.p(ui.HTML('To learn more about our research and publications, go to this ' 
                 '<a href="https://www.prio.org/projects/1931" target="_blank" class="custom-link">site</a>.'), class_="custom-paragraph"), 
            ui.p(ui.HTML('Explore the DDR Dataset, the first disaggregated dataset on ' 
                 'DDR provisions in intra-state peace agreements between 1975-2021, ' 
                 'identified by the <a href="https://ucdp.uu.se/downloads/index.html#peaceagreement" target="_blank" class="custom-link">Uppsala Conflict Data Programme</a>.The ' 
                 '(open access) article introducing the data, published in The ' 
                 'Journal of Peace Research, is available here.'), class_="custom-paragraph"),
            ui.p("Meet the team behind the DDR Dataset: Julia "
                 "Palik, Mauricio Rivera Celestine, David Gomez, "
                 "Nicholas Marsh, and Ida Rødningen.", class_="custom-paragraph"),
            ui.p("The DISARM project is hosted by the Peace Research "
                 "Institute Oslo (PRIO) and receives funding from the Norwegian "
                 "Research Council (Grant no. 324997; project leader: Julia Palik).", class_="custom-paragraph")
                    )
        )
        , class_="country-details-container")

    return ui_details 


                        