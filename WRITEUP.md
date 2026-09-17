# HW0 writeup

**Name:** Nayla Trigueros
**Date:** 2026-09-11

Replace every placeholder below with your answer. Every number you give comes from a script in this repo; say which one.

## Part 1. Basic rating statistics

Code: `human_part1.py`. One or two sentences per answer, with the numbers.

**(a) How many ratings, users, and movies are there, and how are ratings distributed across 1–5 stars?**

Using human_part1.py, There are 100000 of ratings There are 943 of users. There are 1682 of movies. And the distribution looks like:
rating
1 star    6110
2 star   11370
3 star   27145
4 star   34174
5 star   21201

**(b) What is the median number of ratings per user, and how many users have 100 or more ratings?**

Using human_part1.py, the median rateings per user is: 65.0, and the users with 100+ ratings are this many: 364

**(c) Which 10 movies have the most ratings?**

Using human_part1.py, The 10 movies with the most ratings are:
Star Wars (1977)                 583
Contact (1997)                   509
Fargo (1996)                     508
Return of the Jedi (1983)        507
Liar Liar (1997)                 485
English Patient, The (1996)      481
Scream (1996)                    478
Toy Story (1995)                 452
Air Force One (1997)             431
Independence Day (ID4) (1996)    429

**(d) Among movies with at least 20 ratings, which 10 have the highest mean rating?**

Using human_part1.py, The top 10 highest-rated movies that have at least 20 reatings are:
Close Shave, A (1995) mean =  4.491071428571429 count =  112
Schindler's List (1993) mean =  4.466442953020135 count =  298
Wrong Trousers, The (1993) mean =  4.466101694915254 count =  118
Casablanca (1942) mean =  4.45679012345679 count =  243
Wallace & Gromit: The Best of Aardman Animation (1996) mean =  4.447761194029851 count =  67
Shawshank Redemption, The (1994) mean =  4.445229681978798 count =  283
Rear Window (1954) mean =  4.3875598086124405 count =  209
Usual Suspects, The (1995) mean =  4.385767790262173 count =  267
Star Wars (1977) mean =  4.3584905660377355 count =  583
12 Angry Men (1957) mean =  4.344 count =  125

**Anything you got stuck on (what you tried, where it broke), or "none":**

I was unsure on how to do part d, because I got the title of the movies and their rating but I had no idea how to also show count. Eventually I tried a for loop and it looks a little messy but it works!

## Part 2. The best movie

Code: `human_part2.py`.

**My rule:** Among movies with 50+ ratings, rank by mean rating

**One rule I considered and rejected, and why:** I thought of only using the number of ratings as a rule (most = best), but then I decided agaisnt it because it only looks at popularity. A film rated many times does not mean the ratings were good.

**Top 10 under my rule:** 408 Close Shave, A (1995) count =  112 mean =  4.491071428571429
318 Schindler's List (1993) count =  298 mean =  4.466442953020135
169 Wrong Trousers, The (1993) count =  118 mean =  4.466101694915254
483 Casablanca (1942) count =  243 mean =  4.45679012345679
114 Wallace & Gromit: The Best of Aardman Animation (1996) count =  67 mean =  4.447761194029851
64 Shawshank Redemption, The (1994) count =  283 mean =  4.445229681978798
603 Rear Window (1954) count =  209 mean =  4.3875598086124405
12 Usual Suspects, The (1995) count =  267 mean =  4.385767790262173
50 Star Wars (1977) count =  583 mean =  4.3584905660377355
178 12 Angry Men (1957) count =  125 mean =  4.344


**Why my rule, in at most 150 words. Name one thing it gains and one thing it loses:**

A raw average of all the ratings gets dominated by noise from small samples, i.e, a movie with 2 5 star ratings would make it higher on the list than another movie with a bigger ratings range. 50 ratings is a good threshold in my opinion to get more meaningful results and helps to filter out small samples while keeping a low enough bar that regular films make it alongside huge mainstreams. It gains: A list of both well-liked movies and well-known. It loses: Under-watched but valuable movies get filtered out.

## Part 3. The most ___ movie

Code: `human_part3.py`.

**My adjective:** polarizing

**My definition** (one sentence, precise enough that a classmate could code it)**:** among movies with at least 50 ratings, the most polarizing movie has the highest standard deviation of ratings (meaning people are most split between loving and hating it.)

**One definition I considered and rejected, and why:** I wanted to use the starts (so 1 star or 5 star) ratings as a measurement rather than standard deviation. After I thought it out and thinking of STAT 253, I rejected it because it does not account for the consistency in the divide in ratings.

**Top 5 under my definition:**

1065 Koyaanisqatsi (1983) count =  53  mean =  1.3675165799787186
898 Postman, The (1997) count =  58  mean =  1.3513229833029046
53 Natural Born Killers (1994) count =  128  mean =  1.3272396018164618
640 Cook the Thief His Wife & Her Lover, The (1989) count =  82  mean =  1.323814258689104
219 Nightmare on Elm Street, A (1984) count =  111  mean =  1.3133847589261591

