+++
id = "ref/feat/lucky"
kind = "feat"
title = "Lucky"
aon = "FeatDisplay.aspx?ItemName=Lucky"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lucky", path = "json/feat10.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/black-cat", label = "or" },
  { kind = "prerequisite", target = "ref/feat/lucky-halfling", label = "or" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "6"

[fields]
kind = "feat"
prerequisites = "Black Cat or Lucky Halfling; must have a racial trait with \"luck\" in its name."
prerequisite_feats = ["ref/feat/black-cat", "ref/feat/lucky-halfling"]
benefit = "Choose one of the following feats: Black Cat, Lucky Halfling, or any feat that lists one of these feats as a prerequisite and is usable once per day. Add two to the number of times per day that you can use the chosen feat. You must have the chosen feat in order to select it with Lucky."
special = "This feat can be selected multiple times. You cannot add more than six uses to a single feat in this manner. A character with the Defiant Luck feat can ignore this feat's prerequisites, but she must choose Defiant Luck or a feat that lists Defiant Luck as a prerequisite and is usable once per day."
+++

Your luck-based abilities seem limitless.\
**Prerequisites:** [Black Cat](ref/feat/black-cat) or [Lucky Halfling](ref/feat/lucky-halfling);
must have a racial trait with "luck" in its name.\
**Benefit:** Choose one of the following feats: Black Cat, Lucky Halfling, or any feat that lists
one of these feats as a prerequisite and is usable once per day. Add two to the number of times per
day that you can use the chosen feat. You must have the chosen feat in order to select it with
Lucky.\
**Special:** This feat can be selected multiple times. You cannot add more than six uses to a single
feat in this manner. A character with the [Defiant Luck](ref/feat/defiant-luck) feat can ignore this
feat's prerequisites, but she must choose Defiant Luck or a feat that lists Defiant Luck as a
prerequisite and is usable once per day.
