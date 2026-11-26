+++
id = "ref/arc-investigator/natural-philosopher"
kind = "archetype"
title = "Natural Philosopher"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Natural%20Philosopher"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "natural_philosopher", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "56"

[fields]
kind = "archetype"
features = [
  { anchor = "natural-philosopher-s-inspiration", level = 1 },
  { anchor = "track", level = 1 },
  { anchor = "herbalism", level = 3 },
]
trades = [
  { replaces = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Trapfinding", feature = "trapfinding", by = ["track"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["herbalism"] },
  { replaces = "investigator talent gained at 3rd level", feature = "investigator-talent", levels = [3], by = ["herbalism"] },
  { alters = "Inspiration", feature = "inspiration", by = ["natural-philosopher-s-inspiration"] },
  { alters = "Alchemy", feature = "alchemy", by = ["herbalism"] },
  { alters = "Class skills" },
]
+++

Natural philosophers are scholars, explorers, and survivalists who feel at home in nature, seldom
longing for the comforts of the city.

They eschew the fancy tools and weaponry of gentlefolk detectives and instead employ weapons that
double as tools, materials available in nature, and methods better suited for untamed wilderness.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A natural philosopher is proficient with simple weapons, plus the [handaxe](ref/eq-weapon/handaxe),
[kukri](ref/eq-weapon/kukri), [shortbow](ref/eq-weapon/shortbow),
[throwing axe](ref/eq-weapon/throwing-axe), and [whip](ref/eq-weapon/whip). A natural philosopher is
proficient with light armor but not with shields.

This replaces the investigator's weapon and armor proficiency.

## Class Skills {#class-skills}

A natural philosopher gains Survival as a class skill, but doesn't gain Perform as a class skill.

This alters the investigator's class skills.

## Natural Philosopher's Inspiration (Ex) {#natural-philosopher-s-inspiration}

Natural philosophers employ a skill set suited to studying the natural world. A natural philosopher
can use inspiration on Heal and Survival checks without expending a use of inspiration, provided he
is trained in the skill, but cannot do so for Linguistics or Spellcraft checks. He can later trade
an investigator talent for the ability to use inspiration on Linguistics and Spellcraft checks
without expending a use of inspiration, provided he is trained in the skill.

This alters inspiration.

## Track (Ex) {#track}

A natural philosopher adds half his level (minimum 1) on Survival checks to follow tracks.

This replaces trapfinding.

## Herbalism (Su) {#herbalism}

At 3rd level, a natural philosopher augments his knowledge of alchemy with herbal lore. He gains the
[infusion](ref/discovery/infusion) discovery and can use Knowledge (nature) in place of Craft
(alchemy) and [Profession (herbalist)](ref/skill/profession-any) checks. He also gains a competence
bonus equal to his class level on Craft (alchemy) checks to create alchemical items, and he gains
half that bonus on Profession (herbalist) checks to find herbs (for more information on herbalism,
see page 152).

This alters alchemy and replaces trap sense and the investigator talent gained at 3rd level.
