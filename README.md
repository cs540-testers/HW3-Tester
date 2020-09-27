# HW3-Tester
This is a tester for HW3 of CS540 at UW Madison  
  
To run, download test.py and ref.txt to your working folder.  
BACK UP YOUR CODE. WE ARE NOT RESPONSIBLE FOR DAMAGE.  
In a terminal, run 
```
python3 test.py
````
or 
```
py test.py
```
on some Windows systems.  
  
The tester will generate a test.txt. Deleting or modifying it doesn't affect the tester.

---
**NOTE: Set random.seed(1) at the beginning of n_queens_restart()!!!**

**Don't freak out if n_queens_restart() fails. It requires you to generate a random state in a specific way.**
The reference output was generated with random.seed(1) set at the beginning of the n_queens_restart() function.
Make sure you do the same to ensure you get the same random number sequence.

---
  
When you are convinced that you have a correct solution, please do the following:  
1) Run the tester  
2) Copy the  output printed to the console  
  a. You might have to save the printed output to file by using ```python3 test.py > output```  
3) Create an issue at https://github.com/cs540-testers/HW3-Tester/issues and paste the output  
  
If your output matches ref, we will close your ticket. If not, we can discuss a resolution at  
https://discord.gg/CuJdjN  
  
DO NOT SHARE ANY CODE.
