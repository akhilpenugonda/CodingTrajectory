
var lengthOfLinkedList = function(root)
{
    var length = 0;
    while(root != null)
    {
        length++;
        root = root.next;
    }
    return length;
}
var getIntersectionNode = function(headA, headB) {
    let lengthA = lengthOfLinkedList(headA);
    let lengthB = lengthOfLinkedList(headB);

    if(lengthA > lengthB)
    {
        for(let i = 0; i < lengthA - lengthB; i++)
        {
            headA = headA.next;
        }
    }
    else
    if(lengthB > lengthA)
    {
        for(let i = 0; i < lengthB - lengthA; i++)
        {
            headB = headB.next;
        }
    }

    while(headA && headB)
    {
        if(headA == headB)
        {
            return headA;
        }
        headA = headA.next;
        headB = headB.next;
    }
    return null;
};

// var getIntersectionNode = function(headA, headB) {
//     let a = headA, b = headB
//     while (a !== b) {
//         a = !a ? headB : a.next
//         b = !b ? headA : b.next
//     }
//     return a
// };