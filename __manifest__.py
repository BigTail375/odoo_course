{
    'name': 'Course Management',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Module to manage courses',
    'description': """
        This module allows the management of courses, including fields like 
        name, description, duration, instructors, and price.
    """,
    'author': 'Yurii Smoliar',
    'depends': ['base'],
    'data': [
        'views/course_views.xml',  # This is where you'll define the views
        'security/ir.model.access.csv',  # Access control for the model
    ],
    'installable': True,
    'application': True,
}
