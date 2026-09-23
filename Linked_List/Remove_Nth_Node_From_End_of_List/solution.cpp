

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode* removeNthFromEnd(ListNode* head, int n) {
      ListNode* right = head ; 
      ListNode* left = head ; 
      while( n-- > 0 ){
          right = right->next ; 
      }
      if( !right ){
          return head->next; 
      }
      while( right->next  ){
          right = right->next ; 
          left = left->next ; 
      }
      left->next = left->next->next ;
      return head ; 
  }
};