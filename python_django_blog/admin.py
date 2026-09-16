import os

from django.core.management import execute_from_command_line


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "python_django_blog.settings",
    )
    execute_from_command_line()
