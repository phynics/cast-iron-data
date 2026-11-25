+++
id = "ref/arc-rogue/phantom-thief"
kind = "archetype"
title = "Phantom Thief"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Phantom%20Thief"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantom_thief", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "46"

[fields]
kind = "archetype"
features = [
  { anchor = "refined-education", level = 1 },
  { anchor = "broad-education" },
  { anchor = "social-sense", level = 3 },
  { anchor = "master-of-all", level = 20 },
]
trades = [
  { replaces = "Debilitating injury", by = ["refined-education"] },
  { replaces = "sneak attack", feature = "sneak-attack", by = ["refined-education"] },
  { replaces = "trapfinding", feature = "trapfinding", by = ["refined-education"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["social-sense"] },
  { replaces = "Master strike", feature = "master-strike", by = ["master-of-all"] },
  { alters = "Rogue's edge", by = ["refined-education"] },
  { alters = "Rogue talent", feature = "rogue-talents", by = ["broad-education"] },
  { alters = "Class skills", by = ["refined-education"] },
]
+++

Also known as gentleman thieves or lady thieves, phantom thieves don't know the desperation of a
hard life like many rogues. Instead, they come from the ranks of the elite, having grown bored with
their finery, and seek thrills from acts of daring, skill, and crime. Phantom thieves don't need the
money, so they often perform acts such as breaking into a secure vault for the thrill, leaving a
calling card rather than robbing the place.

## Refined Education (Ex) {#refined-education}

A phantom thief adds Handle Animal, Heal, Ride, Spellcraft, Survival, and all Knowledge skills to
her list of class skills. Furthermore, she selects one of her rogue class skills and adds half her
rogue level on all skill checks using that skill. At 3rd level and every 2 rogue levels thereafter,
she selects an additional rogue class skill and adds half her rogue level on all skill checks using
that skill as well. Starting at 4th level, if the phantom thief is an unchained rogue, she gains
rogue's edge skill unlocks with each of these skills rather than selecting one skill every 5 levels,
and she adds half her rogue level to her number of ranks to determine when she receives a skill
unlock (so a 7th level rogue (phantom thief) with 7 ranks in a chosen skill would count as having 10
ranks and receive the second skill unlock).

This ability alters the rogue's class skills and replaces sneak attack and trapfinding. For an
unchained rogue, it also alters rogue's edge and replaces debilitating injury.

## Broad Education (Ex) {#broad-education}

A phantom thief's broad studies with expensive tutors keep her up to speed in both martial and
magical knowledge, as well as in her skills. She can select the
[combat trick](ref/talent/combat-trick), [minor magic](ref/talent/minor-magic), and
[major magic](ref/talent/major-magic) rogue talents as many times as she likes, and she can select
the [Skill Focus](ref/feat/skill-focus) feat as a rogue talent, also as many times as she likes.
Finally, she can select a vigilante social talent instead of a rogue talent, except for social grace
and vigilante social talents that would require her to be a craftsman or professional. For the
purpose of vigilante social talents, a phantom thief does not have a vigilante identity and is
always considered to be in her social identity.

This ability alters rogue talent.

## Social Sense (Ex) {#social-sense}

At 3rd level, a phantom thief's social sixth sense allows her to avoid danger in social situations
and to act first when it breaks out. She receives a +1 bonus on Sense Motive checks to avoid being
surprised by a foe, on Bluff checks to surprise a foe, and on initiative checks for surprise rounds
that involved Bluff and Sense Motive checks to determine surprise. This bonus increases by 1 at 3rd
level and every 3 rogue levels thereafter.

This ability replaces trap sense.

## Master of All (Ex) {#master-of-all}

At 20th level, a phantom thief can reroll any skill check as long as it is a class skill in which
she is trained. She must take the second result, even if it is worse. She can use this ability no
more than once per minute.

This ability replaces master strike.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the phantom thief archetype: combat trick, major magic, minor
magic (as well as certainty for an unchained rogue).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the phantom thief archetype: feat, hidden mind,
rumormonger, and skill mastery (as well as cutting edge for an unchained rogue).
