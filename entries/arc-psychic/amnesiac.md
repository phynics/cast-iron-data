+++
id = "ref/arc-psychic/amnesiac"
kind = "archetype"
title = "Amnesiac"
aon = "ArchetypeDisplay.aspx?FixedName=Psychic%20Amnesiac"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "amnesiac", path = "json/archetypes_psychic.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/psychic" },
]
[[sources]]
publication = "occult-adventures"
page = "104"

[fields]
kind = "archetype"
alters = ["Spellcasting"]
+++

The amnesiac once possessed great psychic power, but mental blocks - resulting from either a
traumatic event or intentional implantation - have caused her to forget what she knew before. The
amnesiac's struggle to control her psychic magic leads to wild and unpredictable results.

**Repressed Memories**

**Info:** All the amnesiac's older memories have been deeply hidden, as though she had been affected
by multiple [repress memory](ref/spell/repress-memory) spells. She isn't prevented from remembering
things that happen over the course of a game, but might be forgetful. If the amnesiac's memories are
ever restored, she loses this archetype and reverts to a standard psychic.

**Spells**

**Action:** Ability

**Alters:** Spellcasting

An amnesiac's ability to cast psychic spells is the same as that of the psychic class, with the
following exceptions.

An amnesiac's faulty memory makes remembering and casting spells difficult, but the increased
flexibility can be a great benefit. Instead of choosing a number of spells known from the
[psychic's](ref/class/psychic) Spells Known table, an amnesiac accesses spells she knew the previous
day from the recesses of her mind. This requires 1 hour of meditation. Each day, for each spell
level the amnesiac can cast, she retains a number of spells known equal to half the number listed on
the Spells Known table, rounded up. These spells must be selected from spells the amnesiac knew the
previous day (including any spells she remembered using _spell recollection;_ see below). The
remainder of her spells known (half that of a normal psychic, rounded down) become amnesia slots,
which the amnesiac can use with her _spell recollection_ ability. To determine the spells she knows
on the day when she first takes this archetype, the amnesiac picks any one 1st-level spell from the
psychic spell list.

This change to spells doesn't apply to knacks (0-level spells) or discipline spells, which function
the same way they do for a normal psychic. When the amnesiac gains access to 3rd-level spells, she
gains full recall of her 1st-level spells and no longer gains 1st-level amnesia slots, instead
gaining the full number of 1st-level spells known from the Spells Known table and casting them as a
normal psychic. When this happens, the amnesiac can select any level-appropriate spells from the
psychic spell list as her spells known, even if they were never among the spells she prepared or
recalled; once selected, these spells can no longer be changed, as with a normal psychic. Each time
the psychic gains access to a new level of spells, she gains full memory of spells 2 levels lower in
the same way (gaining full memory and permanently selecting her 2nd-level spells when she gains
access to 4th-level spells, and so on).

**Spell Recollection (Ex)**

**Action:** Swift Action

**Usage:** Once per hour

**Usage:** Once per hour

An amnesiac can attempt to remember any spell from the psychic spell list of her choice from either
of the 2 highest spell levels she can cast. When she does, she rolls on the table below to determine
the result. Because the mental stress of combat brings memories to the surface more easily, the
amnesiac adds 1d10 to this roll's result if she's in combat when she attempts to recall a spell.
Regardless of the result, the amnesiac expends an amnesia slot of the appropriate level for the
spell she is attempting to remember; she must cast the spell remembered (if any) using that amnesia
slot during the same round, or the spell slot is lost without effect. Once a spell has been
remembered in this way, the amnesiac can cast it as one of her spells known for the rest of the day
(even if she failed to cast the spell during the round in which she remembered it), unless _spell
recollection_ allowed her to cast a spell of a higher level than she would normally be able to cast.

|d%|Result|
| --- | --- |
|01-10|The amnesiac is unable to cast spells this round.|
|11-35|The amnesiac can't remember the new spell (but can still cast spells this round).|
|36-95|The amnesiac remembers and can cast the new spell.|
|96+|The amnesiac can choose to treat this result as 36-95. Alternatively, once per day, she can instead temporarily recall any spell from the psychic spell list that's 1 level higher than the spell she's attempting to remember. When she does, her caster level counts as the minimum caster level required to cast the higher-level spell, and she forgets the spell after it's cast.|
