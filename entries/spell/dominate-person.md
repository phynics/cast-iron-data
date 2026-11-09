+++
id = "ref/spell/dominate-person"
kind = "spell"
title = "Dominate Person"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dominate_person", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "274"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Mesmerist, Skald\
5: Arcanist, Occultist, Psychic, Shaman, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one humanoid
Subschool: Compulsion
Descriptors: mind-affecting
:::

You can control the actions of any humanoid creature through a telepathic link that you establish
with the subject's mind.

If you and the subject have a common language, you can generally force the subject to perform as you
desire, within the limits of its abilities. If no common language exists, you can communicate only
basic commands, such as "Come here," "Go there," "Fight," and "Stand still." You know what the
subject is experiencing, but you do not receive direct sensory input from it, nor can it communicate
with you telepathically.

Once you have given a dominated creature a command, it continues to attempt to carry out that
command to the exclusion of all other activities except those necessary for day-to-day survival
(such as sleeping, eating, and so forth). Because of this limited range of activity, a Sense Motive
check against DC 15 (rather than DC 25) can determine that the subject's behavior is being
influenced by an enchantment effect (see the
[Sense Motive skill description](ref/skill/sense-motive)).

Changing your orders or giving a dominated creature a new command is a move action.

By concentrating fully on the spell (a standard action), you can receive full sensory input as
interpreted by the mind of the subject, though it still can't communicate with you. You can't
actually see through the subject's eyes, so it's not as good as being there yourself, but you still
get a good idea of what's going on.

Subjects resist this control, and any subject forced to take actions against its nature receives a
new saving throw with a +2 bonus. Obviously self-destructive orders are not carried out. Once
control is established, the range at which it can be exercised is unlimited, as long as you and the
subject are on the same plane. You need not see the subject to control it.

If you don't spend at least 1 round concentrating on the spell each day, the subject receives a new
saving throw to throw off the domination.

[Protection from evil](ref/spell/protection-from-evil) or a similar spell can prevent you from
exercising control or using the telepathic link while the subject is so warded, but such an effect
does not automatically dispel it.
