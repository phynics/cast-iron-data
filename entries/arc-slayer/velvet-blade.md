+++
id = "ref/arc-slayer/velvet-blade"
kind = "archetype"
title = "Velvet Blade"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Velvet%20Blade"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "velvet_blade", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "70"

[fields]
kind = "archetype"
features = [
  { anchor = "studied-socialite" },
  { anchor = "courtly-graces", level = 1 },
  { anchor = "treacherous-blade", level = 7 },
  { anchor = "silent-dispatch", level = 11 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["courtly-graces"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["silent-dispatch"] },
  { alters = "Armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Studied target", feature = "studied-target", by = ["studied-socialite"] },
]
+++

Velvet blades specialize in infiltrating the upper echelons of society, mingling with nobles and
courtiers, and killing them. Velvet blades are often born into the aristocracy, with an intricate
understanding of the inner workings of upper-class society. Though a few velvet blades are unhinged
maniacs who enjoy preying on their peers, most of these well-heeled slayers assume a professional
demeanor and hire themselves out to other nobles or well-connected criminal organizations.

## Class Skills {#class-skills}

A velvet blade adds Diplomacy and Knowledge (nobility) to her list of class skills, instead of
Knowledge (dungeoneering).

This alters the slayer's class skills.

## Armor Proficiency {#armor-proficiency}

A velvet blade is not proficient with medium armor or shields.

This alters the slayer's armor proficiency.

## Studied Socialite (Ex) {#studied-socialite}

A velvet blade focuses her studies on social infiltration rather than brute force, believing it is
easier to kill an opponent quietly and unprepared than in a loud battle. She adds her studied target
bonus on Bluff, Diplomacy, Disguise, Intimidate, Knowledge, Perception, Sense Motive, Stealth, and
Survival checks against studied opponents, as well as to the DCs of slayer class abilities she uses
against such opponents. She never gains a bonus on weapon attack and damage rolls from her studied
target ability.

This ability alters studied target.

## Courtly Graces (Ex) {#courtly-graces}

A velvet blade spends long hours memorizing etiquette and family lineages of royalty and other
prominent families. She gains a bonus on Knowledge (nobility checks) equal to
[half](ref/misc/fractions-and-rounding) her slayer level (minimum +1).

This ability replaces track.

## Treacherous Blade (Ex) {#treacherous-blade}

At 7th level, a velvet blade can capitalize on how others underestimate her and allow her close to
them, assuming she is harmless. She gains the [Betrayer](ref/feat/betrayer) feat as a bonus feat,
whether or not she meets the prerequisites. Additionally, when making her first attack against a
studied target that believes her to be harmless or to be an ally, the attack counts as a sneak
attack, even if the target isn't flanked or denied its Dexterity bonus to AC, and the velvet blade
gains +2d6 sneak attack damage, increasing by 1d6 at 10th level and every 5 levels thereafter. Even
if she immediately attacks the target again (such as by continuing a full attack), only the first
attack gains these benefits, since the target immediately realizes the velvet blade is something
more than she seemed.

## Silent Dispatch (Ex) {#silent-dispatch}

At 11th level, a velvet blade becomes adept at taking out her targets quietly. She gains the
[silent dispatch](ref/vigtalent/silent-dispatch) vigilante talent without meeting the talent's
prerequisites.

This ability replaces swift tracker.
