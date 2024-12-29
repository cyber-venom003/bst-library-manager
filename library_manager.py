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

    
    def _borrowBook(self, p_node, book_id, patron_id):
        # Base case: when the tree is empty
        if p_node is None:
            return "Book not found."

        # Traverse the tree to find the book with the given book_id
        if book_id < p_node.book_id:
            return self._borrowBook(p_node.left, book_id, patron_id)
        elif book_id > p_node.book_id:
            return self._borrowBook(p_node.right, book_id, patron_id)
        else:
            # Case when the book_id matches the current node's book_id
            if len(p_node.borrowed_books) > 0:
                return "Book is already borrowed."
            else:
                p_node.borrowed_books.append(patron_id)
                return "Book borrowed successfully."

    def _returnBook(self, p_node, book_id, patron_id):
        # Base case: when the tree is empty
        if p_node is None:
            return "Book not found."

        # Traverse the tree to find the book with the given book_id
        if book_id < p_node.book_id:
            return self._returnBook(p_node.left, book_id, patron_id)
        elif book_id > p_node.book_id:
            return self._returnBook(p_node.right, book_id, patron_id)
        else:
            # Case when the book_id matches the current node's book_id
            if patron_id in p_node.borrowed_books:
                p_node.borrowed_books.remove(patron_id)
                return "Book returned successfully."
            else:
                return "This patron did not borrow the book."
    
    def _searchBook(self, pNode, bookId):
        # Base case: when the tree is empty
        if pNode is None:
            return "Book not found."

        # Traverse the tree to find the book with the given bookId
        if bookId < pNode.book_id:
            return self._searchBook(pNode.left, bookId)
        elif bookId > pNode.book_id:
            return self._searchBook(pNode.right, bookId)
        else:
            # Case when the bookId matches the current node's bookId
            if len(pNode.borrowed_books) > 0:
                availability = "Not available"
            else:
                availability = "Available"
            return f"Title: {pNode.title}\nAuthor: {pNode.author}\nISBN: {pNode.isbn}\nAvailability: {availability}"

    def _listAvailableBooks(self, pNode):
        available_books = []
        if pNode:
            if pNode.available:
                available_books.append(f"Book ID {pNode.bookId}: \"{pNode.title}\" by {pNode.author}")
            return self._listAvailableBooks(pNode.left)
            return self._listAvailableBooks(pNode.right)

        if available_books:
            return "Available Books:\n" + "\n".join(available_books)
        return "No available books."

    def _listBooksByAuthor(self, pNode, authorName):
        books_by_author = []
        if pNode:
            if pNode.author == authorName:
                books_by_author.append(f"Book ID {pNode.bookId}: \"{pNode.title}\" by {pNode.author}")
            return self._listBooksByAuthor(pNode.left, authorName)
            return self._listBooksByAuthor(pNode.right, authorName)

        if books_by_author:
            return f"Books by Author \"{authorName}\":\n" + "\n".join(books_by_author)
        return f"No books found by {authorName}."