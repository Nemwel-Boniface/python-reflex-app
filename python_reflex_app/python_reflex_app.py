"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import requests

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    message = """Are you a cat lover? Discover fascinating and fun facts about
                our feline friends with Cat Fact Finder. From quirky behaviors to 
                historical tidbits, our app provides a treasure trove of information 
                about cats. Join us today and become a cat facts expert!"""
    cat_facts_url = 'https://cat-fact.herokuapp.com/facts/'
    status_code = 200

    def fetch_cat_facts():
        try:
            response = requests.get(cat_facts_url)
            if not response.status_code:
                print('Error', response.status_code)
                return None
            else:
                cat_facts = response.json()
                return cat_facts
        except requests.exceptions.RequestException as e:
            print('Error', e)
            return None            

    print(fetch_cat_facts())

    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Hello World!", size="9"),
            rx.heading("Welcome to the Cat Facts Application", size="8"),
            rx.text( message,
                size="5",
            ),
            rx.link(
                rx.button("Fetch data…"),
                href="https://cat-fact.herokuapp.com/facts/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.hstack(
            rx.list.ordered(
                rx.list.item(
                    rx.link(
                        rx.button("Project GitHub link"),
                        href="https://github.com/Nemwel-Boniface/python-reflex-app",
                        is_external=True,
                    ),
                ),
                rx.list.item(
                    rx.link(
                        rx.button("Made with love by Nemwel"),
                        href="https://www.linkedin.com/in/nemwel-nyandoro/",
                        is_external=True,
                    ),
                ),
                list_style_type="none",
            ),
            as_child=True,
            justify="end",
            min_height="15vh",
        ),
        rx.logo(),
    )




app = rx.App()
app.add_page(index)
