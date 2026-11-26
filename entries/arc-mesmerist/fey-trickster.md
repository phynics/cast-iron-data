+++
id = "ref/arc-mesmerist/fey-trickster"
kind = "archetype"
title = "Fey Trickster"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Fey%20Trickster"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fey_trickster", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "37"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-s-lure" },
  { anchor = "feytouched", level = 2 },
  { anchor = "fey-veil", level = 3 },
  { anchor = "one-with-the-fey", level = 20 },
]
trades = [
  { replaces = "Towering ego", feature = "towering-ego", by = ["feytouched"] },
  { replaces = "Touch treatment", feature = "touch-treatment", by = ["fey-veil"] },
  { replaces = "Rule minds", feature = "rule-minds", by = ["one-with-the-fey"] },
  { alters = "Spellcasting", feature = "spells", by = ["nature-s-lure"] },
  { alters = "Class skills" },
]
+++

Most mesmerists draw psychic power from the Astral Plane, but a few gain their powers in an unusual
way: from a brush with the fey. Prisoner-guests of the fey, these souls find themselves changed when
they return to the mortal world, infused with the eldritch energy of their former hosts.

## Class Skills {#class-skills}

A fey trickster adds Handle Animal, Knowledge (nature), and Survival to her list of class skills,
instead of Appraise, Knowledge (dungeoneering), and Profession.

This alters the mesmerist's class skills.

## Nature's Lure {#nature-s-lure}

Rather than casting psychic spells from the mesmerist spell list, a fey trickster casts divine
spells drawn from the druid and ranger spell lists, in just the same way as a hunter does. This
means that she gains orisons instead of knacks. This doesn't change her number of spells per day or
spells known. The fey trickster's mesmerist spells and
[spell-like abilities](ref/umr/spell-like-abilities) count as if they were fey spell-like abilities
for the purpose of effects like resist nature's lure that apply against fey spell-like abilities.

This alters the mesmerist's spellcasting.

## Feytouched (Ex) {#feytouched}

At 2nd level, a [fey](ref/type/fey) trickster's time with the fey has granted her strange powers, as
well as resistance to further fey mischief. The fey trickster gains the druid's
[resist nature's lure](ref/ability/resist-natures-lure) and
[woodland stride](ref/ability/woodland-stride) abilities, and she counts as both fey and her
original creature type for the purpose of spells and effects.

This ability replaces towering ego.

## Fey Veil (Sp, Su) {#fey-veil}

At 3rd level, a fey trickster's physical form begins to shift, as she gains some of the impossible
allure of the fey. At the same time, she begins able to use fey veils to assist herself and her
allies in befuddling and bewitching their opponents. She can use her fey veils a number of times per
day equal to 3 + her Charisma modifier.

Using the ability is a standard action (or a swift action if the fey trickster calls up a
[veil](ref/spell/veil) over herself). If she targets another ally, the fey trickster must be able to
contact the ally bodily, usually with a kiss. When she uses her fey [veil](ref/spell/veil), the fey
trickster subtly alters the appearance and aura of her target, granting one of the powers allowed by
her mesmerist level.

At 3rd level, she can grant the ally a +2 circumstance bonus on her choice of Diplomacy, Intimidate,
or Handle Animal checks for 1 minute. At 6th level, she can change the ally's form so thoroughly
that the ally gains a +10 bonus on Disguise checks until the next sunrise (similar to the bonus from
_[disguise self](ref/spell/disguise-self)_, but it also disguises touch and sound, and it doesn't
allow a saving throw to disbelieve). At 10th level, the fey trickster can make the ally and her aura
so attractive or repulsive for 10 minutes that the [veil](ref/spell/veil) automatically adjusts the
moods of those who see the ally and fail their saving throw, as
_[telempathic projection](ref/spell/telempathic-projection)_. At 14th level, a fey trickster can
create a veil so powerful that it fools even reality, granting the full effects of both the
6th-level fey veil and _[alter self](ref/spell/alter-self)_ to the target for 1 hour. Each of these
abilities, even the 14th-level ability, is an illusion and glamer effect, though the last ability
counts as a size-changing [polymorph](ref/spelldef/polymorph) effect for the limit of only one
polymorph or size-changing effect on a creature.

This ability replaces touch treatment.

## One with the Fey {#one-with-the-fey}

At 20th level, a fey trickster fully transforms into a fey, though she can still choose to count as
her original creature type as well whenever it would be advantageous to her (such as if she is a
humanoid and wishes to be affected by _[reduce person](ref/spell/reduce-person)_). She gains
[low-light vision](ref/rule/low-light-vision) as well as an additional ability depending on which
type of fey she chooses to most closely associate with. Some examples follow.

### Erlking {#erlking}

The fey trickster is constantly under the effects of _[haste](ref/spell/haste)_.

### Nymph {#nymph}

The fey trickster gains the [nymph's](ref/monster/nymph) unearthly grace ability (_Pathfinder RPG
Bestiary_ 217)

### Quickling {#quickling}

The fey trickster gains the [quickling's](ref/monster/quickling) supernatural speed ability
(_Pathfinder RPG Bestiary 2_ 227).

### Rusalka {#rusalka}

The fey trickster gains the [rusalka's](ref/monster/rusalka) tresses ability and four tress primary
[natural attacks](ref/umr/natural-attacks) similar to those of a rusalka (_Pathfinder RPG Bestiary
3_ 232).

This ability replaces rule minds.
