/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    public:
        ListNode* reverseKGroup(ListNode* head, int k) {
            int len = 0 ; 
            ListNode* curr = head ; 
            while( curr ){
                len++ ; 
                curr = curr->next ; 
            }
            ListNode* dummy = new ListNode(-1) ; 
            int rounds = len/k ; 
            ListNode* ele = head ; 
            ListNode* tail = dummy ; 
            while( rounds-- ){
                ListNode* rs = ele ; 
                ListNode* nextTail = ele ;
                ele = ele->next ;  
                for( int i=1 ; i<k ; ++i ){
                    ListNode* temp = ele->next ; 
                    ele->next = rs ;
                    rs = ele ; 
                    ele = temp ; 
                }
                nextTail->next = nullptr ; 
                tail->next = rs ; 
                tail = nextTail ; 
            }
            tail->next = ele ; 
            return dummy->next ; 
        }
    };