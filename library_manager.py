##### Add your functions here!

class BookNode:
    """The class BookNode will represent each book in the library."""
    def __init__(self, book_id, title, author, isbn):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True # Initially the book is available self.left = None
        self.left = None
        self.right = None

class PatronNode:
    """The class PatronNode will represent each patron."""
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = [] # List of borrowed book IDs self.left = None
        self.right = None
        self.left = None

class LibraryBST:
    """Binary Search Tree Class for Library Manager."""
    def __init__(self):
        self.root = None
    
    def _addBookRec(self, p_node, book_id, title, author, isbn):
        # BASE CASE: When there is no node in the tree
        if p_node is None:
            return BookNode(book_id, title, author, isbn)
        
        # Traverse the tree to find the correct position for the new book
        elif book_id < p_node.book_id:
            # CASE WHEN incoming book id is less than current pointer book id.
            p_node.left = self._addBookRec(p_node.left, book_id, title, author, isbn)            
        elif book_id > p_node.book_id:
            # CASE WHEN incoming book id is greater than current pointer book id.
            p_node.right = self._addBookRec(p_node.right, book_id, title, author, isbn)
        
        else:
            # Update Book with same book id
            p_node.title = title
            p_node.author = author
            p_node.isbn = isbn

        return p_node

