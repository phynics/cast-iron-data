+++
id = "ref/arc-occultist/reliquarian"
kind = "archetype"
title = "Reliquarian"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Reliquarian"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reliquarian", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "occult-origins"
page = "14"

[fields]
kind = "archetype"
replaces = ["Knacks"]
alters = ["Spells", "Focus powers", "Implements", "Mental focus"]
+++

Not all occultists derive their power from psychic impressions left on objects. Some find faith
first, and draw out the divine potential in religious relics. Many see these religious scholars as
eccentrics or heretics who pilfer holy magic with their bizarre rituals.

**Prerequisites:** Must worship a deity, and must be within one step of her deity's alignment, along
either the law/chaos axis or the good/evil axis.

**Faithful**

**Info:** A reliquarian is proficient with her deity's favored weapon in addition to her normal
weapon and armor proficiencies.

**Spells**

**Alters:** Spells

**Info:** A reliquarian's spells are considered divine spells, not psychic spells. The reliquarian's
spells use verbal components instead of thought components, and somatic components instead of
emotional components, and she uses a _sacred implement_ (see below) as a divine focus.

**Domain**

**Ability:** A reliquarian gains access to one of her deity's [domains](ref/ability/domains). She
treats her occultist level as her cleric level for the purposes of access to domain powers and their
strength. Additionally, the reliquarian adds the domain's spells to her occultist spell list and her
spells known.

**Diminished Focus Power (Su)**

**Alters:** Focus powers

**Info:** A reliquarian learns only the base focus power from one implement school at 1st level. She
gains additional focus powers as normal.

**Sacred Implements (Su)**

**Ability:** A reliquarian gains one implement school. Additionally, the reliquarian gains a relic
of her god, typically a holy symbol of significant age, a fixture from a lost temple, or bone or
hair from a prominent historical figure of the religion. This grants the reliquarian access to one
of her deity's domains, as detailed above. Without this implement, the reliquarian cannot use her
_domain_ powers and must succeed at a [concentration](ref/rule/concentration) check to cast spells
from her _domain._

**Alters:** Implements

**Gained:** At 1st Level

**Special:** All of a reliquarian's future implements must be somehow representative of her faith.

**Orisons**

**Ability:** A reliquarian gains one orison, or 0-level divine spell, each time she selects an
implement school (including when she again selects a school that she has already learned to use.)
These orisons otherwise behave as an occultist's knacks.

**Replaces:** Knacks

**Divine Focus (Su)**

**Alters:** Mental focus

**Info:** A reliquarian uses her Wisdom modifier, rather than her Intelligence modifier, to
determine the amount of mental focus available to her each day.
