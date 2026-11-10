+++
id = "ref/arc-vigilante/darklantern"
kind = "archetype"
title = "Darklantern"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Darklantern"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darklantern", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "11"

[fields]
kind = "archetype"
replaces = ["1st-level social talent", "Vigilante talent gained at 4th level"]
alters = ["Dual identity"]
alters_features = ["dual-identity"]
+++

The [Lantern Bearers](ref/rule/aff-lights) are an elite group of elves dedicated to the containment
and eradication of the drow. However, some Lantern Bearers are tasked with the unthinkable
assignment of infiltrating drow society so as to relay information to the Winter Council - a secret
cabal tasked with keeping the existence of drow a secret - about activities in the Darklands and
drow cities. In order to accomplish this task, select members of the Lantern Bearers undergo a
horrific ritual allowing them to temporarily experience the dark transformation into a drow, but at
the cost of their sanity.

**Prerequisites:** Must be a creature with the [elf](ref/subtype/elf) subtype

**Dark Identity (Su)**

**Ability:** A darklantern can transform into her vigilante identity as a **full-round action**.
When a darklantern switches to her vigilante identity, she undergoes a horrifying transformation
from an elf into a [drow](ref/race/drow). After the transformation is complete, the darklantern
takes on the appearance of a drow (but otherwise retains her normal facial features and voice) and
gains a +2 bonus to Dexterity and Charisma, [darkvision](ref/rule/darkvision) with a range of up to
60 feet, and the [light blindness](ref/umr/light-blindness) universal monster ability. While in her
vigilante identity, the darklantern counts as a drow for the purpose of any ability, spell, or magic
item targeting drow.

**Ability2:** Transforming back into the darklantern's social identity requires a **move action**.
However, a darklantern must succeed at a Will save (DC = 10 + the number of hours she has been in
her vigilante identity) in order to successfully transform back into her social identity; otherwise,
the move action is wasted and the action cannot be attempted for 1 minute. Each time a darklantern
fails this check, she takes 1 point of [Wisdom damage](ref/rule/ability-damage-drain) and the DC for
the save decreases by 2.

**Alters:** Dual identity

**Info:** A darklantern's vigilante identity must be chaotic evil, but her social identity can be
more than one step removed from this alignment.

**Gained:** At 1st Level

**Drow Magic (Sp)**

**Ability:** When in her vigilante identity, a darklantern can cast
[dancing lights](ref/spell/dancing-lights), [darkness](ref/spell/darkness), and
[faerie fire](ref/spell/faerie-fire), once each per day, using her vigilante level as her caster
level.

**Gained:** At 1st Level

**Replaces:** 1st-level social talent

**Drow Paragon (Su)**

**Gained:** At 4th Level

**Passive:** The darklantern gains [Spell Resistance](ref/rule/spell-resistance) equal to 6 + her
vigilante level, and the range of her [darkvision](ref/rule/darkvision) increases to 120 feet while
in her vigilante identity.

**Replaces:** Vigilante talent gained at 4th level
