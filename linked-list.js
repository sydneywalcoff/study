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

const obj = new LinkedList();
obj.addAtHead(1);
obj.addAtTail(3);
console.log(obj)
