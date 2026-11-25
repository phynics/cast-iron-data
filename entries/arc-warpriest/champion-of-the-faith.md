+++
id = "ref/arc-warpriest/champion-of-the-faith"
kind = "archetype"
title = "Champion of the Faith"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Champion%20of%20the%20Faith"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "champion_of_the_faith", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "advanced-class-guide"
page = "128"

[fields]
kind = "archetype"
features = [
  { anchor = "chosen-alignment", level = 1 },
  { anchor = "sacred-weapon", level = 1 },
  { anchor = "detect-alignment", level = 3 },
  { anchor = "smite", level = 4 },
]
trades = [
  { replaces = "Bonus feat gained at 3rd level", feature = "bonus-feats", levels = [3], by = ["detect-alignment"] },
  { replaces = "Channel energy", feature = "channel-energy", by = ["smite"] },
  { alters = "Sacred weapon", feature = "sacred-weapon", by = ["sacred-weapon"] },
]
+++

Champions of the faith are crusaders who use the power of their divine patron to annihilate the
faith's enemies.

## Chosen Alignment {#chosen-alignment}

At 1st level, a champion of the faith must select one of the following as his chosen alignment:
chaos, evil, good, or law. This choice must be one of the alignments shared by the champion of the
faith and his deity. Champions of the faith who are neutral with no other alignment components (or
whose deity is) can choose any of the above alignments for this purpose. Additionally, a champion of
the faith must select the blessing corresponding to his chosen alignment, even if it's not on his
deity's list of domains.

His chosen alignment's opposite is referred to as his opposed alignment. Good and evil oppose one
another, just as law and chaos oppose one another.

## Sacred Weapon (Su) {#sacred-weapon}

At 1st level, a champion of the faith gains the sacred weapon class feature as normal. However, this
ability does not grant the 4th-level ability to enhance the champion of the faith's weapon with
divine power, nor does it grant any subsequent increases to that ability. Instead, at 4th level, any
sacred weapon wielded by a champion of the faith counts as having his chosen alignment for the
purposes of overcoming [damage reduction](ref/rule/damage-reduction).

At 12th level, once per day as a swift action, a champion of the faith can enhance any one sacred
weapon with a weapon special ability based on his chosen alignment
(_[anarchic](ref/magic-enh/anarchic)_ for chaos, _[unholy](ref/magic-enh/unholy)_ for evil,
_[holy](ref/magic-enh/holy)_ for good, and _[axiomatic](ref/magic-enh/axiomatic)_ for law). This
effect lasts for 1 minute. He can use this ability one additional time per day at 16th and 20th
levels. This ability alters sacred weapon.

## Detect Alignment (Sp) {#detect-alignment}

At 3rd level, a champion of the faith can detect his opposed alignment. As a move action, the
champion of the faith can focus on a single item or creature within 60 feet and determine whether it
possesses the opposed alignment, as _[detect chaos/evil/good/law](ref/spell/detect-evil)_, learning
the strength of the aura as if he had studied it for 3 rounds. The champion of the faith does not
detect alignment in any other object or creature when using this ability in this way. This ability
replaces the bonus feat gained at 3rd level.

## Smite (Su) {#smite}

At 4th level, a champion of the faith can focus his powers against his chosen foes. As a swift
action, the champion of the faith chooses one target within sight to smite. If this target is of his
opposed alignment, the champion of the faith adds his Charisma bonus (if any) to his attack rolls
and adds his warpriest level to all damage rolls made against the target of his smite. If the target
of his smite is an [outsider](ref/type/outsider) with the subtype corresponding to his opposed
alignment, the bonus to damage on the first successful attack increases to 2 points of damage per
warpriest level the champion of the faith possesses. Regardless of the target, smite attacks
automatically bypass any DR the target possesses.

In addition, while smite is in effect, the champion of the faith gains a deflection bonus equal to
his Charisma modifier (if any) to his AC against attacks made by the target of the smite. If the
smite targets a creature that's not of the champion of the faith's opposed alignment, the smite is
wasted with no effect.

The smite effect remains until the target of the smite is dead or the next time the champion of the
faith regains spells. The champion of the faith can use this ability once per day, plus one
additional time per day for every 4 levels beyond 4th (to a maximum of five times per day at 20th
level). Using this ability consumes two uses of his fervor ability. This ability replaces channel
energy.
