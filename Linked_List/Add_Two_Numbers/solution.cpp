struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0) ; 
        ListNode* curr = dummy ;
        int carry = 0 ; 
        while( l1 || l2 || carry ){
            int a = 0 , b = 0; 
            if( l1 ){
                a = l1->val ; 
                l1 = l1->next ; 
            }
            if( l2 ){
                b = l2->val ; 
                l2 = l2->next ; 
            }
            int sum = a + b + carry ; 
            curr->next =  new ListNode( sum%10 ) ; 
            curr = curr->next ; 
            carry = sum>9 ? 1 : 0 ; 
        }
        return dummy->next ; 
    }
};