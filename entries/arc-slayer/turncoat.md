+++
id = "ref/arc-slayer/turncoat"
kind = "archetype"
title = "Turncoat"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Turncoat"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "turncoat", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "dubious-recognition", level = 1 },
  { anchor = "double-speak", level = 7 },
  { anchor = "sudden-betrayal", level = 14 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["dubious-recognition"] },
  { replaces = "Stalker", feature = "stalker", by = ["double-speak"] },
  { replaces = "Quarry", feature = "quarry", by = ["sudden-betrayal"] },
  { replaces = "improved quarry", feature = "improved-quarry", by = ["sudden-betrayal"] },
]
+++

In Sekamina, betraying others before they have the chance to betray you can be a necessary survival
technique. While not all adventurers have the heart for such underhanded dealings, others have
developed a knack for it. The turncoat's natural talents for deception and treachery are fitting
when negotiating with the untrustworthy inhabitants of Sekamina and other notoriously unscrupulous
areas, and his ability to adapt allows him to preempt opponents' schemes. Not all party members may
be comfortable with having someone so adept at backstabbing among their ranks, but most tend to be
grateful that he uses his skills to their benefit.

## Dubious Recognition (Ex) {#dubious-recognition}

A turncoat adds half his level (minimum 1) to Sense Motive checks to recognize when a creature is
lying or attempting to take advantage of the turncoat and his allies.

This replaces track.

## Double Speak (Ex) {#double-speak}

At 7th level, a turncoat can attempt a Bluff check in place of a Diplomacy check against a studied
target. The target can attempt an opposed Sense Motive check.

This ability replaces stalker.

## Sudden Betrayal (Ex) {#sudden-betrayal}

At 14th level, as a standard action a turncoat can choose a single creature within 30 feet. He gains
a +4 circumstance bonus on [Diplomacy](ref/skill/diplomacy) checks against this target. If the
target has an attitude of indifferent or better toward him, the first attack roll the turncoat makes
against that target is automatically treated as threatening a critical hit. If the target's attitude
is friendly or better, a successful attack is treated as a confirmed critical hit. This ability can
be used only once per day.

At 19th level, the bonus increases to +6, and the attack is treated as a confirmed critical hit if
the target is at least indifferent to the turncoat.

This ability replaces quarry and improved quarry.
