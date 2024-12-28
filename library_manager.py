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
    
    def _removeBookRec(self, p_node, book_id):
        """function to remove a book from the tree."""
        if p_node is None:
            return p_node

        # Traverse to the left or right subtree based on book_id
        if book_id < p_node.book_id:
            p_node.left = self._removeBookRec(p_node.left, book_id)
        elif book_id > p_node.book_id:
            p_node.right = self._removeBookRec(p_node.right, book_id)
        else:
            # Case 1: Node to be deleted has no children (leaf node)
            if p_node.left is None and p_node.right is None:
                return None
            # Case 2: Node to be deleted has one child
            elif p_node.left is None:
                return p_node.right
            elif p_node.right is None:
                return p_node.left
            # Case 3: Node to be deleted has two children
            else:
                # Find the in-order successor (smallest node in the right subtree)
                successor = self._minValueNode(p_node.right)
                # Copy the inorder successor's content to this node
                p_node.book_id = successor.book_id
                p_node.title = successor.title
                p_node.author = successor.author
                p_node.isbn = successor.isbn
                # Delete the in-order successor
                p_node.right = self._removeBookRec(p_node.right, successor.book_id)
        
        return p_node


    def _minValueNode(self, node):
        """function to find the node with the smallest book_id value."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    


