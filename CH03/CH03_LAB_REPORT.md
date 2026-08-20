# Lab Report — Chapter 3: Recursion

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your output, including part of the call-stack trace.*

```
----- Task 1: find_file -----
-> entering: /root
  -> entering: /root/readme.txt
  <- exiting: /root/readme.txt
  -> entering: /root/photo.jpg
  <- exiting: /root/photo.jpg
  -> entering: /root/documents
    -> entering: /root/documents/resume.docx
    <- exiting: /root/documents/resume.docx
    -> entering: /root/documents/cover_letter.docx
    <- exiting: /root/documents/cover_letter.docx
    -> entering: /root/documents/taxes
      -> entering: /root/documents/taxes/2022.pdf
      <- exiting: /root/documents/taxes/2022.pdf
      -> entering: /root/documents/taxes/2023.pdf
      <- exiting: /root/documents/taxes/2023.pdf
    <- exiting: /root/documents/taxes
  <- exiting: /root/documents
<- exiting: /root
/root/documents/taxes/2023.pdf
-> entering: /root
  -> entering: /root/readme.txt
  <- exiting: /root/readme.txt
  -> entering: /root/photo.jpg
  <- exiting: /root/photo.jpg
  -> entering: /root/documents
    -> entering: /root/documents/resume.docx
    <- exiting: /root/documents/resume.docx
    -> entering: /root/documents/cover_letter.docx
    <- exiting: /root/documents/cover_letter.docx
    -> entering: /root/documents/taxes
      -> entering: /root/documents/taxes/2022.pdf
      <- exiting: /root/documents/taxes/2022.pdf
      -> entering: /root/documents/taxes/2023.pdf
      <- exiting: /root/documents/taxes/2023.pdf
    <- exiting: /root/documents/taxes
  <- exiting: /root/documents
  -> entering: /root/music
    -> entering: /root/music/song1.mp3
    <- exiting: /root/music/song1.mp3
    -> entering: /root/music/song2.mp3
    <- exiting: /root/music/song2.mp3
    -> entering: /root/music/playlists
      -> entering: /root/music/playlists/workout.m3u
      <- exiting: /root/music/playlists/workout.m3u
    <- exiting: /root/music/playlists
  <- exiting: /root/music
  -> entering: /root/empty_folder
  <- exiting: /root/empty_folder
<- exiting: /root
None
----- Task 2: count_files -----
9
----- Task 3: total_size -----
374
----- Task 4 (bonus): print_tree_with_depth -----
root
  readme.txt
  photo.jpg
  documents
    resume.docx
    cover_letter.docx
    taxes
      2022.pdf
      2023.pdf
  music
    song1.mp3
    song2.mp3
    playlists
      workout.m3u
  empty_folder

```

## Reflection Questions

1. **Explain recursion to someone who has never programmed.**
   - Imagine a scenario where a box might contain smaller boxes inside of it, and somewhere among all of them is an item you are looking for. TO find that item, you open a box and look to see what is inside. If you find the item you are looking for, you simply grab your item, and close the box. If you do not find your item, and see more boxes inside, you will have to repeat the same process on each of those smaller boxes. If you reach the point where you open a box and there are no more smaller boxes or item inside, you then stop. Recursion uses a similar concept where you repeat a process until a specific condition is met. In my example, that condition is if there are no more boxes to open.

2. **An empty folder is a legitimate base case, not an error. Why does treating it as an error break the program?**

  - In my output, /root/empty_folder was entered and exited cleanly even though it had no files inside it, and the program didn't crash or throw any errors. Since the program had nothing to loop through, it returned the function immediately. If the code instead treated an empty folder as an error, it would break the recursion for every empty directory, even though an empty folder is a completely normal state a file system can be in. Recursion depends on being able to reach a clean stopping points, and an empty folder would be a perfect stopping point.

3. **A folder nested 10,000 levels deep would crash your code. Why?**
  - Most coding languages has a limit on how many stack frames can exist at once, such each stack uses memory. A folder that is nested 10,000 levels deep would mean 10,000 recursive calls stacking on top of each other before any of them count properly return. Which would exceed most language's default recursion limit and throw a stack overflow error.
