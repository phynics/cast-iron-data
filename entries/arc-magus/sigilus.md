+++
id = "ref/arc-magus/sigilus"
kind = "archetype"
title = "Sigilus"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sigilus", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "adventurers-guide"
page = "59"

[fields]
kind = "archetype"
replaces = ["Spellstrike", "Medium armor", "heavy armor"]
replaces_features = ["spellstrike", "medium-armor", "heavy-armor"]
+++

Traditionally, the [Cyphermages](ref/rule/aff-i-tradition) have harbored something of a resistance
toward physical combat, preferring to rely upon the power of magic to solve problems and defeat
foes. Many of the organization's traditionalists hold prejudices against those who rely upon martial
skills, and this prejudice has bled over to those who mix magic with combat, such as
[eldritch knights](ref/pclass/eldritch-knight) and magi. With the organization's recent change to
its traditions, though, its numbers have grown more welcoming of these traditions, and magi in
particular, have developed a unique method of incorporating their lore.

When a magus joins the ranks of the Cyphermages, she can learn the art of infusing her _arcane pool_
with the secrets of ancient Thassilonian magic. Such an individual becomes known as a sigilus. While
the mysteries of ancient Thassilon drive her spellcraft, the sigilus makes little effort to
understand the academic and philosophic aspects of runes. Instead, she focuses almost entirely upon
their practical application.

A sigilus manipulates the discoveries of wizards and other more sagacious Cyphermages, using those
findings to create special sigils that allow her to transfer spell effects into different objects
for later use. Her craft builds upon traditions founded by the runelords that allowed them to infuse
magic into their flesh, but rather than infusing magic into her body, the sigilus infuses it into a
weapon. More interested in the exploration of Thassilonian ruins than academic research, sigiluses
serve the Cyphermages by engaging in fieldwork and recovering artifacts. They work alongside more
studious Cyphermages, sometimes serving as bodyguards or as regulatory agents who make sure no
member gains too much power through the acquisition of potent Thassilonian secrets.

**Inscribe Rune (Su)**

**Action:** Ability

**Gained:** At 2nd Level

**Replaces:** Spellstrike

A sigilus learns how to magically inscribe a Thassilonian rune onto a weapon. The rune to be
inscribed must be chosen from the seven runes that symbolize the seven schools of Thassilonian magic
(see [Thassilonian Magic](ref/arcaneschool/thassilonian-magic) for a list). Note that due to the
nature of magus spells, certain runes (and thus certain schools of magic) are more appropriate for
inscription than others - the runes for conjuration, evocation, illusion, and transmutation are the
strongest choices, while those for abjuration, enchantment, and necromancy are less enticing.
Inscribing a rune takes 10 minutes.

Once a weapon has been infused with a rune, the sigilus becomes more adept at using her _spell
combat_ ability with spells of that rune's school. Her penalty on attack rolls when using _spell
combat_ is reduced by 1 (to -1) when she casts a spell from the same school as her inscribed rune,
but is increased by 2 (to -4) when she uses _spell combat_ with a spell not from her inscribed
rune's school. As long as she has a rune inscribed on her weapon in this manner, she cannot use
spells from that rune's opposition schools at all with _spell combat._

The sigilus can maintain only a single inscribed rune on a weapon at any time; if she inscribes a
new rune on a weapon, the previously inscribed rune fades.

**Inscribe Sihedron (Su)**

**Ability:** A sigilus learns to inscribe the Sihedron rune (the seven-pointed star that symbolizes
all seven schools of Thassilonian magic) on a suit of light armor she wears. When she does so, her
armor becomes physically empowered with defensive magic, granting her energy
[resistance](ref/umr/resistance) 5 to two energy types of her choice selected from acid, cold, fire,
electricity, or sonic, and increasing the armor's armor bonus by 1. (Note that this increase is an
armor bonus increase, and thus stacks with any enhancement bonus a suit of magic light armor may
have.) Inscribing the Sihedron rune in this way becomes part of the sigilus's spell preparation
ritual - she can inscribe a Sihedron rune in this way once per day as a result. Each day she
inscribes the Sihedron rune, she can change the two types of energy resistance it grants as she
wishes.

**At 13th Level:** An inscribed Sihedron rune grants energy resistance 10 to one energy type and
energy resistance 5 to two other energy types, and its armor bonus increases to +2.

**Gained:** At 7th Level

**Replaces:** Medium armor, heavy armor

**Special:** A Sihedron rune can be inscribed only on light armor - it cannot be inscribed on medium
or heavy armor, even if the magus later gains proficiency with medium or heavy armor.
