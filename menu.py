'''Module for running a console programme to store, modify and search for notes.'''
import sys
from notebook import Notebook


class Menu:
    '''
    Display a menu and respond to choices when run.
    '''

    def __init__(self):
        '''
        Initialize a menu with an empty notebook and available choices.
        '''
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        '''
        Display the menu.
        '''
        print('''
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit''')

    def run(self):
        '''
        Display the menu and respond to choices.
        '''
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print('{0} is not a valid choice'.format(choice))

    def show_notes(self, notes=None):
        '''
        Show all notes in a formatted way.
        '''
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print(f'{note.id}: {note.tags}\n{note.memo}')

    def search_notes(self):
        '''
        Search for notes by filter query.
        '''
        filter_str = input('Search for: ')
        notes = self.notebook.search(filter_str)
        self.show_notes(notes)

    def add_note(self):
        '''
        Add a note to the notebook.
        '''
        memo = input('Enter a memo: ')
        self.notebook.new_note(memo)
        print('Your note has been added.')

    def modify_note(self):
        '''
        Modify note by id if it exists.
        '''
        note_id = input('Enter a note id: ')
        memo = input('Enter a memo: ')
        tags = input('Enter tags: ')

        if memo:
            self.notebook.modify_memo(note_id, memo)

        if tags:
            self.notebook.modify_tags(note_id, tags)

    def quit(self):
        '''
        Stop the script.
        '''
        print('Thank you for using your notebook today.')
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
