+++
id = "ref/arc-cavalier/first-mothers-fang"
kind = "archetype"
title = "First Mother's Fang"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20First%20Mother%27s%20Fang"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "first_mothers_fang", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "serpent-mount" },
  { anchor = "honored-warrior", level = 1 },
]
trades = [
  { replaces = "Order", feature = "order", by = ["honored-warrior"] },
  { alters = "The cavalier's weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { alters = "Mount", feature = "mount", by = ["serpent-mount"] },
  { alters = "Class skills" },
]
+++

Nagajor legend states that when [Nalinivati](ref/faith/nalinivati) created the first
[nagaji](ref/race/nagaji), she chose a paragon of their kind to instruct in the use of exotic
weapons, lore, and words so the creature could best serve her as a bodyguard and emissary: the
original first mother's fang. Whether or not these paragons descend from a single nagaji, first
mother's fangs of Nagajor have expanded their numbers over the generations, and they no longer speak
with the full authority of the First Mother. In modern times, a first mother's fang acts as a
servant of his nation, a skilled general and tactician in times of war and a noble governor during
times of peace.

## Class Skills {#class-skills}

A first mother's fang adds all Knowledge skills to his list of class skills.

This alters the cavalier's class skills.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A first mother's fang is proficient with all simple and martial weapons. Additionally, a first
mother's fang is proficient in one exotic melee weapon of his choice and one exotic ranged weapon of
his choice.

This alters the cavalier's weapon proficiencies.

## Serpent Mount (Ex) {#serpent-mount}

Instead of the usual choices for a cavalier's mount, first mother's fangs ride on giant riding
constrictors. These use the statistics of the [constrictor snake](ref/companion/snake-constrictor)
druid animal companion, except that they are suitable mounts and begin as size Large at 1st level
with no other adjustments to their abilities or statistics based on this size change. A serpent
mount is considered to be a quadruped for the purpose of determining its
[carrying capacity](ref/rule/carrying-capacity), and its base land speed is 40 feet (other speeds
are unaffected). At 4th level, a giant riding constrictor doesn't increase in size again, but it
does receive all the other usual 4th-level benefits.

This alters mount.

## Honored Warrior (Ex) {#honored-warrior}

A first mother's fang is expected to act as a military leader in wartime and a governor in peace
time, and as a result, he must be versed both in the martial and political arts. At 1st level, he
gains [Combat Expertise](ref/feat/combat-expertise) as a bonus feat, and if his Intelligence score
is less than 13, it counts as 13 for the sole purpose of meeting the prerequisites of combat feats
that require Combat Expertise as a prerequisite.

At 2nd, 8th, and 15th levels, the first mother's fang gains a [vigilante](ref/class/vigilante)
social talent and a bonus combat feat. When selecting his vigilante social talent, a first mother's
fang can select [celebrity discount](ref/soctalent/celebrity-discount),
[celebrity perks](ref/soctalent/celebrity-perks), [great renown](ref/soctalent/great-renown),
[incredible renown](ref/soctalent/incredible-renown),
[instant recognition](ref/soctalent/instant-recognition), [loyal aid](ref/soctalent/loyal-aid),
[renown](ref/soctalent/renown), [social grace](ref/soctalent/social-grace), or
[triumphant return](ref/soctalent/triumphant-return). He treats his cavalier level as his effective
vigilante level when determining whether he meets a talent's prerequisites, as well as its effects.
He gains the improved attitude and Intimidate bonuses from renown as if he were in both social and
vigilante identities. When selecting skills with social grace, he must choose from the following
list: Appraise, Bluff, Diplomacy, Intimidate, Knowledge (geography, history, local, or nobility),
Perform, Profession (soldier), or Sense Motive. He is always considered to be in his social identity
for the purpose of social grace (though he continues to receive the benefits for both identities
from renown). When selecting his bonus combat feat, he can choose from only combat feats that list
Combat Expertise as a prerequisite.

This ability replaces order.
