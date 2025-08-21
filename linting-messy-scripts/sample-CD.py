import os


def main():
    """
    Main application function that demonstrates environment-specific deployment.

    When deployed, this function will:
    - Read the ENVIRONMENT variable set by GitHub Actions
    - Print the current environment name to logs
    - Provide clear evidence that deployment succeeded in the correct environment

    Expected log output:
    - Dev environment: "Application is running in: DEV"
    - Test environment: "Application is running in: TEST"
    - Production environment: "Application is running in: PRODUCTION"

    This logging pattern helps verify that:
    1. Environment variables are correctly configured
    2. Deployment reached the intended environment
    3. Application can access environment-specific settings
    """
    environment = os.environ.get("ENVIRONMENT", "unknown")
    print(f"Application is running in: {environment.upper()}")


if __name__ == "__main__":
    main()
