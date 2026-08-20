# Lab Report — Chapter 6: Breadth-First Search

*Complete both sections and commit this file with your code.*

## Test Results

```
True
True
2
['you', 'claire', 'thom', 'diego']
True
['create_repo_template', 'write_starter_code', 'write_tests', 'create_classroom_assignment', 'invite_students', 'grade_submissions']

```

## Reflection Questions

1. **Explain breadth-first search to someone who has never programmed.**
   - Imagine you need to hire a roofing service to replace your worn down roof. Instead of asking random strangers on the street, you decide to call your friends first to ask if they know any good services. With no luck from them, you decide to call the friends of your friends next, then you try your friends' friends' friends. Breadth-First Search is essentially the same concept, you start with the circle closest to you, then you branch out one circle at a time.

2. **Two people in your network each know the other. Walk through what happens without the `searched` set.**
  - Without the `searched` set to remember who you have already checked in the search, you will pull one person from the queue and check their connections, and you will add the other person to the queue. You will then pull the other person from the queue and check their connections, which will lead you back to the first person you checked. In short, you will be left in an infinite loop as you will continue this process repeatedly with no end in sight.

3. **Where does this show up in real software?**
   - "People you may know" on a social media platform like Facebook or Instagram is a very solid example of Breadth-First Search. It is essentially why these social media platforms may suggest connections that are friends of your friends. Mutual connections, if you will. It starts with the closest circle, which are friends or connections you already have added, and then it branches out one more circle, which is friends or connections that your friends or connections have added.
