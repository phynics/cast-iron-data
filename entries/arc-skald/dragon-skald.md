+++
id = "ref/arc-skald/dragon-skald"
kind = "archetype"
title = "Dragon Skald"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Dragon%20Skald"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragon_skald", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "advanced-class-origins"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "wind-whistler", level = 1 },
  { anchor = "sea-legs", level = 1 },
  { anchor = "fearless-raider", level = 2 },
  { anchor = "glorious-epic", level = 3 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["wind-whistler"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["sea-legs"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["fearless-raider"] },
  { replaces = "Song of marching", feature = "song-of-marching", by = ["glorious-epic"] },
]
+++

The Ulfen prize skalds on sea raids and linnorm hunts. Dragon skald performances involve song,
whistling, or blowing mighty horns, and viking sailors often talk about having a skald along to
whistle up a wind or sing away the mists on the morning of a momentous raid.

## Wind Whistler (Su) {#wind-whistler}

At 1st level, a dragon skald adds _[alter winds](ref/spell/alter-winds)_,
_[fog cloud](ref/spell/fog-cloud)_, and _[obscuring mist](ref/spell/obscuring-mist)_ to his class
spell list, at the same levels the wizard gains them. He still must add these spells to his spells
known as normal. This ability replaces Scribe Scroll.

## Sea Legs (Ex) {#sea-legs}

A dragon skald adds 1/2 his class level (minimum 1) on all Profession (sailor) checks, Survival
checks while at sea, Acrobatics and Climb checks made while aboard a boat, and Swim checks. This
ability replaces bardic knowledge.

## Fearless Raider (Ex) {#fearless-raider}

At 2nd level, the dragon skald becomes resistant to fear effects. The dragon skald gains a +4 bonus
on saving throws against fear effects, and DCs to affect the dragon skald with the Intimidate skill
increase by 4. This ability replaces well-versed.

## Raging Song (Su) {#raging-song}

A dragon skald gains access to the following raging song.

## Glorious Epic (Su) {#glorious-epic}

At 3rd level, a dragon skald learns how to truly extol the virtues and prowess of the heroic figures
in his epic tales. By performing for 10 minutes and expending 1 round of raging song, the dragon
skald can influence opinions positively towards a heroic subject of the dragon skald's choice. If
the subject of the epic attempts a Diplomacy or Intimidate check against anyone who listened to the
full performance, he receives a circumstance bonus on that check equal to the Will save bonus
granted by the dragon skald's inspired rage. This ability replaces song of marching.
