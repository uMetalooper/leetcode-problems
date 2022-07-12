#include <vector>
#include <iostream>
#include <string>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        // in these 2 cases we don't need to do anything
        if (!head || !head->next) return head;

        ListNode* slow = head, * fast = head->next, * result = slow, * tmp;
        int first = -101;
        while (fast) {
            if (fast->next == nullptr) {
                slow->next = fast;
                slow = slow->next;
                fast = fast->next;
            }
            else {
                if (fast->val != fast->next->val) {
                    slow->next = fast;
                    slow = slow->next;
                    fast = fast->next;
                }
                else {
                    int val = fast->val;
                    if (first < -100) first = val;
                    tmp = fast;
                    while (tmp && tmp->val == val) {
                        tmp = tmp->next;
                    }
                    fast = tmp;
                }
            }
        }
        // clean duplicates at the end: 1,2,3,4,4,NULL
        //                                  |      ^
        //                                next     |
        //                                  |------|
        slow->next = fast;

        // clean duplicate at the front
        // case 1: list input: 1,1,1,2,3,4
        //         list until now: 1,2,3,4 (first = 1)
        if (result->val == first)
            result = result->next;

        // case 2.1: list input: 1,1,2,3,4
        //           list until now: 1,1,2,3,4
        //
        // case 2.2: list input: 1,1,NULL
        if (result && result->next && result->val == result->next->val)
            result = result->next->next;
        return result;
    }
};

ListNode* buildLinkedList(vector<int> iterable) {
    int n = iterable.size();
    if (n == 0) {
        return nullptr;
    }
    ListNode* head = new ListNode(iterable[0]);
    ListNode* p = head;
    for (int i = 1; i < n; i++) {
        p->next = new ListNode(iterable[i]);
        p = p->next;
    }
    return head;
}

void PrintLinkedList(ListNode* head) {
    ListNode* p = head;
    while (p) {
        cout << p->val << " ";
        p = p->next;
    }
    cout << endl;
}

int main() {
    Solution* _driver = new Solution();
    vector<int> nums = vector<int>({ 1,1 });

    ListNode* head = buildLinkedList(nums);
    PrintLinkedList(head);
    ListNode* result = _driver->deleteDuplicates(head);
    PrintLinkedList(result);

    return 0;
}