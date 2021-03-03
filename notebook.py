"""Module for storing, modifying and searching for notes."""
import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    '''
    Represent a note in the notebook. Match against a
    string in searches and store tags for each note.
    '''

    def __init__(self, memo, tags=''):
        '''
        Initialize a note with memo and optional
        space-separated tags. Automatically set
        the note's creation date and a unique id.

        >>> note1 = Note('some note')
        >>> note1.memo
        'some note'
        >>> note1.tags
        ''
        >>> note1.id
        1
        >>> note2 = Note('other note')
        >>> note2.id
        2
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter_str):
        '''
        Determine if this note matches the filter
        text. Search is case sensitive and matches
        both text and tags.

        >>> note1 = Note('some note', ['studying', 'coding'])
        >>> note1.match('coding')
        True
        >>> note1.match('note')
        True
        >>> note1.match('something')
        False
        '''
        return filter_str in self.memo or filter_str in self.tags


class Notebook:
    '''
    Represent a collection of notes that can be tagged,
    modified, and searched for by certain parameters.
    '''

    def __init__(self):
        '''
        Initialize an empty notebook.

        >>> notebook = Notebook()
        >>> notebook.notes
        []
        '''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list.

        >>> notebook = Notebook()
        >>> notebook.new_note('hello world')
        >>> notebook.new_note('hello again')
        >>> len(notebook.notes)
        2
        >>> notebook.notes[1].memo
        'hello again'
        '''
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its
        memo to the given value.

        >>> notebook = Notebook()
        >>> notebook.new_note('hello world')
        >>> note_id = notebook.notes[0].id
        >>> notebook.modify_memo(note_id, 'new memo')
        >>> notebook._find_note(note_id).memo
        'new memo'
        '''
        note = self._find_note(note_id)

        if note:
            note.memo = memo

    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given id and change its
        tags to the given value.

        >>> notebook = Notebook()
        >>> notebook.new_note('hello world')
        >>> note_id = notebook.notes[0].id
        >>> notebook.modify_tags(note_id, 'new tags')
        >>> notebook._find_note(note_id).tags
        'new tags'
        '''
        note = self._find_note(note_id)

        if note:
            note.tags = tags

    def search(self, filter_str):
        '''
        Find all notes that match the given filter string.

        >>> notebook = Notebook()
        >>> notebook.new_note('hello world')
        >>> notebook.new_note('hello again', 'mytag')
        >>> notebook.new_note('ah', 'mytag')
        >>> len(notebook.search('hello'))
        2
        >>> len(notebook.search('mytag'))
        2
        '''
        return [note for note in self.notes if
                note.match(filter_str)]

    def _find_note(self, note_id):
        '''
        Locate the note with the given id.

        >>> notebook = Notebook()
        >>> notebook.new_note('hello world')
        >>> notebook.new_note('hello again', 'mytag')
        >>> notebook.new_note('ah', 'mytag')
        >>> notebook._find_note(5).memo
        'hello again'
        '''
        for note in self.notes:
            if note.id == note_id:
                return note

        return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
