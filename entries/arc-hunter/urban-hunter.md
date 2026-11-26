+++
id = "ref/arc-hunter/urban-hunter"
kind = "archetype"
title = "Urban Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Urban%20Hunter"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urban_hunter", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-companion", level = 1 },
  { anchor = "captor", level = 3 },
  { anchor = "animal-insight", level = 5 },
  { anchor = "frightful-ferocity", level = 17 },
]
trades = [
  { replaces = "Hunter tactics", feature = "hunter-tactics", by = ["captor"] },
  { replaces = "teamwork feat", feature = "teamwork-feat", by = ["captor"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["animal-insight"] },
  { replaces = "One with the wild", feature = "one-with-the-wild", by = ["frightful-ferocity"] },
  { alters = "Animal companion", feature = "animal-companion", by = ["animal-companion"] },
  { alters = "Class skills" },
]
+++

Urban hunters help guards track down and apprehend criminals or spies, find lost children and
disaster victims, and protect animals from abuse in the city. They still draw their inspiration and
strength from the natural world, marveling at how nature flourishes wherever the city allows.

## Class Skills {#class-skills}

An urban hunter adds Diplomacy (Cha), Knowledge (local) (Int), and Sense Motive (Wis) as class
skills, and removes Knowledge (nature) (Int) and Survival (Wis). This alters the hunter's class
skills.

## Animal Companion (Ex) {#animal-companion}

Urban hunters have animal companions that are domesticated animals or animals native to a major
city. The urban hunter must select her animal companion from the following list:
[axe beak](ref/companion/axe-beak), [badger](ref/companion/badger), [bird](ref/companion/bird),
[camel](ref/companion/camel), [dire rat](ref/companion/dire-rat), [dog](ref/companion/dog),
[horse](ref/companion/horse), [llama](ref/companion/llama), [ostrich](ref/companion/ostrich),
[pony](ref/companion/pony), [ram](ref/companion/ram), or
[trumpeter swan](ref/companion/swan-trumpeter). In urban settings, an urban hunter's animal
companion seems domesticated and likely harmless to anyone who has not seen it in combat
(potentially reducing the DC of Diplomacy checks to convince anyone to allow it into secure areas).
It draws no more attention than a friendly dog, loyal horse, or similar tame animal.

Creatures who have never seen the animal companion make an attack must succeed at a Sense Motive
check (opposed by the animal companion's Stealth check) to realize the animal companion is a
potential threat. The hunter can calm those who witness her animal companion's attacks (so long as
they were not injured) with a successful Handle Animal check (DC = 15 + the target's Will save
modifier).

## Captor (Ex) {#captor}

At 3rd level, an urban hunter and her animal companion take no penalties when dealing nonlethal
damage with weapons or natural attacks. At 6th level and every 3 levels thereafter, the urban hunter
selects a bonus feat from the following list to be gained by both the hunter and her animal
companion: [Improved Bull Rush](ref/feat/improved-bull-rush),
[Improved Dirty Trick](ref/feat/improved-dirty-trick), [Improved Disarm](ref/feat/improved-disarm),
[Improved Grapple](ref/feat/improved-grapple), and [Improved Trip](ref/feat/improved-trip). At 12th
level, the hunter can also select from the following feats: [Combat Patrol](ref/feat/combat-patrol),
[Combat Reflexes](ref/feat/combat-reflexes), [Disarming Strike](ref/feat/disarming-strike),
[Greater Bull Rush](ref/feat/greater-bull-rush),
[Greater Dirty Trick](ref/feat/greater-dirty-trick), [Greater Disarm](ref/feat/greater-disarm),
[Greater Grapple](ref/feat/greater-grapple), [Greater Trip](ref/feat/greater-trip), and
[Lunge](ref/feat/lunge). Neither the hunter nor her animal companion needs to meet the prerequisites
for these bonus feats. This ability replaces hunter tactics and teamwork feat.

## Animal Insight (Ex) {#animal-insight}

At 5th level, an urban hunter and her animal companion learn to combine their insights to defeat
deception and manipulation. As long as they are within 30 feet of each other, both hunter and animal
companion gain an insight bonus on Sense Motive checks equal to half the urban hunter's hunter
level. They also gain a +2 insight bonus on Will saving throws against illusions and mind-affecting
effects. This ability replaces woodland stride.

## Frightful Ferocity (Ex) {#frightful-ferocity}

At 17th level, an urban hunter and her animal companion can each attempt an Intimidate check to
demoralize a foe as a swift action. This ability replaces one with the wild.
