+++
id = "ref/rule/using-a-library"
kind = "rule"
title = "Using a Library"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "using_a_library", path = "json/rules_subsystems04.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Intrigue pg 148

Every library has two primary statistics: a Complexity rating, which reflects the intricacy or
confusing nature of the library's contents, and knowledge points (abbreviated kp), which are an
abstract representation of the sum of the library's collected information.

To research a specific topic or question within a library, a character must succeed at a Research
check, using one of the skills listed in the library's stat block. Stat blocks for sample libraries
are listed [here](ref/rule/sample-libraries). A Research check is akin to a Knowledge check, though
each library stat block lists the specific skills that can be used for Research checks based on the
nature of that library's collections. A library's Complexity rating serves as the DC for Research
checks that attempt to unravel that library's clues.

Attempting a Research check requires an uninterrupted 8-hour period of research, and a character
cannot take 10 or 20 on a Research check. Each 8-hour period of research grants a cumulative +1
bonus on Research checks. If a researcher stops researching at the same library for a month or more,
she loses any cumulative bonuses gained for that library thus far. Up to two additional characters
can use the aid another action to assist a primary researcher. In addition, some libraries grant a
Knowledge bonus - a bonus on specific Knowledge checks (including Research checks) attempted within
that library - due to the depth and completeness of its collections. Research checks cannot normally
be attempted untrained unless the library's Complexity is 10 or lower, the Research check involves a
skill that allows untrained checks, or the library's collection is extensive enough to allow
untrained checks, as detailed in the library's stat block.

Succeeding at a Research check reduces a library's knowledge points, similar to dealing damage to a
creature's hit points. As its knowledge points decrease, a library reveals its secrets. Characters
learn information when a library's knowledge points reach various research thresholds, as detailed
in each library's stat block. The amount of knowledge points reduced on a successful Research check
depends on the nature of the primary researcher and the type of library. It is generally a
reflection of the character's training and Intelligence score, represented by a die roll modified by
the character's ability modifier (see [Research by Expertise](ref/rule/research-by-expertise)).

In addition to these base amounts, for every 5 by which a Research check exceeds the library's
Complexity rating, the library's knowledge points are reduced by 1 additional point. Rolling a
natural 20 on a Research check acts like a critical threat. If the researcher confirms the critical
hit by succeeding at a second Research check with all the same modifiers (this takes no additional
time), the resulting knowledge point reduction is doubled. Conversely, rolling a natural 1 on a
Research check automatically results in failure, and the library's knowledge points increase by 1/4
of the library's maximum knowledge points as the library's complexity causes a researcher to follow
a wrong avenue of investigation.

When a library's knowledge points are reduced to 0, the characters have learned everything they can
from that library, and gain experience points according to the library's CR. To learn additional
information, they must visit another library and continue their research there.
