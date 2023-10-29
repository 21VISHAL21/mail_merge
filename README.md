# mail_merge
This Python script, `main.py`, is a simple invitation letter generator. It reads a list of names from a file, substitutes these names into a template letter, and then saves individual invitation letters for each person. It can be useful for generating personalized invitation letters in bulk.

## Prerequisites

Before using this script, make sure you have Python installed on your system. This script is compatible with Python 3.x.

## Usage

1. Clone or download this repository to your local machine.

2. Create the following directory structure in the project directory to organize your input and output files:

    ```
    ├── Invitation-Letter-Generator
    │   ├── Input
    │   │   ├── Letters
    │   │   │   └── starting_letter.txt
    │   │   └── Names
    │   │       └── invited_names.txt
    │   ├── Output
    │   │   └── ReadyToSend
    ```

3. Place the template invitation letter in `./Input/Letters/starting_letter.txt`. The placeholder `[name]` in the letter will be replaced with the names from `./Input/Names/invited_names.txt`.

4. Add the names of the recipients, one per line, in `./Input/Names/invited_names.txt`.

5. Open your terminal and navigate to the project directory.

6. Run the script by executing the following command:

   ```
   python main.py
   ```

7. The personalized invitation letters will be generated in the `./Output/ReadyToSend` directory with filenames like `letter_for_name.txt`.

## Example

Suppose you have the following input files:

**invited_names.txt:**
```
Alice
Bob
Charlie
```

**starting_letter.txt:**
```
Dear [name],

You are cordially invited to our event on [event_date].

Sincerely,
[Your Name]
```

After running the script, the output will be:

```
./Output/ReadyToSend/letter_for_Alice.txt
./Output/ReadyToSend/letter_for_Bob.txt
./Output/ReadyToSend/letter_for_Charlie.txt
```

## Customization

You can customize the template letter and file paths in the `main.py` script to match your specific requirements.



Feel free to use and modify it as needed for your projects. If you find any issues or have suggestions for improvement, please open an issue or create a pull request on this GitHub repository.

Happy letter generation! 💌