**What your definition captures, what it misses, and where "___-ness" lives in this data — the
genre labels, what the crowd did, or the words in the titles. At most 150 words:**

it captures polarizing-ness based on the users behavior. It uses the indiidual ratings no matter genre or title. It however ignores why opinions might differ. Like different audiences rate things differently. It also treats all ratings as equal in terms of timing, missing trends or popularity over the years. Within this data, polarizing-ness is in what the crowd (users) did (rating movies)

## Part 4. Claude's answers

Claude answers the same three questions in `claude_answers_1_2_3.py`, without seeing your code
or your answers.

**Did its numbers for Part 1 match yours? If not, which, and what did you find?**

It did! It also added percentage comparisons next to each number for 1a which is interesting. The format in its answers are also way cleaner than mine, which I think derives from the fact that I followed a very limited format based on orevious knowledge from for example Core Concepts (COMP 123. ) Looking at Claude's code I doubt I would've been able to recreate that.

## Part 5. Comparing the best movie

**Claude's rule:**

highest mean rating among movies with a reasonably large number of ratings

**Read what Claude wrote about its rule. Does it anywhere admit the rule was a choice, and that a different rule was possible? Or does it give its answer as simply the answer? Quote the sentence that decides it:**

Claude looked at best movies with 20, 50 and 100 ratings. It explains why it chose the rule, but not that it was explicitly a choice: "A raw average is misleading for movies with only a handful of
    # ratings (a single 5-star rating gives a "perfect" 5.0 mean with
    # n=1). So "best" here means:"

**Your Part 2 top 10 and Claude's Part 2 top 10 — not the Part 1(d) lists. Where do they differ, and why?**

For this part, my Claude did not provide a list, just gave me 1 best movie overall. Which does agree with mine, but my for loop did return the top 10 with my rule. I guess somewhere in the code, claude puts a limit to 1 movie just like i put on my loop that as soon as the shown movies reach 10, the for loop should stop.

**Better for what purpose? Name a situation where your rule is the right one and a situation where Claude's is. At most 150 words. You may conclude yours, its, or neither:**

Mine would be a better option if, say, the Main Cinema Theater wanted to show crowd favorites and they used this data to see which movies they could show in a film festival. Claude's could be better if an investor is interested in buying rights or stocks to a certain well-rated movie. It depends on the context, but simply because mine shows a wider range, I would say mine as it coukd be used for multiple purposes.

## Part 6. Comparing the most ___ movie

**Claude's definition:**

Polarizing

**Is Claude's film in your top 5?**

I chose the same word after searching on Google the most popular terms to describe movies in recent years. I wonder if the response Google gave me uses the same data that Claude used to pick its word. We coded this very differently, and interestingky enough, our lists are very different. The top 1 in Claude's list that is supposed to be similar to mine, actually is different. And my list includes a film that is not listed in Claude's list. 

**What Claude's definition sees that yours does not, and the reverse. At most 150 words:**

Claude's definition makes a distiction between film that are polarizing per se and films that are either highly liked or disliked. I think my list does not have seperate boundaries and I used a similar set up to my part 2 (since it was easiest, oops?) so it showed polarizing movies with 50+ ratings, while Claude's answer had sepoerate thresholds.

## Working with Claude

**What you asked Claude for during Parts 1–3** (debugging and installing only — say what you
got stuck on)**:**

I asked it for this: "How do I start the homework?", "What is the name of the dataset?", "What to do if I'm done with Part 1?", "How do I get the numbers for the writeup if I can't run individual parts?", "How to run it", "Do I commit anything yet, or keep going until Part 3?"

I mentioned it in class too, but I clearly had issues rememring the setup in VS code, so it was super helpful with that. After, I also asked if I could go back and fix typos for my writeup after I committed, but I apparentky couldn't so I hope everything's still understandable.

**Something Claude said that you could not verify, and why. Or "none," and how you checked:**

None, I didn't really ask stuff other than how to navigate my VS code or where to find certain things in all the files.

**What you would do differently next time, in 3–5 sentences:**

If I had known, I maybe would have gone with a similar word to polarizing, maybe "dividing", and see if our lists diferred. It would have been interesting to see if different thresholds still rendered the same movies or not. I would have also started a little earlier because I had some issues getting Claude started.

**Where did this assignment slow you down for a reason that was its fault, not yours? Point at
the step. Or "nowhere." One or two sentences:**

With the readme instructions, I was a little confused as to where to start with the whole process of downloading Claude code and getting it to work; the order there is not what I ended up doing with Shilad's help. 

**Hours spent:** 4.5 hours

**Anyone who helped you, or "no one":** Google search for "What are some popular terms to describe films", and search for " Ways to measure divergence in people who liked a movie and people who didn't". Class resources for STAT 253 (taken with Brianna heggeseth in 2025).
