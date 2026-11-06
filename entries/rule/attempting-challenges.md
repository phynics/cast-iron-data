+++
id = "ref/rule/attempting-challenges"
kind = "rule"
title = "Attempting Challenges"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "attempting_challenges", path = "json/rules_opt_magic01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 180

Each challenge presents two tasks. One creator can choose a single task to attempt, or two creators
can each choose to do a different task. This choice of tasks to attempt must be made before rolling
any associated checks. Creators can't take 10 or 20 (even with bardic knowledge or skill mastery) or
benefit from aid another on item creation tasks.

Some tasks don't require checks, but present other conditions for success. If a creator takes on
such a task, it must be completed before attempting a task that involves a check.

If the creators decide to attempt both tasks for a given challenge, each task must be attempted by a
different creator. For instance, when faced with a
[sesquipedalian elucidation challenge](ref/rule/random-challenges), a wizard might pull out his
dictionary and attempt a Linguistics check, while a rogue might choose to make up her own big words
and attempt a Use Magic Device check. The number of tasks attempted and their success or failure
determines the outcome of the challenge, as detailed below.

|One Task Attempted|Both Tasks Attempted|Challenge Result|
| --- | --- | --- |
|-|Succeed at both|Critical success|
|Succeed|Succeed at one and fail the other by less than 5|Success|
|Fail|Succeed at one and fail the other by 5 or more|Failure|
|-|Fail both|Critical failure|
