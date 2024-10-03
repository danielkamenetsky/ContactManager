import os
import secrets

def generate_secret_key():
    """Generate a secure random string for use as a SECRET_KEY."""
    return secrets.token_urlsafe(50)

def generate_database_url(user, password, host, name, port):
    """Generate DATABASE_URL from individual components."""
    return f"postgresql://{user}:{password}@{host}:{port}/{name}"

def generate_env():
    variables = [
        ('DJANGO_SECRET_KEY', 'Enter your DJANGO_SECRET_KEY (press Enter to generate one):'),
        ('DJANGO_DEBUG', 'Enter DJANGO_DEBUG (True/False):'),
        ('DB_USER', 'Enter your DB_USER:'),
        ('DB_PASSWORD', 'Enter your DB_PASSWORD:'),
        ('DB_HOST', 'Enter your DB_HOST (default is localhost):', 'localhost'),
        ('DB_NAME', 'Enter your DB_NAME:'),
        ('DB_PORT', 'Enter your DB_PORT (default is 5432):', '5432'),
    ]

    env_content = """# Django Environment Variables

# To generate a new secret key, you can use the following Python code:
# from django.core.management.utils import get_random_secret_key
# print(get_random_secret_key())
# Or use the Python secrets module:
# import secrets
# print(secrets.token_urlsafe(50))

"""

    db_values = {}

    for var, prompt, *default in variables:
        default_value = default[0] if default else None
        value = input(prompt + ' ') or default_value
        if var == 'DJANGO_SECRET_KEY' and not value:
            value = generate_secret_key()
            print(f"Generated SECRET_KEY: {value}")
        env_content += f'{var}={value}\n'
        if var.startswith('DB_'):
            db_values[var] = value

    # Generate DATABASE_URL
    database_url = generate_database_url(
        db_values['DB_USER'],
        db_values['DB_PASSWORD'],
        db_values['DB_HOST'],
        db_values['DB_NAME'],
        db_values['DB_PORT']
    )
    env_content += f'DATABASE_URL={database_url}\n'

    with open('.env', 'w') as env_file:
        env_file.write(env_content)

    print('.env file generated successfully!')
    print(f"Generated DATABASE_URL: {database_url}")

if __name__ == '__main__':
    generate_env()