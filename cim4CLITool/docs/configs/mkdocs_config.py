from datetime import datetime

# Get the current year
current_year = datetime.now().year

class MkDocsConfig:

    def elbits(profiles=[]):

        config = {
            'site_name': 'CIM for Norway',
            'theme_name': 'material',
            'theme_favicon': 'images/cim4nologo.svg',
            'theme_logo': 'images/cim4nologo.svg',
            'feature_navigation_tabs': True,
            'feature_navigation_expand': False,
            'feature_navigation_sections': True,
            'feature_navigation_top': True,
            'feature_navigation_integrate': False,
            'feature_navigation_footer': False,
            'feature_search_suggest': True,
            'feature_search_highlight': True,
            'feature_content_tabs_link': True,
            'feature_content_code_annotation': True,
            'feature_content_code_copy': True,
            'language': 'en',
            'light_mode_color_primary': 'black',
            'light_mode_color_accent': 'red',
            'dark_mode_color_primary': 'black',
            'dark_mode_color_accent': 'green',
            'mermaid': True,
            'nav': True,
            'profiles': profiles
        }

        return config
    
    def default(profiles=[]):

        config = {
            'site_name': 'This is my site',
            'theme_name': 'material',
            'theme_favicon': 'images/my_logo.svg',
            'theme_logo': 'images/my_logo.svg',
            'feature_navigation_tabs': True,
            'feature_navigation_expand': False,
            'feature_navigation_sections': True,
            'feature_navigation_top': True,
            'feature_navigation_integrate': False,
            'feature_navigation_footer': False,
            'feature_search_suggest': True,
            'feature_search_highlight': True,
            'feature_content_tabs_link': True,
            'feature_content_code_annotation': True,
            'feature_content_code_copy': True,
            'language': 'en',
            'light_mode_color_primary': 'black',
            'light_mode_color_accent': 'red',
            'dark_mode_color_primary': 'black',
            'dark_mode_color_accent': 'green',
            'social_links': [
                {'icon': 'fontawesome/brands/github', 'link': 'https://github.com/mygithub'}
            ],
            'mermaid': True,
            'nav': False,
            'profiles': profiles,
        }

        return config