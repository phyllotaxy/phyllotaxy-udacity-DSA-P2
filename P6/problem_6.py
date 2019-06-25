# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        # There is no handler for the root of the trie, the root path / home page node
        # is one level higher than the root of the trie. This is to distinguish a real
        # root path '/' from a non-path empty string ''.
        self.insert([''], root_handler)

    def insert(self, path_parts, path_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for path_part in path_parts:
            current_node.insert(path_part)
            current_node = current_node.children[path_part]
        current_node.handler = path_handler

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for path_part in path_parts:
            if path_part not in current_node.children:
                return None
            current_node = current_node.children[path_part]
        return current_node.handler

class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()
        return self.children[path_part]

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.routes.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # Trailing slash handled in split_path() method.
        handler = self.routes.find(self.split_path(path))
        return handler if handler else self.not_found_handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path:
            path_parts = path.split('/')
            # Handle trailing slash
            return path_parts[:-1] if path_parts[-1] == '' else path_parts
        # If the given string is a non-path empty string, return an empty list.
        return []

def main():
    # Here are some test cases and expected outputs you can use to test your implementation
    # create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route
    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
    # edge cases
    print(router.lookup("")) # should print 'not found handler'
    print(router.lookup("a")) # should print 'not found handler'
    print(router.lookup("//")) # should print 'not found handler'

if __name__ == '__main__':
    main()
