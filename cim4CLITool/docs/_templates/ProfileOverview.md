# {{ title }}

Profile Name: {{ name }}

{{ description }}

Profiles:

- Abstract Classes
    {% for item in abstractClasses %}
    - [{{ item.name }}]({{ item.path }})
    {% endfor %}

- Concrete Classes
    {% for item in concreteClasses %}
    - [{{ item.name }}]({{ item.path }})
    {% endfor %}

- Enumerations
    {% for item in enumerations %}
    - [{{ item.name }}]({{ item.path }})
    {% endfor %}

- Types
    {% for item in types %}
    - [{{ item.name }}]({{ item.path }})
    {% endfor %}