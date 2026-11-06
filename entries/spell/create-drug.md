+++
id = "ref/spell/create-drug"
kind = "spell"
title = "Create Drug"
source_ids = ["book-of-the-damned", "pathfinder-99-dance-of-the-damned"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_drug", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 round"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "1 dose of a drug/3 levels" },
]
duration = "1 minute"
saving_throw = "none (see below)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Alchemist, Druid, Hunter, Investigator, Occultist\
4: Cleric, Oracle, Warpriest
Casting time: 1 round
Components: V, S
Range: 0 ft.
Duration: 1 minute
Saving throw: none (see below)
Spell resistance: no
Effect: 1 dose of a drug/3 levels
Subschool: Creation
:::

**Sources:** Book of the Damned pg 183, Pathfinder \#99: Dance of the Damned pg 74

The caster conjures into being one of the following drugs: [aether](ref/drug/aether),
[flayleaf](ref/drug/flayleaf), [opium](ref/drug/opium), [pesh](ref/drug/pesh),
[scour](ref/drug/scour), [shiver](ref/drug/shiver), or [zerk](ref/drug/zerk). (At the GM's
discretion, other drugs of similar power can be included on this list.) The drug doses the caster
creates with this spell must be used within 1 minute of being conjured, or they dissolve into
worthless dust or evaporate into noxious but fleeting vapors, though the effects of the drug may
last far longer if taken before it decays.

The drugs created by this spell cannot be sold, but they can be given to other creatures. A creature
that takes a dose of one of these drug typically must be either willing or helpless, though some
drugs might be inhaled, applied to injuries, or secretly slipped into food if the caster acts
swiftly (see each drug's description). The DC to resist a drug created by this spell is based on the
conjurer's caster level, not the DC listed in the common versions of the drug. For more information,
see [Drugs and Addiction](ref/rule/drugs-and-addiction).

As a special use of this spell, a lawful evil worshiper of Mahathallah, the Dowager of Illusions,
can create doses of the drug [adyton](ref/drug/adyton). A Mahathallah worshiper can create adyton
only once per week, regardless of her level or how many times she casts this spell. The spell
otherwise functions - and creates as many doses - as normal.

#### Adyton

The drug adyton is central to Mahathallah's worship and the spreading of her mysteries. It can be
purchased only from worshipers of Mahathallah, and typically only by servants of the goddess.

**Adyton**\
**Type** contact; **Addiction** major, Fortitude DC 20\
**Price** 2,000 gp\
**Effect** An affected creature that succeeds at an additional DC 20 Will saving throw has its
consciousness transported into the [mindscape](ref/rule/mindscapes) called the Adyton, where it can
linger for as long as it likes and return as a full-round action whenever it so pleases. Those that
fail this secondary saving throw sleep fitfully for 2d4 hours and wake remembering snippets of
surreal dreams.\
**Damage** 1d4 Str damage
