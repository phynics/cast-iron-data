+++
id = "ref/arc-investigator/spiritualist"
kind = "archetype"
title = "Spiritualist"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Spiritualist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spiritualist", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "advanced-class-guide"
page = "102"

[fields]
kind = "archetype"
features = [
  { anchor = "commune-with-spirits" },
  { anchor = "spirit-sense", level = 2 },
  { anchor = "strong-life", level = 2 },
  { anchor = "sixth-sense", level = 3 },
  { anchor = "whispering-spirits", level = 4 },
  { anchor = "touched-by-the-beyond", level = 11 },
]
trades = [
  { replaces = "Alchemy", feature = "alchemy", by = ["commune-with-spirits"] },
  { replaces = "Poison lore", feature = "poison-lore", by = ["spirit-sense"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["strong-life"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["sixth-sense"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["whispering-spirits"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [11], by = ["touched-by-the-beyond"] },
]
+++

While most investigators look to the physical world to gain their knowledge, there are those who
seek out knowledge beyond the pale. Those who think that the dead tell no tales are quickly proven
wrong by the spiritualist. Instead of toying with chemicals and reagents to find clues, he talks
directly to the spirit world to uncover the ways and means of skullduggery and the desperate acts
committed in the heat of dark passions.

## Commune with Spirits (Sp) {#commune-with-spirits}

Instead of relying on alchemical research to find clues, a spiritualist relies on communion with the
world beyond death. At 1st level, a spiritualist gains the ability to use
_[comprehend languages](ref/spell/comprehend-languages)_,
_[detect secret doors](ref/spell/detect-secret-doors)_, and _[identify](ref/spell/identify)_, but
each has a casting time of 1 minute, as the spiritualist needs to consult with the spirits of the
dead that dwell in his area or that are somehow attached to him in some way. The spiritualist can
use this ability a number of times per day equal to his investigator level + his Wisdom modifier.

As he goes up in level, the spiritualist gains the ability to use other spells with the casting time
as above. At 5th level, he can use _[augury](ref/spell/augury)_. At 7th level, he can use
_[speak with dead](ref/spell/speak-with-dead)_ and _[locate object](ref/spell/locate-object)_. At
9th level, he can use _[legend lore](ref/spell/legend-lore)_. Each of these requires one use of this
ability.

This ability replaces alchemy. A spiritualist cannot take the
[alchemist discovery](ref/invtalent/alchemist-discovery) talent or any investigator talent that
affects alchemy.

## Spirit Sense (Su) {#spirit-sense}

At 2nd level, when a spiritualist attempts a saving throw against an ability or an effect delivered
by an incorporeal creature, he can expend one use of his inspiration instead of two to augment that
saving throw. If the spiritualist has the [combat inspiration](ref/invtalent/combat-inspiration)
investigator talent, he need not spend any inspiration to augment such saving throws. This ability
replaces poison lore.

## Strong Life (Ex) {#strong-life}

At 2nd level, his dealings with the other side and knowledge of what lies beyond strengthens the
spiritualist's will. He gains a +2 bonus on saving throws against death effects and negative energy
damage. This bonus increases to +4 at 5th level, and to +6 at 8th level. This ability replaces
poison resistance.

## Sixth Sense (Su) {#sixth-sense}

At 3rd level, a spiritualist can spend one of his uses of the commune with spirits ability to reroll
a single saving throw that he has failed. He must take the results of the reroll, even if it is
lower. This ability replaces trap sense.

## Whispering Spirits (Su) {#whispering-spirits}

At 4th level, the spiritualist can open a conduit with the spirit world that can aid him in combat
for a short time. He can expend one use of his commune with spirits ability in order to gain an
insight bonus to both AC and saving throws equal to his Wisdom modifier (minimum 1) for 1 minute.
This ability replaces swift alchemy.

## Touched by the Beyond (Su) {#touched-by-the-beyond}

At 11th level, the spiritualist's ability to touch the beyond grants him further protection against
the dangers of death and negative energy. The spiritualist becomes immune to death effects, and he
takes half damage from negative energy. This ability replaces poison immunity.

## Investigator Talents {#investigator-talents}

The following investigator talents complement the spiritualist archetype:
[amazing inspiration](ref/invtalent/amazing-inspiration),
[combat inspiration](ref/invtalent/combat-inspiration),
[effortless aid](ref/invtalent/effortless-aid),
[eidetic recollection](ref/invtalent/eidetic-recollection), [empathy](ref/invtalent/empathy),
[expanded inspiration](ref/invtalent/expanded-inspiration),
[hidden agendas](ref/invtalent/hidden-agendas),
[inspirational expertise](ref/invtalent/inspirational-expertise),
[item lore](ref/invtalent/item-lore), [studied defense](ref/invtalent/studied-defense), and
[tenacious inspiration](ref/invtalent/tenacious-inspiration).
