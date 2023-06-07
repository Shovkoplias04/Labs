# **Іпс - 12 Шовкопляс Богдан Вікторович **

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TextEditor:
    def __init__(self):
        self.head = None
        self.cursor = None

    def openTextEditor(self, filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
                self.head = Node(content)
                self.cursor = self.head
                print("Text editor opened successfully!")
        except FileNotFoundError:
            self.head = Node('')
            self.cursor = self.head
            print("New file created!")

    def addText(self, text):
        new_node = Node(text)
        if self.head is None:
            self.head = new_node
            self.cursor = new_node
        else:
            new_node.next = self.cursor.next
            self.cursor.next = new_node
            self.cursor = new_node
        print(f"Added text: {text}")

    def deleteText(self, n):
        deleted_count = 0
        current_node = self.cursor
        while current_node.next and deleted_count < n:
            current_node.next = current_node.next.next
            deleted_count += 1
        print(f"Deleted {deleted_count} characters")
        return deleted_count

    def cursorLeft(self, n):
        characters = ''
        for _ in range(n):
            if self.cursor == self.head:
                break
            previous_node = self.head
            while previous_node.next != self.cursor:
                previous_node = previous_node.next
            self.cursor = previous_node
            characters = self.cursor.data[-10:] + characters
        print(f"Cursor moved left {n} times")
        return characters[:10]

    def cursorRight(self, n):
        characters = ''
        for _ in range(n):
            if self.cursor.next:
                self.cursor = self.cursor.next
                characters += self.cursor.data[:10]
        print(f"Cursor moved right {n} times")
        return characters[:10]

    def delete(self):
        self.head = None
        self.cursor = None
        print("File deleted and memory cleared.")


editor = TextEditor()
editor.openTextEditor("example.txt")
editor.addText("Hello,")
editor.addText("world!")
editor.cursorLeft(3)
editor.deleteText(4)
editor.cursorRight(1)
editor.addText("Bohdan Ips-12")
editor.delete()
