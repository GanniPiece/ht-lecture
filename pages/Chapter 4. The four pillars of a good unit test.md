title:: Chapter 4. The four pillars of a good unit test

- title:: Chapter 4. The four pillars of a good unit test
- What is the good properties for good unit test?
	- 1. integrate into develop cycle
	  2. target most important part of codebase
	  3. max value / min cost
- What is four pillars of good unit test?
	- protection against [[regressions]]
		- the amount of code execution during test
		- the complexity of that code
		- the code's domain significance
			- library, frameworks, external system
	- resistance to refactoring
		- benefit
			- early warning before breaking functionality
			- won't lead regression after refactoring
		- false positive
			- decouple: the more the test is coupled to the implementation detailed of SUT, the more false alarms it generates.
		- What is the final outcome for the SUT?
		-
	- fast feedback
	- maintainability
-
-