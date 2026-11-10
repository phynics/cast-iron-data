+++
id = "ref/arc-investigator/gravedigger"
kind = "archetype"
title = "Gravedigger"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gravedigger", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "horror-adventures"
page = "54"

[fields]
kind = "archetype"
replaces = ["Weapon and armor proficiencies", "Trapfinding", "trap sense", "Poison resistance", "poison immunity", "Poison lore", "Swift alchemy"]
alters = ["Alchemy", "investigator talents", "Investigator talents", "Studied combat", "studied strike"]
+++

Gravediggers pursue long buried mysteries, figuratively and literally digging up the truth and
finding answers to secrets only moldering corpses and dry bones can tell.

**Weapon and Armor Proficiency**

**Info:** A gravedigger is proficient with simple weapons and [scythes](ref/eq-weapon/scythe), and
can fight with gravediggers' tools such as a shovel or lantern as if she had the
[Catch Off-Guard](ref/feat/catch-off-guard) feat. A gravedigger is proficient with light armor, but
not with shields.

**Replaces:** Weapon and armor proficiencies

**Limited Alchemy**

**Ability:** A gravedigger prepares and uses extracts as an investigator but gains no other benefits
of the _alchemy_ ability. This also means that a gravedigger can't take the
[alchemist discovery](ref/invtalent/alchemist-discovery) investigator talent or any discovery that
affects or involves alchemy.

**Alters:** Alchemy, investigator talents

**Grave Magic (Sp)**

**Ability:** A gravedigger can sacrifice unused extract slots of the level given below or higher to
use the following spells as [spell-like abilities](ref/umr/spell-like-abilities), using her
investigator level as her caster level and her Intelligence to determine DCs.

**Spells:** Expeditious excavation

**Spells:** Calm spirit

**Spells:** Speak with dead

**Spells:** Rest eternal

**Spells:** Call spirit

**Spells:** Undeath to death

**Relic Focus (Su)**

**Ability:** A gravedigger can form a psychic bond with a skull or bone that she has personally
exhumed or recovered from a burial site, using it as an [occultist](ref/class/occultist)
[necromancy implement](ref/implement/necromancy) and gaining its base focus power. The gravedigger
cannot invest mental focus into the implement and thus doesn't receive any resonant powers. However,
she can expend one use of _inspiration_ to use any focus power she knows that has a cost of 1 point
of mental focus. She can do this a number of times each day equal to 1 +
[one-third](ref/misc/fractions-and-rounding) of her investigator level.

**Replaces:** Trapfinding, trap sense

**Special:** To activate a focus power that costs more than 1 point of mental focus, the gravedigger
can expend that number of daily uses of this ability (as well as uses of _inspiration_) at the same
time. In addition, any number of times per day, she can expend 1 use of _inspiration_ to use
[grave words](ref/spell/grave-words) as a [spell-like ability](ref/umr/spell-like-abilities).

**Deny Death (Ex)**

**Gained:** At 2nd Level

**Passive:** A gravedigger gains a +2 bonus on all saving throws against death effects and
[energy drain](ref/rule/energy-drain-and-negative-levels).

**Replaces:** Poison resistance, poison immunity

**Read the Bones (Su)**

**Ability:** A gravedigger can perform _[object reading](ref/spell/object-reading)_ as an occultist,
but only on corpses, bones, and other physical remains.

**Gained:** At 2nd Level

**Replaces:** Poison lore

**Focus Talent (Su)**

**Ability:** A gravedigger can select a focus power for one of her implements as per an occultist of
her investigator level in place of an investigator talent.

**Alters:** Investigator talents

**Kill the Dead (Ex)**

**Alters:** Studied combat, studied strike

**Info:** A gravedigger focuses on battling the undead, and her _studied combat_ and _studied
strike_ function as if she were 2 levels lower against creatures other than undead (this means she
can't use them at all against such creatures until 6th level).

**Grave Lamp (Su)**

**Ability:** A gravedigger can form a psychic bond with a lantern, using it as a
[conjuration](ref/implement/conjuration) implement in much the same way as she uses her _relic
focus_ as a necromancy implement. She can expend _inspiration_ to fuel her grave lamp's focus powers
the same number of times each day as she can for her _relic focus_ (for example, a 6th-level
gravedigger with 6 points of _inspiration_ could expend up to three uses of _inspiration_ as mental
focus for her _relic focus_ and up to three uses of _inspiration_ as mental focus for her grave
lamp).

**Gained:** At 4th Level

**Replaces:** Swift alchemy
