+++
id = "ref/feat/threatening-illusion"
kind = "feat"
title = "Threatening Illusion"
aon = "FeatDisplay.aspx?ItemName=Threatening%20Illusion"
source_ids = ["gnomes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "threatening_illusion", path = "json/feat16.json" },
]
[[sources]]
publication = "gnomes-of-golarion"
page = "27"

[fields]
kind = "feat"
feat_types = ["Metamagic"]
prerequisites = "Spell Focus (illusion), Gnome."
prerequisite_feats = ["ref/feat/spell-focus"]
benefit = "You can use this metamagic feat only on illusion (figment) spells."
+++

## Threatening Illusion (Metamagic)

You've mastered the art of making illusions that force foes to divide their attention in combat.\
**Prerequisites:** [Spell Focus](ref/feat/spell-focus) (illusion), [Gnome](ref/race/gnome).\
**Benefit:** You can use this metamagic feat only on illusion (figment) spells.

A threatening illusion spell causes one target to believe your illusion is a threat. Choose one
5-foot square within the area of your illusion; that square threatens the target as long as it is
adjacent. Thus, if you or an ally is on the opposite side of the target, it is considered
[flanking](ref/rule/flanking).

Normally the area must contain an illusory creature of Small or Medium size. However, you can select
one square of a larger illusory creature to threaten the target. For example, an illusory Large
[ogre](ref/monster/ogre) takes up four 5-foot squares; you select one square to be the source of the
threat, and its other three squares do not threaten anyone.

If the target has reason to believe there is an invisible creature in the vicinity, even an auditory
illusion with no visual elements (such as [ghost sound](ref/spell/ghost-sound)) is sufficient to
convince the target that the selected square contains an actual threat. As long as you maintain the
illusion, you can change the location of the threatening square as a swift action.

When you threaten a target with this spell, the foe may make a Will save to disbelieve (DC 10 +
threatening spell's level + your spellcasting ability score modifier). If the target makes this
save, the threatening effect of this feat no longer applies to it.

A threatening illusion takes up a spell slot one level higher than normal.
