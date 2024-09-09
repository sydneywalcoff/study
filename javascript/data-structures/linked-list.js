const ListNode = function(val) {
    this.val = val;
    this.next = null;
}

const LinkedList = function() {
    this.head = null;
    this.tail = null;
    this.length = 0;
};

LinkedList.prototype.addAtHead = function(val) {
    const node = new ListNode(val);
    const list = this;
    let placeholder;
    if(!list.head) {
        list.head = node;
    } else {
        placeholder = list.head;
        list.head = node;
        list.head.next = placeholder;
    }
    list.length++;
}

LinkedList.prototype.addAtTail = function(val) {
    const node = new ListNode(val);
    const list = this;
    if(!list.head) {
        list.head = node;
        list.tail = node;
    } else {
        list.tail = node;
        list.head.next = node;
    }
    list.length++;
}

LinkedList.prototype.addAtIndex = function(index, val) {
    const list = this;
    const node = new ListNode(val);
    let counter = 0;
    let curr = list.head;
    while (counter !== index -1) {
        curr = curr.next;
        counter++;
    }
    let temp = curr.next;
    curr.next = node;
    node.next = temp;
    list.length++;
}

LinkedList.prototype.deleteAtIndex = function(index) {
    const list = this;
    let counter = 0;
    let curr = list.head;
    let temp;
    while(counter !== index-1) {
        curr = curr.next;
        counter++;
    }
    temp = curr.next.next
    curr.next = temp;
    list.length--;
}

LinkedList.prototype.get = function(index) {
    const list = this;
    let counter = 0;
    let curr = list.head;
    while(counter !== index) {
        curr = curr.next;
        counter++;
    }
    return curr.val;
}

const obj = new LinkedList();
obj.addAtHead(1);
obj.addAtTail(3);
obj.addAtIndex(1,2);
obj.deleteAtIndex(1)
console.log(obj)

