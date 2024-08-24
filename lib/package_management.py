import os
from lib.repository import Repository
from lib.dependency import DependencyManager

# The PackageManager class will manage package installation, updating, and removal
class PackageManager:
    
    # Initialization method, loads repositories and dependencies
    def __init__(self):
        self.repository = Repository()
        self.dependency_manager = DependencyManager()

    # Method to install a package
    def install_package(self, package_name):
        try:
            # First, resolve dependencies for the package
            dependencies = self.dependency_manager.resolve_dependencies(package_name)
            for dependency in dependencies:
                print(f"Installing dependency: {dependency}")
                # You could add logic here to actually install dependencies
            with open('installations.log', 'a') as log_file:
                log_file.write(f"{package_name}\n")
            print(f"Installing package: {package_name}")
            # Example logic to install the package
            os.system(f"sudo apt-get install {package_name}")
            print(f"Package '{package_name}' installed successfully.")
            print("Command to view installed packages: ./bin/package_manager show_installation_packages")
        except Exception as e:
            print(f"Error installing package '{package_name}': {str(e)}")
    
    # Function to list registered installations
    def show_installation_packages(self):
        try:
            with open('installations.log', 'r') as log_file:
                installations = log_file.readlines()
                if installations:
                    print("Installed packages:")
                    for package in installations:
                        print(f"- {package.strip()}")
                else:
                    print("No installed packages have been recorded.")
                
        except FileNotFoundError:
            print("No se ha registrado ningún paquete instalado.")

    # Method to update a package
    def update_package(self, package_name):
        print(f"Updating package: {package_name}")
        # Example logic to update the package
        os.system(f"sudo apt-get upgrade {package_name}")

    # Method to remove a package
    def remove_package(self, package_name):
        print(f"Removing package: {package_name}")
        # Example logic to remove the package
        os.system(f"sudo apt-get remove {package_name}")

    # Method to update package repositories
    def update_repositories(self):
        print("Updating repositories...")
        self.repository.update()
