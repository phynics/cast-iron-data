+++
id = "ref/spell/sarzari-shadow-memory"
kind = "spell"
title = "Sarzari Shadow Memory"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sarzari_shadow_memory", path = "json/spells8.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "160"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 hour"
components = "V, S, M (a work of art bearing your target's likeness worth at least 1,500 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 month"
saving_throw = "Will negates (harmless)"
spell_resistance = "no (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 6: Arcanist, Bard, Cleric, Inquisitor, Oracle, Psychic, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 hour
Components: V, S, M (a work of art bearing your target's likeness worth at least 1,500 gp)
Range: personal
Duration: 1 month
Saving throw: Will negates (harmless)
Spell resistance: no (harmless)
Target: you
:::

While casting this spell, you slowly destroy a piece of art bearing your victim's likeness and
beseech Achaekek to grant you access to the knowledge and lore contained within the innermost
sanctum of the Crimson Citadel, the Sarzari Library. This endows you with information that could
facilitate the target's assassination by your hands. This information must be chosen from one of the
three following categories: back doors, character, or weakness.

"Back doors" informs you of hidden passages and other means of navigation within your target's home.
While inside your target's home, you gain a +10 insight bonus on Perception checks and gain the
constant benefits of [detect secret doors](ref/spell/detect-secret-doors) and
[find traps](ref/spell/find-traps). You automatically see through any illusory walls in the target's
home.

"Character" lets you know of a compromising detail about your target's personal life, giving you a
+10 bonus on Bluff, Diplomacy, and Intimidate checks when attempting to gather information about
your contracted victim from other people. Your target takes a -2 penalty on all saving throws
against mind-affecting effects you generate, and you gain a +4 bonus on caster level checks you
attempt to overcome the target's [spell resistance](ref/rule/spell-resistance).

"Weakness" grants you knowledge of physical vulnerabilities your target has, as well as information
about the target's [damage reduction](ref/rule/damage-reduction), immunities, and other defensive
abilities. If these vulnerabilities and defenses change during the spell's duration, you immediately
know. You automatically confirm all critical threats against the target.

Once your victim is slain or a month has passed (whichever comes first), the information you gained
from the spell fades. While you can recall certain elements of these memories, you no longer gain
any of the benefits associated with the spell. You can only have one target affected by Sarzari
shadow memory at any one time; if you cast this spell a second time while a previous casting is
still active, the effects of the new spell replace the effects of the old one.
