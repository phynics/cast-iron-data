+++
id = "ref/spell/word-of-beckoning"
kind = "spell"
title = "Word of Beckoning"
source_ids = ["core-rulebook", "mythic-adventures", "pathfinder-131-the-reapers-right-hand"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "word_of_beckoning", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/sending" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 5 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M/DF (fine copper wire)"
range = "see text"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Medium, Mesmerist\
4: Cleric, Inquisitor, Occultist, Oracle, Psychic, Shaman, Summoner, Warpriest\
5: Alchemist, Arcanist, Investigator, Sorcerer, Spiritualist, Unchained Summoner, Wizard
Casting time: 10 minutes
Components: V, S, M/DF (fine copper wire)
Range: see text
Duration: 1 round; see text
Saving throw: none
Spell resistance: no
Target: one creature
:::

### Mythic Sending

**Sources:** Mythic Adventures pg 107

You can contact a number of additional creatures equal to your tier. Each creature must receive the
same message, and can communicate back only to you.

_Augmented (3rd):_ If you expend two uses of mythic power, you can send the message to unfamiliar
creatures (using the same number of creatures as non-augmented mythic sending). You must either
describe the intended recipients in general or specific terms (such as "orcs," "the queen of this
country," or "left-handed half-elven males") or specify restrictions such as range, creature type,
and alignment (such as "all good-aligned humanoids in the castle on the hill"). If a greater number
of creatures meet your description than the maximum number you can send to, the closest ones to you
receive the message.

### Word of Beckoning

**Sources:** Pathfinder \#131: The Reaper's Right Hand pg 72

This spell functions like [sending](ref/spell/sending), except the subject also receives knowledge
of a command word that, when spoken, summons you to the open space nearest to the subject. The
subject must speak the command word within 1 round of knowing it to summon you, although the subject
isn't obligated to speak it. You can be transported any distance within a plane but cannot travel
between planes. You can bring along objects as long as their weight doesn't exceed your maximum
load. You may also bring one additional willing Medium or smaller creature (carrying gear or objects
up to its maximum load) or its equivalent per three caster levels. A Large creature counts as two
Medium creatures, a Huge creature counts as four Medium creatures, and so forth. All creatures to be
transported must be in contact with one another, and at least one of those creatures must be in
contact with you.
