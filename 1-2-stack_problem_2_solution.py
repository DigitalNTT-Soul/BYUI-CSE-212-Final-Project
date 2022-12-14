class Stack:
    def __init__(self):
        self.__data = []
    
    def push(self, value):
        self.__data.append(value)
    
    def pop(self):
        return self.__data.pop()
    
    def size(self):
        return len(self.__data)

    def empty(self):
        return not self.size()

class FileBrowser:
    def __init__(self):
        self.__current_address = 'C:/'
        self.__previous_addresses = Stack()
    
    def __open_folder(self, full_path_to_folder):
        # the function that actually moves you into the provided folder
        self.__current_address = full_path_to_folder
        print("Arriving at " + full_path_to_folder)

    def click_folder(self, child_folder_name):
        self.__previous_addresses.push(self.__current_address)
        full_path = self.__current_address + child_folder_name + '/'
        print("Clicking to " + full_path)
        self.__open_folder(full_path)

    def go_back(self):
        old_address = self.__previous_addresses.pop()
        print("Returning to " + old_address)
        self.__open_folder(old_address)

file_browser = FileBrowser()
file_browser.click_folder("Program Files")
file_browser.click_folder("Google Chrome")
file_browser.go_back()
file_browser.go_back()
file_browser.click_folder("users")
file_browser.click_folder("admin")
file_browser.click_folder("Documents")
file_browser.go_back()
file_browser.click_folder("Downloads")
file_browser.go_back()
file_browser.go_back()
file_browser.go_back()