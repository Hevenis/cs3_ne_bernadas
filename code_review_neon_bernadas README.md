### Annex C
#### Code Quality Assessment Worksheet

##### Section: 9 NEON Score:____________
##### C# / Name: RUDOLF BENEDICT BERNADAS	Date: AUGUST 26, 2026

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**
numbers = [5, 12, 18, 23, 31, 47, 56, 68, 74, 90]
target = 47

**Implementation 1**

    def linear_search(numbers, target):
  
       for i in range(len(numbers)):
    
       if numbers[i] == target:
           return i

       return -1


**Implementation 2**

    def binary_search(numbers, target):
   
       low = 0
   
       high = len(numbers) - 1


       while low <= high:
       
          middle = (low + high) // 2


          if numbers[middle] == target:
              return middle
          elif numbers[middle] < target:
              low = middle + 1
          else:
              high = middle - 1


        return -1






### Questions with Checklists
**1. Efficiency**
 
 Which algorithm is faster when the list of numbers is very large? Why?

>**Implementation 1**, because it is much _shorter_ than Implementation 2, making it faster and easier to run



#### Checklist to guide your answer:


**Implementation 1**

 How many elements might the algorithm need to check? not much |

 Does the algorithm reduce the search area as it runs? yes |

  Does the algorithm still work efficiently with a very large list? yes |


**Implementation 2**

 How many elements might the algorithm need to check? a lot |

 Does the algorithm reduce the search area as it runs? no |

  Does the algorithm still work efficiently with a very large list? no |


**2. Readability**
 
 Which algorithm is easier to understand at first glance? What makes it clearer?

>Admittedly, implementation 2 looks more simple for a less experienced coder such as I, but generally for other more advanced coders, it's **implementation 1** since it's shorter and says what its supposed to do much clearer than lots of if and elif codes.

#### Checklist to guide your answer:


**Implementation 1**

How meaningful are the variable names? pretty meaningful |

 How simple is the logic? very simple (to view for the eyes as well) |
 
  How concise is the code? very concise |
  
   How easy is it to follow the search process? pretty easy |


**Implementation 2**

How meaningful are the variable names? not exactly |

 How simple is the logic? not simple at all |
 
  How concise is the code? not that concise |
  
   How easy is it to follow the search process? takes more time to process what it's supposed to do |




**3. Maintainability**
 
 If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?
>**Implementation 1**, because it's easier to analyze and think about what to do when updating it.


#### Checklist to guide your answer:


**Implementation 1**
 
 Is the structure straightforward? Yes |
 
  Would adding new steps break the code easily? Not easily at least |
  
   Is there less chance of errors when updating? Yes |


**Implementation 2**
 
 Is the structure straightforward? No |
  
  Would adding new steps break the code easily? Yes |
   
   Is there less chance of errors when updating? No |



**4. Testability**
 
 Which algorithm is easier to test with different inputs? Why?
>**Implementation 1**, since it's simpler code to run and is easier and faster for my device to get the output.


#### Checklist to guide your answer:


**Implementation 1**
 
 Can you test with small lists easily? Yes |
  
  Does the algorithm have fewer conditions to check? Yes |
   
   Is the output predictable and clear? Yes |


**Implementation 2**
 
 Can you test with small lists easily? Yes, though it may take a bit more time |
  
  Does the algorithm have fewer conditions to check? No |
   
   Is the output predictable and clear? Kind of if you think long enough, but not really |



**5. Reliability and Input Validation**
 
 What should the algorithm check to avoid errors when receiving input from a user?
>In **both** implementations, they don't have any error checks, or at least from what I can deduce. First, both should check if the list is empty, has invalid inputs like string instead of integer, has weird units (like PI perhaps?), and if the list is sorted. I don't know how to do these though, I just know this is what the original coders of this thing are supposed to do.



#### Checklist to guide your answer:


**Implementation 1**
 
 Does the algorithm check if the list is empty? No |
  
  Does it handle invalid inputs (like letters instead of numbers)? No |
   
   Does it avoid crashing when inputs are unusual? No |
    
   Does it check that the list is sorted before using Linear Search? No |


**Implementation 2**
 
 Does the algorithm check if the list is empty? No |
  
  Does it handle invalid inputs (like letters instead of numbers)? No |
   
   Does it avoid crashing when inputs are unusual? No |
    
  Does it check that the list is sorted before using Binary Search? No |


**6. Final Answer**
Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.
>It would be **implementation 1**, as it's simpler and faster to run, simpler read and understand, straight forward, and is not as easy to break. I believe the other implementation/algorithm could work if it's meant to handler heavier/more complex lists/other code stuff. But for now, it's implementation 1.







(I’m unable to find a partner and I think I wasted a bit too much time on tutorials on md files, so I’m not sure if this really is the correct way to do it since I'm rushing right now, sorry…)
