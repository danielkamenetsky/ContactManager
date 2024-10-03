import os
import secrets

def generate_secret_key():
    """Generate a secure random string for use as a SECRET_KEY."""
    return secrets.token_urlsafe(50)

def generate_env():
    variables = [
        ('DJANGO_SECRET_KEY', 'Enter your DJANGO_SECRET_KEY (press Enter to generate one):'),
        ('DJANGO_DEBUG', 'Enter DJANGO_DEBUG (True/False):'),
        ('DB_USER', 'Enter your DB_USER:'),
        ('DB_PASSWORD', 'Enter your DB_PASSWORD:'),
        ('DB_HOST', 'Enter your DB_HOST:'),
        ('DB_NAME', 'Enter your DB_NAME:'),
        ('DB_PORT', 'Enter your DB_PORT (default is 5432):'),
    ]

    env_content = """# Django Environment Variables

# To generate a new secret key, you can use the following Python code:
# from django.core.management.utils import get_random_secret_key
# print(get_random_secret_key())
# Or use the Python secrets module:
# import secrets
# print(secrets.token_urlsafe(50))

"""

    for var, prompt in variables:
        value = input(prompt + ' ')
        if var == 'DJANGO_SECRET_KEY' and not value:
            value = generate_secret_key()
            print(f"Generated SECRET_KEY: {value}")
        env_content += f'{var}={value}\n'

    with open('.env', 'w') as env_file:
        env_file.write(env_content)

    print('.env file generated successfully!')

if __name__ == '__main__':
    generate_env()