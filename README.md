# Hubble homework 4

This is the Homwork for CP1-24 based on Edwin's Hubble paper on the velocity-distance relation of extra galactic nebulae.
Everyone has to choose a task during the first day after publishing the homework.
Tasks are distributed on a first come first serve basis starting with distributing tasks in class.
The tasks have strict deadlines and depend on each other. 
Every task will be graded at the time it is due.
Any missing task element at its deadline will be filled in by me.

3 teams for 3 task groups:

*Team Data and Documentation (3 members):*
- Select the 9 groups (due till HW deadline -6 days)(1 member) 
- Describe in the documentation how the 9 groups were selected (1 member due till HW deadline -2 days)
- Compare the slope of the fitted straight line to Hubble's value of K and explain if there is a discrepancy (1 member due at homework deadline).

*Team Algorithm + unit test + docstrings (12 members):*
- Translate the pseudo-code below into python code (1 member) with docstrings (1 member) and unit tests (1 member) (due till HW deadline -6 days)
- Make a least-squares fit with uncertainties to the 9 groups (open circles) in Figure 1 of [_Hubble's 1929 article_](https://www.pnas.org/content/pnas/15/3/168.full.pdf) using the code above (1 member due till HW deadline -3 days).
- Write a function that takes lists of velocities and distances and returns a dictionary of the fitting parameters (1 member) (including unit test and docstrings) (1 member due till HW deadline).
- Write a function that can estimate the age of the universe based on the data in the Hubble paper (1 member) (including unit test and docstrings 1 member)) (due till HW deadline days).
- Determine the 9 groups of the figure (see documentation team) and generate a csv file with the velocities and distances (1 member due till HW deadline -4 days).
- Programmatically read back in this data in your code to do the fit (1 member) (including unit test and docstrings 1 member) due till HW deadline).

*Team Tools (2 members):*
- Add github action for unit testing (using pytest) (1 member) for all code (due till HW deadline -4 days)
- Add github action for linting (flake8)  (1 member) for all code (due till HW deadline -6 days)
- The team tools members are also the maintainer of this homework responsible for merging PRs.


### Pseudocode:
```
input data
n = size of data
if n < 2 : 
   print ‘Error! Not enough data!’
   return
for i = 0... N-1 : 
   if abs( sigma_i ) < 0.00001 : 
      return
   S += 1.0 / sigma_i**2
   s_x += x_i / sigma_i**2
   s_y += y_i / sigma_i**2
for i = 0... N-1 : 
   t_i = 1.0 / sigma_i * (x_i-s_x/S)
   s_tt = t_i**2
   b += t_i * y_i / sigma_i
if abs( S ) < 0.000001 : 
   return
a = (s_y - s_x * b) / S
b = b / s_tt
sigma_a2 = (1 + s_x**2/S*s_tt) / S
sigma_b2 = 1.0 / s_tt
for i = 0... N-1 : 
   chi2 += ((y_i - a - b*x_i)/sigma_i)**2
```

**Note:**
Galaxy catalog available at (http://spider.seds.org/ngc/ngc.html). 

## Grading

| Homework Points                  |                |              |            |
| -------------------------------- | -------------- | ------------ | ---------- |
|                                  |                |              |            |
| Interaction on project           |                |              |            |
| Category                         | min per person | point factor | max points |
| Commits                          | 1              | 1            | 1          |
| Pull requests                    | 1              | 3            | 3          |
| PR Accepted                      | 1              | 4            | 4          |
| Other PR reviewed                | 1              | 3            | 3          |     
| Issues                           | 1              | 1            | 1          | 
| Closed Issues                    | 1              | 1            | 1          |
| \# Conversations                 | 25             | 1/5          | 5          |
|                                  |                |              |            |
| Total                            |                |              | 18         |
|                                  |                |              |            |
| Shared project points            |                |              |            |
| \# Milestones                    | 18             | 1/6          | 3          |
|                                  |                |              |            |
| Total                            |                |              | 21         |
|                                  |                |              |            |
|                                  |                |              |            |
| Result                           |                |              |            |
| Task completion                  |                |              | 21         |
|                                  |                |              |            |
| Sum                              |                |              | 42         |
