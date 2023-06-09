
class Queue:
    def __init__(self, elements):
        self.elements = elements

    def show(self):
        print(self.elements)

    def check_if_empty(self):
        if len(self.elements) == 0:
            print("lista jest pusta")
        else:
            print("lista nie jest pusta")

    def put_element(self, new):
        self.elements.append(new)

    def get_element(self):
        self.elements.pop(0)


shop_queue = Queue(["adam", "ewa", "janek", "seba"])
empty_queue = Queue([])

shop_queue.show()
empty_queue.show()
empty_queue.check_if_empty()
shop_queue.check_if_empty()
empty_queue.put_element("janina")
empty_queue.put_element("ewa")
empty_queue.put_element("roman")
empty_queue.show()
empty_queue.get_element()
empty_queue.show()



