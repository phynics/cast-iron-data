+++
id = "ref/spell/unconscious-agenda"
kind = "spell"
title = "Unconscious Agenda"
source_ids = ["rise-of-the-runelords-anniversary-edition", "pathfinder-5-sins-of-the-saviors"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unconscious_agenda", path = "json/spells11.json" },
]
[[sources]]
publication = "rise-of-the-runelords-anniversary-edition"
page = "419"
[[sources]]
publication = "pathfinder-5-sins-of-the-saviors"
page = "61"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "One humanoid" },
]
duration = "one week/level or until discharged (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Arcanist, Bard, Inquisitor, Skald, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: one week/level or until discharged (D)
Saving throw: Will negates
Spell resistance: yes
Target: One humanoid
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

This spell plants a subconscious directive in the target's mind that forces him to act as you
dictate when specific circumstances arise. The target humanoid can be either conscious or
unconscious, but must understand your language. Upon casting this spell, you must state a course of
action you wish the target to take. This course of action must be described in 20 words or fewer.
You must then state the condition under which you wish the target to take this action, also
describing it in 20 or fewer words. Actions or conditions more elaborate than 20 words cause the
spell to fail. Unconscious agenda cannot compel a target to kill himself, though it can compel him
to perform exceedingly dangerous acts, face impossible odds, or undertake almost any other course of
activity. You cannot issue new commands to the target after the spell is cast.

If the target fails his save against this spell, he is not compelled to act in any way until the
specified trigger circumstances are encountered. He also has no knowledge of the details of the
spell affecting him, and has no memory of the last 10 minutes (although he might come to notice the
missing time or the presence of the caster). He can function as he wishes until the events you
detailed as the condition take place. Upon experiencing the prerequisite condition, the target is
forced to perform the course of action you described as per the spell dominate person. (If the
compelled action is against the victim's nature, he immediately gains a new saving throw at a +5
bonus against the spell to end its effects.) For the next hour, the target acts as you dictated,
doing all he can to fulfill your command. If, at the end of the hour, the target still has not
completed your command, the target is released from the enchantment and the spell ends. Once the
course of action is completed, the spell ends. The target has full memory of acts performed during
this hour.

It's difficult to detect an unconscious agenda before the spell is triggered. Casting detect magic
on one affected by it only reveals an aura of enchantment if the caster of detect magic has a higher
caster level then the caster of unconscious agenda. Even if the spell is detected, it can only be
removed by [break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish).
[Dispel magic](ref/spell/dispel-magic) does not affect unconscious agenda.
