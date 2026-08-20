# Lab Report — Chapter 12: K-Nearest Neighbors

*Complete both sections and commit this file with your code.*

## Test Results

```
[{'features': [6, 4], 'label': 'orange'}, {'features': [7, 3], 'label': 'orange'}, {'features': [6, 3], 'label': 'orange'}]
orange
dog
cat
dog
standard
premium
likes
4.666666666666667
4.666666666666667

```

## Reflection Questions

1. **Explain k-nearest neighbors to someone who has never programmed.**
   - Imagine you want to guess whether or not someone will like a new restaurant that you found, but you don't know them that well. However, you do know a bunch of other people's tastes and preferences, so you find the people whose taste preferences are most similar to this person's. You then invite those people first to gauge their reactions and opinions. That is essentially how k-nearest neighbors works. You borrow the judgement whoever is closest to the person in taste.

2. **Two classmates pick k = 1 and k = 15 on the same data and get different answers. What is each one doing wrong, or right?**
  - The classmate that picked k =1 is trusting a single nearest neighbor completely. This introduces many risk as it could be a weird outlier. On the other hand, the classmate that picked k = 15 is averaging their result over a much wider neighborhood, this essentially eliminates the risk of an outlier drastically swaying the result.
3. **Chapter 12 says Netflix-style recommendations work this way. Describe how someone's viewing history becomes the "features."**
  - Netflix will compare and contrast two viewers who have watched and rated a similar mix of shoes and movies. Netflix will then use that as a reference point and begin to recommend shows or movies to one person if the other person, or the nearest neighbor, has watched a show that you many have not seen yet. It suggests these titles because it borrows the judgement and opinion of the nearest neighbor.
