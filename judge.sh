find . -type f -name "*.zip" -execdir unzip -o {} \;
find . -mindepth 1 -type d -exec cp users.json '{}' \;  
find . -mindepth 1 -type d -exec cp actions.log '{}' \;   

find . -type f -name "*.py" -execdir sh -c '                                        
    # Rename each .py file to main.py within its directory
    mv "$1" "$(dirname "$1")/main.py"
' sh {} \;

find . -type f -name 'main.py' -execdir python3.12 {} \;
